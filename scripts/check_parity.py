"""Check the skill library for language parity and naming rules.

Run from the repository root:

    python scripts/check_parity.py

Checks performed:
1. ko/ and en/ contain the same skill folders.
2. Every SKILL.md has YAML frontmatter whose `name` equals its folder name and
   whose `description` is non-empty and at most 1024 characters.
3. Every skill folder has a manifest.txt that lists exactly the files present
   (excluding manifest.txt itself).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = ['ko', 'en']
NAME_RE = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')


def frontmatter(text: str) -> dict:
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        return {}
    data = {}
    for line in m.group(1).splitlines():
        if ':' in line:
            key, value = line.split(':', 1)
            data[key.strip()] = value.strip()
    return data


def main() -> int:
    errors = []
    listing = {lang: sorted(p.name for p in (ROOT / lang).iterdir() if p.is_dir()) for lang in LANGS}
    if listing['ko'] != listing['en']:
        errors.append(f'skill folders differ: ko={listing["ko"]} en={listing["en"]}')
    for lang in LANGS:
        for skill_dir in sorted((ROOT / lang).iterdir()):
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / 'SKILL.md'
            if not skill_md.exists():
                errors.append(f'{lang}/{skill_dir.name}: SKILL.md missing')
                continue
            fm = frontmatter(skill_md.read_text(encoding='utf-8'))
            if fm.get('name') != skill_dir.name:
                errors.append(f'{lang}/{skill_dir.name}: name {fm.get("name")!r} != folder name')
            if not NAME_RE.match(skill_dir.name) or len(skill_dir.name) > 64:
                errors.append(f'{lang}/{skill_dir.name}: invalid folder name')
            desc = fm.get('description', '')
            if not desc or len(desc) > 1024:
                errors.append(f'{lang}/{skill_dir.name}: description empty or longer than 1024 characters')
            manifest = skill_dir / 'manifest.txt'
            actual = sorted(str(p.relative_to(skill_dir)) for p in skill_dir.rglob('*') if p.is_file() and p.name != 'manifest.txt')
            if not manifest.exists():
                errors.append(f'{lang}/{skill_dir.name}: manifest.txt missing')
            elif sorted(manifest.read_text(encoding='utf-8').split()) != actual:
                errors.append(f'{lang}/{skill_dir.name}: manifest.txt does not match files {actual}')
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'OK: {len(listing["ko"])} skills, ko and en in sync')
    return 0


if __name__ == '__main__':
    sys.exit(main())
