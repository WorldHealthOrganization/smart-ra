#!/usr/bin/env python3
"""Add a DTH's elements, relationships and views to an Archi model, by script.

Usage:
    python3 -I tools/archimate-dth/add_views.py <spec.py> <in.archimate> <out.archimate>

The model is Archi's zipped archive (model.xml plus images/). This script
never reorders or rewrites what is already there: it inserts new XML into the
right folders and leaves every other byte alone, so a diff of model.xml shows
only what was added. Running it twice on its own output adds nothing.

A spec (e.g. dth_sc.py) is a Python file defining:

  SOURCE    the handbook it comes from, written into every new element
  ELEMENTS  {key: (archimateType, name, documentation, {property: value})}
  EXISTING  {key: archi id}  elements reused from the base model, never copied
  RELATIONS [(type, sourceKey, targetKey[, {xmlAttribute: value}])]
            e.g. ("Access", a, b, {"accessType": 1}); Archi's accessType is
            0 write (its default), 1 read, 2 access, 3 read/write
  VIEWS     [(name, documentation, layout)]  layout: a tree of
            ("box", key) | ("group", key, cols, [children])
            | ("row", [children]) | ("col", [children])
            | ("gap",) an empty leaf-sized space, to line columns up
  VIEW_CONNECTIONS {view name: [(type, sourceKey, targetKey)]}  drawn lines
  EXISTING_RELATIONS optional {(type, sourceKey, targetKey): archi id}
            relationships already in the base model, so a new view can
            draw them through VIEW_CONNECTIONS without copying them
  RENAMES   optional {key: new name} for EXISTING elements; the old name is
            kept as property formerName, and a renamed element is left alone
  PROPERTIES optional {key: {property: value}} for any element, new or
            existing; a property the element already has is left alone

Ids are uuid5 of the spec's namespace and the key, so they are stable across
runs: a later edit of the spec keeps every id it does not change. Shared
work: dth-sc and dth-pc both apply their specs through this script.
"""

import html
import importlib.util
import re
import sys
import uuid
import zipfile

LEAF_W, LEAF_H, PAD, HEAD = 170, 55, 12, 28


