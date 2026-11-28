# Injects SEO tags + JSON-LD into every page and writes robots.txt / sitemap.xml.
# Run from the repo root after editing content (and after academic/build.py):  python -I tools/seo.py
import json, re

BASE = 'https://sdmrnwashere.github.io/'
CARD = BASE + 'assets/og-card.jpg'
PROFILES = [
    'https://scholar.google.com/citations?user=nHt79bkAAAAJ',
    'https://github.com/sdmrnwashere',
    'https://www.linkedin.com/in/sadman-rahman-2412b0339/',
    'https://www.researchgate.net/profile/Sadman-Rahman-5',
    'https://www.behance.net/sadmanrahman1',
    'https://sites.google.com/view/sadman-rahman/about',
]
BUET = {'@type': 'CollegeOrUniversity', 'name': 'Bangladesh University of Engineering and Technology', 'alternateName': 'BUET', 'url': 'https://www.buet.ac.bd/'}
MIST = {'@type': 'CollegeOrUniversity', 'name': 'Military Institute of Science and Technology', 'alternateName': 'MIST', 'url': 'https://mist.ac.bd/'}
PERSON = {
    '@type': 'Person', '@id': BASE + '#person',
    'name': 'Sadman Rahman', 'alternateName': ['SdmrnWasHere', 'sdmrnwashere', 'S. Rahman'],
    'url': BASE, 'image': BASE + 'academic/images/sadman.jpg', 'email': 'mailto:sdmrnwashere@gmail.com',
    'jobTitle': 'M.Sc. Student and Research Assistant',
    'description': 'Researcher in signal processing and AI for biomedical and wearable sensing.',
    'affiliation': [BUET, MIST],
    'alumniOf': [MIST, {'@type': 'EducationalOrganization', 'name': 'Milestone College'}],
    'memberOf': [{'@type': 'Organization', 'name': 'INSIA Lab', 'url': 'https://www.insia-lab.com/home'},
                 {'@type': 'Organization', 'name': 'IEEE'}],
    'address': {'@type': 'PostalAddress', 'addressLocality': 'Dhaka', 'addressCountry': 'BD'},
    'nationality': {'@type': 'Country', 'name': 'Bangladesh'},
    'knowsAbout': ['Signal processing', 'Time-frequency analysis', 'Deep learning', 'Machine learning', 'Explainable AI',
                   'Responsible AI', 'Image enhancement', 'EEG', 'ECG', 'IMU', 'FMCW radar', 'Brain-computer interfaces',
                   'Wearable sensing', 'Biomedical signal processing', 'Large language models', 'Retrieval-augmented generation'],
    'award': ['Best Paper Award, IEEE SPICSCON 2025', 'Best Presenter Award, IEEE QPAIN 2026'],
    'sameAs': PROFILES,
}

PAGES = {
    'index.html': ('', 'ProfilePage',
        'Sadman Rahman: researcher in signal processing and AI from Dhaka, Bangladesh. M.Sc. student in EEE at BUET and '
        'Research Assistant at MIST, working on EEG, ECG, IMU and radar sensing with efficient deep learning. 15 peer-reviewed papers.'),
    'publications/index.html': ('publications/', 'CollectionPage',
        'Research by Sadman Rahman (BUET, MIST): time-frequency signal processing, deep learning and biomedical AI. '
        'All 15 peer-reviewed papers, including IEEE Sensors Journal, IEEE Sensors Letters and Biomedical Signal Processing and Control.'),
    'cv/index.html': ('cv/', 'ProfilePage',
        'CV of Sadman Rahman: M.Sc. EEE at BUET, B.Sc. EEE at MIST (ranked 2nd of 97), Research Assistant at MIST, '
        'co-founder of INSIA Lab, IEEE MIST Student Branch chair, awards and skills.'),
    'repositories/index.html': ('repositories/', 'CollectionPage',
        'Projects and code by Sadman Rahman: research systems for EEG, radar and IMU sensing, LLM tools, '
        'and a privacy-preserving fingerprint attendance system.'),
    'academic/index.html': ('academic/', 'ProfilePage',
        'Sadman Rahman: M.Sc. student in EEE at BUET and Research Assistant at MIST, working on signal processing, '
        'deep learning and applied AI for biomedical and wearable sensing. Publications, experience and education.'),
    'misc/index.html': ('misc/', 'AboutPage',
        'Sadman Rahman beyond research: INSIA Lab, IEEE leadership, teaching, and graphic design.'),
}


