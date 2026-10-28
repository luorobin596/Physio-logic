#!/usr/bin/env python3
"""Validate package integrity and fixed-table structure; not clinical reasoning."""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('subjective-analysis', 'objective-analysis', 'impression')
SHARED_REFERENCES = ('clinical-contract.md', 'stage-routing.md',
                     'pain-mechanisms.md', 'pain-discussion-catalog.md',
                     'kinetic-chain-analysis.md')
TITLES = {
    'table-1-1': 'Subjective Table 1.1',
    'table-1-2': 'Subjective Table 1.2',
    'table-2-1': 'Table2.1 Preliminary Hypothesis',
    'table-2-2': 'Table2.2 History timeline-S',
    'table-3-1': 'Objective Table 3.1 — Structural Evidence Categorization Analysis',
    'table-3-2': 'Objective Table 3.2 Regions Contributing to Symptoms:',
    'table-4': 'Table4 Updated Hypothesis',
}
MODES = {
    'subjective-initial': ['table-1-1', 'table-1-2'],
    'subjective-synthesis': ['table-2-1', 'table-2-2'],
    'objective': ['table-3-1', 'table-3-2'],
    'impression': ['table-4'],
    'complete': list(TITLES),
}
BASE_CLASSES = ['Bone', 'Cartilage', 'Capsule', 'Ligament', 'Tendon', 'Muscle',
                'Fascia', 'Nerve', 'Vessel', 'Bursa', 'Fat', 'Skin', 'Viscus']
BASE_SYSTEMS = ['Kinetic chain', 'Myofascial lines', 'Nervous system', 'Vessels',
                'Autonomic Nervous System', 'lymphatic system']
APPROVED = {
    'table-1-1': (['Tissue category', 'Adjacent possible sources',
                   'Possible sources of referred pain from remote regions'], BASE_CLASSES),
    'table-1-2': (['Integrated functions or Systems', 'Upstream and Downstream structure',
                   'Regions This System Passes Through'], BASE_SYSTEMS),
    'table-2-1': (['Item', 'Content'], ['Functional limitations', 'pain mechanisms',
                   'Symptoms Stage', 'Irritability', 'Contributing factors',
                   'Precautions / Red Flags', 'Impression']),
    'table-2-2': (['Time Point', 'Symptom or Event'], None),
    'table-3-1': (['Structural classification', 'Specific structure', 'Supporting evidence',
                   'Negating evidence', 'Level of Evidence Support'], BASE_CLASSES),
    'table-3-2': (['Integrated functions or Systems', 'Upstream and Downstream', 'Regions',
                   'Supporting evidence', 'Possibility of Involvement'], BASE_SYSTEMS),
    'table-4': (['Item', 'Content'], ['Primary Symptom Source', 'Secondary / Contributing regions',
                   'Functional limitations', 'Pain mechanisms', 'Key Contributing Factors',
                   'Precautions', 'Impression']),
}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def cells(line):
    return [x.strip() for x in line.strip().strip('|').split('|')]

def parse_tables(text):
    """Read pipe tables with the last recognized approved title as context."""
    found = []
    title = None
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        heading = re.sub(r'^#+\s+', '', lines[i]).strip()
        if heading in TITLES.values():
            title = next(k for k, v in TITLES.items() if v == heading)
        if (lines[i].startswith('|') and i + 1 < len(lines)
                and re.fullmatch(r'[| :\-]+', lines[i + 1]) and '-' in lines[i + 1]):
            headers = cells(lines[i])
            rows = []
            i += 2
            while i < len(lines) and lines[i].startswith('|'):
                row = cells(lines[i])
                require(len(row) == len(headers), f'{title}: cell count differs from header')
                rows.append(row)
                i += 1
            if title:
                found.append((title, headers, rows))
            continue
        i += 1
    return found

def contracts():
    result = {}
    for path in ROOT.glob('skills/*/assets/table-*.md'):
        parsed = parse_tables(path.read_text())
        require(len(parsed) == 1, f'{path}: expected one template table')
        key, head, rows = parsed[0]
        approved_header, approved_rows = APPROVED[key]
        require(head == approved_header, f'{path}: template differs from approved columns')
        if approved_rows is not None:
            require([row[0] for row in rows] == approved_rows,
                    f'{path}: template differs from approved base rows/order')
        result[key] = (head, [row[0] for row in rows])
    require(set(result) == set(TITLES), 'Expected exactly seven table templates')
    return result