def load(path):
    spec = importlib.util.spec_from_file_location("spec", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def esc(s):
    return html.escape(s, quote=True)


class Ids:
    def __init__(self, ns):
        self.ns = uuid.uuid5(uuid.NAMESPACE_URL, ns)

    def __call__(self, *parts):
        return "id-" + uuid.uuid5(self.ns, "/".join(parts)).hex


def insert_in_top_folder(xml, ftype, text):
    m = re.search(r'\n  <folder [^>]*type="%s"[^>]*?(/?)>' % ftype, xml)
    if not m:
        raise SystemExit(f"no top-level folder of type {ftype}")
    if m.group(1) == "/":  # empty folder written as <folder .../>
        opened = m.group(0)[:-2] + ">"
        return xml[:m.start()] + opened + text + "\n  </folder>" + xml[m.end():]
    close = xml.index("\n  </folder>", m.end())
    return xml[:close] + text + xml[close:]


def insert_in_named_subfolder(xml, parent_type, name, text):
    """Insert text at the end of the folder called name, at any depth under the top folder."""
    top = re.search(r'\n  <folder [^>]*type="%s"[^>]*>' % parent_type, xml)
    m = re.search(r'\n( +)<folder name="%s" id="[^"]+">' % re.escape(name), xml[top.end():])
    if not m:
        raise SystemExit(f"no folder {name!r} under {parent_type}")
    start = top.end() + m.end()
    close = xml.index("\n" + m.group(1) + "</folder>", start)
    return xml[:close] + text + xml[close:]


FOLDER_OF = {
    "business": ("BusinessActor BusinessRole BusinessCollaboration BusinessInterface BusinessProcess "
                 "BusinessFunction BusinessInteraction BusinessEvent BusinessService BusinessObject Contract "
                 "Representation Product"),
    "application": ("ApplicationComponent ApplicationCollaboration ApplicationInterface ApplicationFunction "
                    "ApplicationInteraction ApplicationProcess ApplicationEvent ApplicationService DataObject"),
    "technology": ("Node Device SystemSoftware TechnologyCollaboration TechnologyInterface Path "
                   "CommunicationNetwork TechnologyFunction TechnologyProcess TechnologyInteraction "
                   "TechnologyEvent TechnologyService Artifact"),
    "motivation": "Stakeholder Driver Assessment Goal Outcome Principle Requirement Constraint Meaning Value",
    "strategy": "Resource Capability ValueStream CourseOfAction",
    "other": "Location Grouping Junction",
}


def folder_for(t):
    for f, types in FOLDER_OF.items():
        if t in types.split():
            return f
    raise SystemExit(f"no folder for type {t}")


def size(node):
    if node[0] in ("box", "gap"):
        return LEAF_W, LEAF_H
    if node[0] == "col":
        sizes = [size(k) for k in node[1]]
        return max(w for w, _ in sizes), sum(h for _, h in sizes) + PAD * (len(sizes) - 1)
    kids = node[3] if node[0] == "group" else node[1]
    cols = node[2] if node[0] == "group" else len(kids)
    sizes = [size(k) for k in kids]
    rows = [sizes[i:i + cols] for i in range(0, len(sizes), cols)]
    w = max(sum(s[0] for s in r) + PAD * (len(r) - 1) for r in rows) if rows else LEAF_W
    h = sum(max(s[1] for s in r) for r in rows) + PAD * (len(rows) - 1) if rows else 0
    if node[0] == "group":
        return w + 2 * PAD, h + HEAD + 2 * PAD
    return w, h


def place(node, x, y, ids, view, idx, out, depth):
    """Write node's <child> XML at (x, y) relative to its parent; return its XML."""
    ind = "  " * depth
    if node[0] == "gap":
        return ""
    if node[0] == "col":
        parts, cy = [], y
        for k in node[1]:
            parts.append(place(k, x, cy, ids, view, idx, out, depth))
            cy += size(k)[1] + PAD
        return "".join(parts)
    if node[0] == "row":
        parts, cx = [], x
        for k in node[1]:
            parts.append(place(k, cx, y, ids, view, idx, out, depth))
            cx += size(k)[0] + PAD
        return "".join(parts)
    key = node[1]
    w, h = size(node)
    oid = ids("view", view, "obj", key)
    out[key] = oid
    inner = ""
    if node[0] == "group":
        kids, cols = node[3], node[2]
        cy, cx, row_h = HEAD + PAD, PAD, 0
        for i, k in enumerate(kids):
            if i and i % cols == 0:
                cy += row_h + PAD
                cx, row_h = PAD, 0
            kw, kh = size(k)
            inner += place(k, cx, cy, ids, view, idx, out, depth + 1)
            cx += kw + PAD
            row_h = max(row_h, kh)
    return (f'\n{ind}<child xsi:type="archimate:DiagramObject" id="{oid}" archimateElement="{idx[key]}"'
            f'@@TC:{oid}@@>\n{ind}  <bounds x="{x}" y="{y}" width="{w}" height="{h}"/>'
            f"@@SC:{oid}@@{inner}\n{ind}</child>")


def add_property(xml, eid, key, value):
    """Give element eid the property key=value, unless it has that key already."""
    m = re.search(r'<element [^>]*?id="' + re.escape(eid) + r'"[^>]*?(/?)>', xml)
    prop = f'\n      <property key="{esc(key)}" value="{esc(value)}"/>'
    if m.group(1):  # self-closing: give it a body
        return xml[:m.end() - 2] + ">" + prop + "\n    </element>" + xml[m.end():], True
    close = xml.index("</element>", m.end())
    if f'<property key="{esc(key)}"' in xml[m.end():close]:
        return xml, False
    # properties come after any documentation, before </element>
    return xml[:m.end()] + xml[m.end():close].rstrip() + prop + "\n    " + xml[close:], True


def main(argv):
    spec_path, src, dst = argv
    s = load(spec_path)
    ids = Ids(s.NAMESPACE)
    with zipfile.ZipFile(src) as z:
        xml = z.read("model.xml").decode("utf-8")
        others = {n: z.read(n) for n in z.namelist() if n != "model.xml"}

    idx = dict(s.EXISTING)
    for key, eid in s.EXISTING.items():
        if f'id="{eid}"' not in xml:
            raise SystemExit(f"EXISTING {key} = {eid} is not in the base model")
    added = 0
    for key, new in getattr(s, "RENAMES", {}).items():
        eid = s.EXISTING[key]
        m = re.search(r'(<element [^>]*?)name="([^"]*)"([^>]*?id="' + re.escape(eid) + r'"[^>]*?)(/?)>', xml)
        if not m or m.group(2) == esc(new):
            continue
        xml = xml[:m.start()] + f'{m.group(1)}name="{esc(new)}"{m.group(3)}{m.group(4)}>' + xml[m.end():]
        xml, _ = add_property(xml, eid, "formerName", m.group(2))
        added += 1
    for key, (etype, name, doc, props) in s.ELEMENTS.items():
        eid = ids("element", key)
        idx[key] = eid
        if f'id="{eid}"' in xml:
            continue
        props = dict(props)
        props.setdefault("source", s.SOURCE)
        body = f"\n      <documentation>{esc(doc)}</documentation>" if doc else ""
        body += "".join(f'\n      <property key="{esc(k)}" value="{esc(v)}"/>' for k, v in props.items())
        xml = insert_in_top_folder(xml, folder_for(etype),
                                   f'\n    <element xsi:type="archimate:{etype}" name="{esc(name)}" id="{eid}">{body}\n    </element>')
        added += 1

    for key, props in getattr(s, "PROPERTIES", {}).items():
        for k, v in props.items():
            xml, done = add_property(xml, idx[key], k, v)
            added += done

    rel_ids = dict(getattr(s, "EXISTING_RELATIONS", {}))
    for (rtype, a, b), rid in rel_ids.items():
        if f'id="{rid}"' not in xml:
            raise SystemExit(f"EXISTING_RELATIONS {rtype} {a}->{b} = {rid} is not in the base model")
    for rtype, a, b, *rest in s.RELATIONS:
        rid = ids("rel", rtype, a, b)
        rel_ids[(rtype, a, b)] = rid
        if f'id="{rid}"' in xml:
            continue
        extra = "".join(f' {k}="{esc(str(v))}"' for k, v in (rest[0] if rest else {}).items())
        xml = insert_in_top_folder(xml, "relations",
                                   f'\n    <element xsi:type="archimate:{rtype}Relationship" id="{rid}" source="{idx[a]}" target="{idx[b]}"{extra}/>')
        added += 1

    for name, doc, layout in s.VIEWS:
        vid = ids("view", name)
        if f'id="{vid}"' in xml:
            continue
        objs = {}
        body = place(layout, 24, 24, ids, name, idx, objs, 4)
        tcs, scs = {}, {}
        for rtype, a, b, *_ in s.VIEW_CONNECTIONS.get(name, []):
            rid = rel_ids[(rtype, a, b)]
            cid = ids("view", name, "conn", rtype, a, b)
            scs.setdefault(objs[a], []).append(
                f'\n          <sourceConnection xsi:type="archimate:Connection" id="{cid}" source="{objs[a]}" target="{objs[b]}" archimateRelationship="{rid}"/>')
            tcs.setdefault(objs[b], []).append(cid)
        body = re.sub(r"@@TC:([^@]+)@@", lambda m: f' targetConnections="{" ".join(tcs[m.group(1)])}"' if m.group(1) in tcs else "", body)
        body = re.sub(r"@@SC:([^@]+)@@", lambda m: "".join(scs.get(m.group(1), [])), body)
        docx = f"\n        <documentation>{esc(doc)}</documentation>" if doc else ""
        view = (f'\n      <element xsi:type="archimate:ArchimateDiagramModel" name="{esc(name)}" id="{vid}">{docx}'
                f'\n        <property key="source" value="{esc(s.SOURCE)}"/>{body}\n      </element>')
        xml = insert_in_named_subfolder(xml, "diagrams", s.VIEW_FOLDER, view)
        added += 1

    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("model.xml", xml.encode("utf-8"))
        for n, b in others.items():
            z.writestr(n, b)
    print(f"{dst}: {added} added")


if __name__ == "__main__":
    main(sys.argv[1:])
