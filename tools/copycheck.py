#!/usr/bin/env python3
"""List every user-facing string in index.html and flag wording that reads as AI-written.
Run after any substantive content change:  python3 tools/copycheck.py [index.html]
Exit code 1 when anything is flagged. Review all output by eye as well; the patterns below are a floor."""
import re, sys
p = sys.argv[1] if len(sys.argv) > 1 else 'index.html'
s = open(p, encoding='utf-8').read()
s = re.sub(r'data:[a-z/+-]+;base64,[A-Za-z0-9+/=]+', '', s)
body = s[s.index('<body'):] if '<body' in s else s
strings = set()
for m in re.finditer(r"'((?:[^'\\\n]|\\.){12,})'|\"((?:[^\"\\\n]|\\.){12,})\"", body):
    t = (m.group(1) or m.group(2)).replace("\\'", "'")
    t = re.sub(r'<[^>]+>', ' ', t).strip()
    if re.search(r'[A-Za-z]{3,} [A-Za-z]{2,}', t) and not re.search(r'function|document\.|=>|\bvar\b|[{};]\s*$', t):
        strings.add(t)
for m in re.finditer(r'>([^<>{}]{12,})<', body):
    t = m.group(1).strip()
    if re.search(r'[A-Za-z]{3,} [A-Za-z]{2,}', t): strings.add(t)
RULES = [
 (r'^(?!.*(Creature|Planeswalker|Emblem|Fathomless descent|Choose one)).*[—–]', 'dash used as punctuation (card type lines exempt)'),
 (r'^(?!Delve \().*\b(journey|adventure|embark|unlock|unleash|master the|dive into|delve|realm|tapestry|magical|epic|ultimate|seamless|elevate|craft(ed)?|dance|whisper|symphony)\b', 'stock AI/marketing word'),
 (r'\bnot (just|only|merely)\b|\bnot [a-z ]{2,20}, but\b|\bless about\b|\bmore than just\b', 'contrastive negation'),
 (r'^(The |Our )?(catch|tradeoff|upshot|bottom line|key|real question|truth)\s*:', 'label-colon opener'),
 (r'\b(honestly|candidly|to be fair|genuinely|truly|simply put|let\'s)\b', 'filler or self-crediting modifier'),
 (r'[a-z]+, [a-z]+,? and [a-z]+\.$', 'tricolon tagline (check by eye)'),
 (r'!\s*$', 'exclamation (check tone)'),
]
bad = 0
for t in sorted(strings):
    for rx, why in RULES:
        if re.search(rx, t, re.I):
            print(f'[{why}] {t[:140]}'); bad += 1; break
print(f'{len(strings)} strings scanned, {bad} flagged')
sys.exit(1 if bad else 0)