def validate_package():
    require({p.name for p in (ROOT / 'skills').iterdir() if p.is_dir()} == set(SKILLS),
            'Active skills must contain exactly the three approved stages')
    for name in SKILLS:
        base = ROOT / 'skills' / name
        content = (base / 'SKILL.md').read_text()
        require(content.startswith('---\n'), f'{name}: missing frontmatter')
        front = content.split('---', 2)[1]
        fields = dict(line.split(': ', 1) for line in front.strip().splitlines())
        require(fields.get('name') == name and fields.get('description', '').strip(),
                f'{name}: invalid required scalar frontmatter')
        for path in base.rglob('*.md'):
            body = path.read_text()
            require(not re.search(r'file-[A-Za-z0-9]{10,}', body), f'{path}: obsolete upload ID')
            for target in re.findall(r'\]\(([^)]+)\)', body):
                if '://' not in target:
                    resolved = (path.parent / target.split('#')[0]).resolve()
                    allowed = (base.resolve(), (ROOT / 'references').resolve())
                    require(resolved.is_file() and any(resolved.is_relative_to(p) for p in allowed),
                            f'{path}: missing or out-of-scope resource {target}')
    for resource in SHARED_REFERENCES:
        require((ROOT / 'references' / resource).is_file(), f'Missing shared reference: {resource}')
        require(not list((ROOT / 'skills').glob(f'*/references/{resource}')),
                f'Shared reference duplicated inside a skill: {resource}')
    for path in (ROOT / 'references').rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if '://' not in target:
                resolved = (path.parent / target.split('#')[0]).resolve()
                require(resolved.is_file() and resolved.is_relative_to(ROOT.resolve()),
                        f'{path}: missing or outside-package resource {target}')
    manifests = [json.loads((ROOT / p).read_text()) for p in
                 ['plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json']]
    require(len({(m['name'], m['version']) for m in manifests}) == 1, 'Manifest identity/version drift')
    require(manifests[0]['$schema'] == 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json',
            'Portable schema declaration missing')
    require(all(m['author'] == manifests[0]['author'] for m in manifests),
            'Manifest author drift')
    portable_interface = manifests[0]['extensions']['com.openai']['interface']
    codex_interface = manifests[1]['interface']
    for label, interface in [('Portable', portable_interface), ('Codex', codex_interface)]:
        subtitle = interface.get('shortDescription')
        require(isinstance(subtitle, str) and 1 <= len(subtitle) <= 30,
                f'{label} shortDescription must contain 1–30 characters')
    require(portable_interface == codex_interface, 'Manifest presentation drift')
    for entry in json.loads((ROOT / 'sources/manifest.json').read_text())['files']:
        path = ROOT / 'sources' / entry['path']
        require(hashlib.sha256(path.read_bytes()).hexdigest() == entry['sha256'], f'Source changed: {path}')
    return contracts()

def validate_output(path, mode, symptom_count, contract):
    text = path.read_text()
    placeholders = {token for asset in ROOT.glob('skills/*/assets/*.md')
                    for token in re.findall(r'\[[^\]\n]+\]', asset.read_text())}
    require(not any(token in text for token in placeholders),
            'Output contains unfilled template authoring placeholders')
    tables = parse_tables(text)
    keys = [key for key, _, _ in tables]
    wanted = MODES[mode]
    require(set(keys) == set(wanted), f'{mode}: expected {wanted}, found {keys}')
    for key, headers, rows in tables:
        expected_header, base_rows = contract[key]
        require(headers == expected_header, f'{key}: incorrect headers/order')
        names = [row[0] for row in rows]
        require(len(names) == len(set(names)) or key == 'table-2-2', f'{key}: duplicate category/item')
        if key != 'table-2-2':
            require(names[:len(base_rows)] == base_rows, f'{key}: base rows missing/reordered')
            if key in ['table-2-1', 'table-4']:
                require(names == base_rows, f'{key}: fixed item rows changed')
        require(rows, f'{key}: empty table')
        if key in ['table-3-1', 'table-3-2']:
            labels = ('★★★ Strong', '★★ Moderate', '★ Low', '− Currently not supported',
                      '✕ Ruled-out', '⚠ Conflicting evidence', '? Unable to determine / Pending assessment')
            require(all(row[-1].startswith(labels) for row in rows), f'{key}: unapproved status label')
    require([wanted.index(k) for k in keys] == sorted(wanted.index(k) for k in keys), 'Table groups out of order')
    for key in wanted:
        expected_count = symptom_count if key in ['table-1-1', 'table-1-2'] else 1
        require(keys.count(key) == expected_count, f'{key}: wrong repetition count')
    for heading in ['Red Flags', 'Yellow Flags', 'Reasoning Rationale and Limitations']:
        require(re.search(r'^#+ '+re.escape(heading)+r'\s*$', text, re.M), f'Missing {heading} section')
    if mode in ['complete', 'impression']:
        for label in ['Prognosis:', 'Red flags:']:
            require(label in text, f'Full Impression missing {label}')
    return len(tables)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--mode', choices=MODES, default='complete')
    parser.add_argument('--symptoms', type=int, default=1)
    args = parser.parse_args()
    require(args.symptoms > 0, 'Symptom count must be positive for table-output validation')
    contract = validate_package()
    if args.output:
        count = validate_output(args.output, args.mode, args.symptoms, contract)
        print(f'PASS: package integrity and {count} fixed tables in {args.output}')
    else:
        print('PASS: three skills, seven templates, shared/local resource links, manifests and source hashes')
    print('Limit: this validates structure and provenance, not clinical correctness, skill discovery or model behavior.')

if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, OSError) as error:
        raise SystemExit(f'FAIL: {error}')
