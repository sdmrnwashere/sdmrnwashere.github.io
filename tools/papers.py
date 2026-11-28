# Generates one page per paper at research/<slug>/index.html (abstract, figure, BibTeX,
# Google Scholar citation_* tags, JSON-LD). Data: academic/build.py (paper list) +
# tools/abstracts.json (abstracts extracted from the PDFs).
# Run from the repo root:  python -I tools/papers.py   (then python -I tools/seo.py)
import html, json, os, re, unicodedata

BASE = 'https://sdmrnwashere.github.io/'
E = html.escape


def slugify(t, limit=72):
    s = ''.join(c for c in unicodedata.normalize('NFKD', t) if not unicodedata.combining(c)).lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    if len(s) > limit:
        s = s[:limit].rsplit('-', 1)[0]
    return s


def load():
    src = open('academic/build.py', encoding='utf-8').read()
    ns = {}
    exec(src[:src.index('\ndef thumb')], ns)  # pubs, IMG
    return ns['pubs'], ns['IMG']


PUBS, IMG = load()
ABS = json.load(open('tools/abstracts.json', encoding='utf-8'))
MOD = {'eeg': 'EEG', 'ecg': 'ECG', 'imu': 'IMU', 'radar': 'Radar', 'audio': 'Audio', 'circuits': 'Circuits', 'control': 'Control', 'vision': 'Vision'}


def fig_key(p):
    for prefix, key in IMG.items():
        if p['t'].startswith(prefix):
            return key
    return None


def is_journal(p):
    return not p['v'].startswith('IEEE ') or 'Journal' in p['v'] or 'Letters' in p['v']


def names(p):
    return [n.replace('*', '').strip() for n in p['a'].split(', ')]


def bibtex(p, key):
    first = names(p)[0].split()[-1].lower()
    word = re.sub(r'[^a-z]', '', p['t'].split()[0].lower()) or 'paper'
    kind = 'article' if is_journal(p) else 'inproceedings'
    venue_field = 'journal' if is_journal(p) else 'booktitle'
    venue = p['v'] if is_journal(p) else 'Proceedings of ' + p['v']
    lines = [f'@{kind}{{{first}{p["y"]}{word},',
             f'  title     = {{{p["t"]}}},',
             f'  author    = {{{" and ".join(names(p))}}},',
             f'  {venue_field:<9} = {{{venue}}},',
             f'  year      = {{{p["y"]}}},']
    if p.get('url'):
        lines.append(f'  url       = {{{p["url"]}}},')
    lines[-1] = lines[-1].rstrip(',')
    return '\n'.join(lines) + '\n}'


def page(p, idx):
    slug = slugify(p['t'])
    url = f'{BASE}research/{slug}/'
    abstract = ABS.get(fig_key(p) or '', '') or p['d']
    desc = abstract[:157].rsplit(' ', 1)[0] + '…' if len(abstract) > 160 else abstract
    key = fig_key(p)
    fig = f'../../academic/images/papers/{key}.jpg' if key else f'../../academic/images/{p["k"]}.svg'
    fig_abs = f'{BASE}academic/images/papers/{key}.jpg' if key else f'{BASE}assets/og-card.jpg'
    authors_html = ', '.join(
        f'<a class="me" href="../../">{E(n)}</a>' if n.startswith('Sadman Rahman') else E(n) for n in p['a'].split(', '))
    cite = [f'<meta name="citation_title" content="{E(p["t"])}">']
    cite += [f'<meta name="citation_author" content="{E(n)}">' for n in names(p)]
    cite.append(f'<meta name="citation_publication_date" content="{p["y"]}">')
    cite.append(f'<meta name="citation_{"journal" if is_journal(p) else "conference"}_title" content="{E(p["v"])}">')
    cite.append(f'<meta name="citation_abstract_html_url" content="{url}">')
    cite.append('<meta name="citation_language" content="en">')
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'ScholarlyArticle', '@id': url + '#article', 'headline': p['t'][:110], 'name': p['t'], 'abstract': abstract,
         'datePublished': str(p['y']), 'url': url, 'image': fig_abs, 'inLanguage': 'en',
         'author': [{'@id': BASE + '#person'} if n.startswith('Sadman Rahman') else {'@type': 'Person', 'name': n} for n in names(p)],
         'isPartOf': {'@type': 'Periodical', 'name': p['v']} if is_journal(p) else {'@type': 'CreativeWork', 'name': 'Proceedings of ' + p['v']},
         **({'sameAs': p['url']} if p.get('url') else {}),
         **({'award': p['award']} if p.get('award') else {}),
         'keywords': MOD.get(p['k'], '') + ', signal processing, deep learning, machine learning'},
        {'@type': 'Person', '@id': BASE + '#person', 'name': 'Sadman Rahman', 'url': BASE},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Sadman Rahman', 'item': BASE},
            {'@type': 'ListItem', 'position': 2, 'name': 'Research', 'item': BASE + 'publications/'},
            {'@type': 'ListItem', 'position': 3, 'name': p['t'], 'item': url}]}]}
    status = p.get('note', '').strip('()') or 'published'
    related = [q for q in PUBS if q is not p and q['k'] == p['k']][:3] or [q for q in PUBS if q is not p][:3]
    rel_html = ''.join(f'<li><a href="../{slugify(q["t"])}/">{E(q["t"])}</a><span class="mono">{E(q["v"])} · {q["y"]}</span></li>' for q in related)
    links = (f'<a class="btn solid" href="{p["url"]}" target="_blank" rel="noopener">Read the paper ↗</a>' if p.get('url')
             else '<span class="btn" aria-disabled="true">Link coming soon</span>')
    return slug, f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(p["t"])} | Sadman Rahman</title>
