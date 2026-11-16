#!/usr/bin/env python3
"""Copy views, box for box, from one Archi model into another, by script.

Usage:
    python3 -I tools/archimate-dth/copy_views.py <spec.py> <from.archimate> <in.archimate> <out.archimate>

add_views.py lays a view out from a tree. This script is for a view that is
already drawn in another model, whose layout should be kept as it is: it
copies the view with every box's bounds and every line's bendpoints, and
the elements and relationships the view shows.

A spec (e.g. dpi_h_layered.py) is a Python file defining:

  NAMESPACE  for the new ids: uuid5 of it and the source id, so a re-run
             makes the same ids and adds nothing
  SOURCE     written as property `source` on every copied element
  VIEW_FOLDER the folder under Views the copies go in
  VIEWS      {source view id: new view name}
  REUSE      {(type, source name): target element id}  elements the target
             model already holds: the views draw those, nothing is copied
  NAMES      optional {(type, source name): name}  a copied element's name in
             the target, when the document names it differently; the source
             name is kept as property formerName

Elements are matched by type and name, not by id: a source model that drew
each view with its own copy of "Client Registry" gets one Client Registry in
the target, shown on every view.

A relationship is reused when the target already has one of the same type
between the same two (mapped) elements; otherwise it is copied. Like
add_views.py, this only inserts XML, so a diff of model.xml shows only what
was added.
"""

import html
import importlib.util
import re
import sys
import uuid
import zipfile

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from add_views import esc, folder_for, insert_in_named_subfolder, insert_in_top_folder  # noqa: E402


def load(path):
    spec = importlib.util.spec_from_file_location("spec", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def read(path):
    """model.xml and any other archive members; a plain XML model has none."""
    if not zipfile.is_zipfile(path):
        with open(path, encoding="utf-8") as f:
            return f.read(), {}
    with zipfile.ZipFile(path) as z:
        return z.read("model.xml").decode("utf-8"), {n: z.read(n) for n in z.namelist() if n != "model.xml"}


def element_text(xml, eid):
    """The whole <element ...> ... </element> (or self-closing) text with id eid."""
    m = re.search(r'\n( *)<element [^>]*?\bid="' + re.escape(eid) + r'"[^>]*?(/?)>', xml)
    if not m:
        raise SystemExit(f"no element {eid}")
    if m.group(2) == "/":
        return m.group(0)[1:], m.group(1)
    end = xml.index("\n" + m.group(1) + "</element>", m.end()) + len(m.group(1)) + len("\n</element>")
    return xml[m.start() + 1:end], m.group(1)


def reindent(text, old, new):
    return "\n".join(new + line[len(old):] if line.startswith(old) else line for line in text.split("\n"))


def attr(text, name):
    m = re.search(r'\b' + name + r'="([^"]*)"', text)
    return m.group(1) if m else None


def main(argv):
    spec_path, src_path, base_path, dst = argv
    s = load(spec_path)
    ns = uuid.uuid5(uuid.NAMESPACE_URL, s.NAMESPACE)
    new_id = lambda *parts: "id-" + uuid.uuid5(ns, "/".join(parts)).hex  # noqa: E731
    src, _ = read(src_path)
    xml, others = read(base_path)
    names = getattr(s, "NAMES", {})
    for key, eid in s.REUSE.items():
        if f'id="{eid}"' not in xml:
            raise SystemExit(f"REUSE {key} = {eid} is not in the target model")

    views = {vid: element_text(src, vid)[0] for vid in s.VIEWS}
    elems = sorted({e for v in views.values() for e in re.findall(r'archimateElement="([^"]+)"', v)})
    rels = sorted({r for v in views.values() for r in re.findall(r'archimateRelationship="([^"]+)"', v)})
    key = {}
    for e in elems:
        text, _ = element_text(src, e)
        key[e] = (attr(text, "xsi:type").split(":")[1], html.unescape(attr(text, "name")))
    emap = {e: s.REUSE.get(key[e]) or new_id("element", *key[e]) for e in elems}
    added = 0

    for e in elems:
        if key[e] in s.REUSE or f'id="{emap[e]}"' in xml:
            continue
        text, ind = element_text(src, e)
        etype = key[e][0]
        text = text.replace(f'id="{e}"', f'id="{emap[e]}"', 1)
        props = [("source", s.SOURCE)]
        if key[e] in names:
            props.append(("formerName", key[e][1]))
            text = re.sub(r'\bname="[^"]*"', f'name="{esc(names[key[e]])}"', text, count=1)
        p = "".join(f'\n{ind}  <property key="{esc(k)}" value="{esc(v)}"/>' for k, v in props)
        if text.endswith("/>"):
            text = text[:-2] + ">" + p + f"\n{ind}</element>"
        else:
            text = text[: text.rindex(f"\n{ind}</element>")] + p + f"\n{ind}</element>"
        xml = insert_in_top_folder(xml, folder_for(etype), "\n" + reindent(text, ind, "    "))
        added += 1

    rmap = {}
    for r in rels:
        text, ind = element_text(src, r)
        rtype, a, b = attr(text, "xsi:type"), attr(text, "source"), attr(text, "target")
        if a not in emap or b not in emap:
            raise SystemExit(f"relationship {r} has an end that is not on a copied view")
        same = re.search(r'<element xsi:type="' + re.escape(rtype) + r'" id="([^"]+)" source="' + emap[a]
                         + r'" target="' + emap[b] + '"', xml)
        if same:
            rmap[r] = same.group(1)
            continue
        rmap[r] = new_id("rel", r)
        text = text.replace(f'id="{r}"', f'id="{rmap[r]}"', 1)
        text = text.replace(f'source="{a}"', f'source="{emap[a]}"', 1).replace(f'target="{b}"', f'target="{emap[b]}"', 1)
        xml = insert_in_top_folder(xml, "relations", "\n" + reindent(text, ind, "    "))
        added += 1

    for vid, text in views.items():
        nvid = new_id("view", vid)
        if f'id="{nvid}"' in xml:
            continue
        _, ind = element_text(src, vid)
        local = {i: new_id("view", vid, i) for i in re.findall(r'\bid="([^"]+)"', text)}
        local[vid] = nvid

        def sub_ids(m):
            return m.group(1) + '="' + " ".join(local.get(i, i) for i in m.group(2).split()) + '"'

        text = re.sub(r'\b(id|source|target|targetConnections)="([^"]+)"', sub_ids, text)
        text = re.sub(r'archimateElement="([^"]+)"', lambda m: f'archimateElement="{emap[m.group(1)]}"', text)
        text = re.sub(r'archimateRelationship="([^"]+)"', lambda m: f'archimateRelationship="{rmap[m.group(1)]}"', text)
        text = re.sub(r'\bname="[^"]*"', f'name="{esc(s.VIEWS[vid])}"', text, count=1)
        xml = insert_in_named_subfolder(xml, "diagrams", s.VIEW_FOLDER, "\n" + reindent(text, ind, "      "))
        added += 1

    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("model.xml", xml.encode("utf-8"))
        for n, b in others.items():
            z.writestr(n, b)
    print(f"{dst}: {added} added")


if __name__ == "__main__":
    main(sys.argv[1:])