def papers():
    """Read the paper list from academic/build.py (single source for the academic page)."""
    src = open('academic/build.py', encoding='utf-8').read()
    ns = {}
    exec(src[:src.index('\nIMG =')], ns)  # defines E, ME, pubs
    return ns['pubs']


def JOURNAL(p):
    return not p['v'].startswith('IEEE ') or 'Journal' in p['v'] or 'Letters' in p['v']


def article(p):
    names = [n.replace('*', '').strip() for n in p['a'].split(', ')]
    a = {'@type': 'ScholarlyArticle', 'headline': p['t'], 'name': p['t'], 'datePublished': str(p['y']),
         'author': [{'@id': PERSON['@id']} if n.startswith('Sadman Rahman') else {'@type': 'Person', 'name': n} for n in names],
         'isPartOf': ({'@type': 'Periodical', 'name': p['v']} if JOURNAL(p) else
                      {'@type': 'CreativeWork', 'name': 'Proceedings of ' + p['v']}),
         'abstract': p['d']}
    if p.get('url'):
        a['url'] = p['url']
    return a


def block(path, ptype, desc):
    url = BASE + path
    graph = [dict(PERSON),
             {'@type': 'WebSite', '@id': BASE + '#website', 'url': BASE, 'name': 'Sadman Rahman', 'alternateName': 'SdmrnWasHere',
              'publisher': {'@id': PERSON['@id']}, 'inLanguage': 'en'},
             {'@type': ptype, '@id': url + '#page', 'url': url, 'name': 'Sadman Rahman', 'description': desc,
              'isPartOf': {'@id': BASE + '#website'}, 'about': {'@id': PERSON['@id']},
              'primaryImageOfPage': {'@type': 'ImageObject', 'url': CARD}}]
    if ptype == 'ProfilePage':
        graph[2]['mainEntity'] = {'@id': PERSON['@id']}
    if path in ('publications/', 'academic/'):
        graph[2]['mainEntity'] = {'@type': 'ItemList', 'numberOfItems': len(PUBS),
                                  'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'item': article(p)} for i, p in enumerate(PUBS)]}
    ld = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, separators=(',', ':'))
    me = '\n'.join(f'<link rel="me" href="{u}">' for u in PROFILES)
    return f'''<!-- SEO -->
<link rel="canonical" href="{url}">
<meta name="author" content="Sadman Rahman">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="{'profile' if ptype == 'ProfilePage' else 'website'}">
<meta property="og:site_name" content="Sadman Rahman">
<meta property="og:title" content="Sadman Rahman">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{CARD}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Sadman Rahman: AI that understands signals">
<meta property="profile:first_name" content="Sadman">
<meta property="profile:last_name" content="Rahman">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Sadman Rahman">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{CARD}">
{me}
<script type="application/ld+json">{ld}</script>
<!-- /SEO -->'''


PUBS = papers()
for file, (path, ptype, desc) in PAGES.items():
    s = open(file, encoding='utf-8').read()
    s = re.sub(r'\n<!-- SEO -->.*?<!-- /SEO -->', '', s, flags=re.S)          # idempotent
    s = re.sub(r'\n[ \t]*<meta (?:property|name)="(?:og|twitter):[a-z:_]+"[^>]*>', '', s)  # old partial OG/Twitter tags
    s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', s, count=1)
    s = s.replace('</head>', block(path, ptype, desc) + '\n</head>', 1)
    open(file, 'w', encoding='utf-8').write(s)
    print('seo ->', file)

urls = ['', 'publications/', 'cv/', 'repositories/', 'misc/', 'academic/']
pri = {'': '1.0', 'academic/': '0.9', 'publications/': '0.9', 'cv/': '0.8'}
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    sm.append(f'  <url><loc>{BASE}{u}</loc><lastmod>2026-11-28</lastmod><changefreq>monthly</changefreq><priority>{pri.get(u, "0.6")}</priority></url>')
sm.append('</urlset>')
open('sitemap.xml', 'w', encoding='utf-8').write('\n'.join(sm) + '\n')
open('robots.txt', 'w', encoding='utf-8').write(f'User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n')
print('sitemap.xml + robots.txt written,', len(PUBS), 'papers in structured data')
