#!/usr/bin/env python3
"""Build SMART-RA-Mapper.html from one or more ArchiMate reference models.

Usage:
  python build_ra_mapper.py MODEL [MODEL ...] [-o OUT.html] [-t TEMPLATE] [-l LABEL ...]

MODEL     .archimate file (Archi native XML, Open Group exchange XML, or a
          zipped Archi archive containing model.xml). First model = default version.
-l LABEL  optional label per model (same order); defaults to the model's name.

Example:
  python build_ra_mapper.py ../archimate/draft/WHOBaseFile.archimate \\
         ../archimate/current/WHOBaseFile_prev.archimate \\
         -l "WHO RA (draft)" "WHO RA (previous)" -o ../SMART-RA-Mapper.html
"""
import argparse, json, sys, zipfile, io, re
import xml.etree.ElementTree as ET

XSI = '{http://www.w3.org/2001/XMLSchema-instance}type'

def layer_of(ty):
    if re.match(r'^(Capability|ValueStream|Resource|CourseOfAction)$', ty): return 'Strategy'
    if re.match(r'^(Goal|Driver|Outcome|Value|Stakeholder|Principle|Requirement|Constraint|Assessment|Meaning)$', ty): return 'Motivation'
    if re.match(r'^Business|^(Product|Contract|Representation)$', ty): return 'Business'
    if re.match(r'^Application|^DataObject$', ty): return 'Application'
    if re.match(r'^Technology|^(Node|SystemSoftware|Device|Artifact|CommunicationNetwork|Path)$', ty): return 'Technology'
    if re.match(r'^(WorkPackage|Deliverable|Plateau|Gap)$', ty): return 'Implementation & Migration'
    return 'Other'

def read_xml(path):
    raw = open(path,'rb').read()
    if raw[:2] == b'PK':  # zipped Archi archive
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            name = next((n for n in z.namelist() if n.endswith('.xml')), None)
            if not name: sys.exit(f'{path}: zip contains no xml')
            raw = z.read(name)
    return ET.fromstring(raw.decode('utf-8-sig'))

def strip_ns(tag):
    return tag.split('}')[-1].split(':')[-1]

def parse_model(path):
    root = read_xml(path)
    els, rels = [], []
    if root.find('.//folder') is not None or strip_ns(root.tag)=='model' and root.find('folder') is not None or list(root.iter('folder')):
        pass
    # detect: Archi native has <folder> children; exchange has namespaced <elements>
    native = any(strip_ns(c.tag)=='folder' for c in root)
    name = root.get('name') or ''
    if native:
        def walk(node, pathf):
            for ch in node:
                tg = strip_ns(ch.tag)
                if tg=='folder':
                    walk(ch, (pathf+'/' if pathf else '')+(ch.get('name') or ''))
                elif tg=='element':
                    ty=(ch.get(XSI) or '').replace('archimate:','')
                    if not ty or ty in ('ArchimateDiagramModel','SketchModel'): continue
                    if ty.endswith('Relationship'):
                        rels.append({'t':ty.replace('Relationship',''),'s':ch.get('source'),'g':ch.get('target')})
                    else:
                        d=ch.find('documentation')
                        els.append({'i':ch.get('id'),'t':ty,'n':(ch.get('name') or '').strip(),
                                    'f':pathf or layer_of(ty),'d':(d.text.strip() if d is not None and d.text else '')})
        walk(root,'')
    else:
        ns = root.tag.split('}')[0]+'}' if root.tag.startswith('{') else ''
        nm = root.find(f'{ns}name')
        if nm is not None and nm.text: name = nm.text
        for el in root.findall(f'.//{ns}elements/{ns}element'):
            ty=(el.get(XSI) or '')
            if not ty: continue
            n2=el.find(f'{ns}name'); d=el.find(f'{ns}documentation')
            els.append({'i':el.get('identifier'),'t':ty,'n':(n2.text.strip() if n2 is not None and n2.text else ''),
                        'f':layer_of(ty),'d':(d.text.strip() if d is not None and d.text else '')})
        for r in root.findall(f'.//{ns}relationships/{ns}relationship'):
            rels.append({'t':(r.get(XSI) or ''),'s':r.get('source'),'g':r.get('target')})
    els=[e for e in els if e['n']]
    ids={e['i'] for e in els}
    rels=[{'i':f'id-rel-{k}','t':r['t'],'s':r['s'],'g':r['g']} for k,r in enumerate(rels) if r['t'] and r['s'] in ids and r['g'] in ids]
    return {'modelName':name or path,'modelId':'id-built','source':path,'elements':els,'relationships':rels}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('models', nargs='+')
    ap.add_argument('-o','--out', default='SMART-RA-Mapper.html')
    ap.add_argument('-t','--template', default='template.html')
    ap.add_argument('-l','--labels', nargs='*', default=[])
    a=ap.parse_args()
    versions=[]
    for k,p in enumerate(a.models):
        m=parse_model(p)
        label=a.labels[k] if k<len(a.labels) else m['modelName']
        versions.append({'key':f'v{k}','label':label,'data':m})
        print(f"  {label}: {len(m['elements'])} elements, {len(m['relationships'])} relationships")
    catalog={'versions':versions,'defaultKey':'v0'}
    tpl=open(a.template,encoding='utf-8').read()
    if '__MODEL_JSON__' not in tpl: sys.exit('template missing __MODEL_JSON__ placeholder')
    js=json.dumps(catalog,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
    open(a.out,'w',encoding='utf-8').write(tpl.replace('__MODEL_JSON__',js))
    print(f'built {a.out} ({len(tpl)+len(js)>>10} KB)')

if __name__=='__main__':
    main()