<meta name="description" content="{E(desc)}">
{chr(10).join(cite)}
<link rel="canonical" href="{url}">
<meta name="author" content="Sadman Rahman">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Sadman Rahman">
<meta property="og:title" content="{E(p["t"])}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{fig_abs}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{E(p["t"])}">
<meta name="twitter:description" content="{E(desc)}">
<meta name="twitter:image" content="{fig_abs}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False, separators=(',', ':'))}</script>
<link rel="icon" href="../../assets/favicon.svg?v=2">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../assets/site.css?v=__CSSV__">
<script>try {{ const t = localStorage.getItem('theme'); if (t) document.documentElement.dataset.theme = t; }} catch (e) {{}}</script>
</head>
<body>
<main class="wrap paper-page">
  <nav class="crumbs mono" aria-label="Breadcrumb"><a href="../../">Sadman Rahman</a> / <a href="../../publications/">Research</a> / <span>{MOD.get(p["k"], "Paper")}</span></nav>
  <header class="pp-head">
    <span class="mono">{"Journal article" if is_journal(p) else "Conference paper"} · {E(p["v"])} · {p["y"]}</span>
    <h1>{E(p["t"])}</h1>
    <p class="pp-authors">{authors_html}</p>
    <div class="pp-meta"><span class="pill">{E(status)}</span>{f'<span class="pill q1">{E(p["v"])}</span>'}{f'<span class="pill win">★ {E(p["award"])}</span>' if p.get("award") else ""}</div>
    <div class="cta">{links}<a class="btn" href="../../publications/">All research</a></div>
  </header>
  <figure class="pp-fig"><img src="{fig}" alt="Figure from “{E(p["t"])}” by Sadman Rahman et al." width="320" height="320"><figcaption class="mono">Figure from the paper</figcaption></figure>
  <section class="pp-sec"><h2>Abstract</h2><p>{E(abstract)}</p></section>
  <section class="pp-sec"><h2>In one line</h2><p>{E(p["d"])}</p></section>
  <section class="pp-sec"><h2>Cite</h2><pre class="bib" id="bib">{E(bibtex(p, slug))}</pre>
    <button class="btn" type="button" onclick="navigator.clipboard.writeText(document.getElementById('bib').textContent).then(()=>{{this.textContent='Copied ✓'}})">Copy BibTeX</button></section>
  <section class="pp-sec"><h2>Related papers</h2><ul class="pp-rel">{rel_html}</ul></section>
  {"<p class='note'>* Equal contribution / co-first authorship.</p>" if "*" in p["a"] else ""}
</main>
<script src="../../assets/site.js?v=__JSV__" data-root="../../" data-page="publications"></script>
</body>
</html>
'''


def main():
    css_v = re.search(r'site\.css\?v=(\d+)', open('index.html', encoding='utf-8').read()).group(1)
    js_v = re.search(r'site\.js\?v=(\d+)', open('index.html', encoding='utf-8').read()).group(1)
    os.makedirs('research', exist_ok=True)
    slugs = []
    for i, p in enumerate(PUBS):
        slug, doc = page(p, i)
        os.makedirs(f'research/{slug}', exist_ok=True)
        open(f'research/{slug}/index.html', 'w', encoding='utf-8').write(doc.replace('__CSSV__', css_v).replace('__JSV__', js_v))
        slugs.append(slug)
    json.dump(slugs, open('tools/paper_slugs.json', 'w'), indent=1)
    print(len(slugs), 'paper pages written')


if __name__ == '__main__':
    main()
