"""Builds academic/index.html from the data below.
Base: Jon Barron's template (stylesheet.css); layout ideas from Zhexin Liang, Rui Li and Ziqi Huang (layout.css).
Run from the repo root: python -I academic/build.py"""
import html

E = html.escape
ME = 'Sadman Rahman'

pubs = [
    dict(k='eeg', t='MODWT-MRA-Based Activity-Aware Epilepsy Discrimination Using Single-Channel Wearable EEG During Activities of Daily Living',
         a='Md. Mehedi Hasan Bhuiyan, Sadman Rahman, Mahdia Binte Maksud, Tahiya Iffat Majumder, Kazi Newaj Faisal', v='Results in Engineering', y=2026,
         d='Tells epileptic and healthy subjects apart during everyday activities, using MODWT multiresolution features from a single wearable EEG channel.'),
    dict(k='eeg', t='Single-Channel Wearable EEG for ADL Recognition in Healthy and Epileptic Cohorts Using MODWT-MRA and Machine Learning',
         a='Mahdia Binte Maksud, Sadman Rahman, Md. Mehedi Hasan Bhuiyan, Tahiya Iffat Majumder, Kazi Newaj Faisal', v='Biomedical Signal Processing and Control', y=2026, note='(accepted)',
         url='https://www.sciencedirect.com/science/article/pii/S1746809426021580', hl=True,
         d='Recognises activities of daily living in both healthy and epileptic cohorts from one wearable EEG channel, with MODWT-MRA features and lightweight classifiers.'),
    dict(k='ecg', t='Short-Term SVMD-Enhanced High-Resolution Time–Frequency Representation for ECG Signal Analysis',
         a='Sadman Rahman, Kazi Newaj Faisal', v='IEEE SPMB', y=2026, note='(accepted)',
         d='A short-term, SVMD-based time–frequency representation that gives sharper views of ECG signals.'),
    dict(k='imu', t='Stacking Multi-Variate Time–Frequency Information: A Deep Learning Approach for IMU–MMG Based Hand Gesture Recognition',
         a='Sadman Rahman, Md. Mehedi Hasan Bhuiyan, Nasiruddin Mahmud Himel, Rishi Raj Sharma, Kazi Newaj Faisal', v='IEEE Sensors Journal', y=2026,
         url='https://ieeexplore.ieee.org/abstract/document/11508135', hl=True,
         d='Stacks multivariate time–frequency maps from IMU and MMG sensors so a deep network can recognise hand gestures.'),
    dict(k='eeg', t='HatSeqNet: A Sequence-Based Deep Learning Model for Cross-Subject Driver Drowsiness Detection Using Single-Channel EEG Signal',
         a='Sadman Rahman, Saquib Farhan, Rishi Raj Sharma, Kazi Newaj Faisal', v='IEEE Sensors Journal', y=2026,
         url='https://ieeexplore.ieee.org/document/11459382', hl=True,
         d='A sequence model that detects driver drowsiness in unseen subjects from a single EEG channel.'),
    dict(k='radar', t='Radar-Based Sleep Posture Transition Sensing: An Efficient Deep Learning Hierarchical Temporal Architecture Utilizing Depthwise Convolution',
         a='Sadman Rahman, Rishi Raj Sharma, Kazi Newaj Faisal', v='IEEE Sensors Letters', y=2026,
         url='https://ieeexplore.ieee.org/document/11594419/', hl=True,
         d='A lightweight hierarchical temporal network with depthwise convolutions that detects sleep posture transitions from radar.'),
    dict(k='circuits', t='A Comparative Logic-Style Framework for 8-Bit 12-Function Efficient ALU Design Using Transmission Gate and NMOS Pass Transistor Logic in 90-nm CMOS',
         a='Saquib Farhan, Sadman Rahman, Sanjida Sultana, Md. Tawfiq Amin, Gourab Datta', v='Analog Integrated Circuits and Signal Processing', y=2026,
         url='https://link.springer.com/article/10.1007/s10470-026-02664-5',
         d='Compares transmission-gate and NMOS pass-transistor logic styles for an efficient 8-bit, 12-function ALU in 90 nm CMOS.'),
    dict(k='imu', t='FormSense: A Continuous Fatigue and Form Tracking Application for Resistance Workout Monitoring Utilizing Phase-Graded IMU Analysis',
         a='Abdullah Al Mahi*, Munawar Arif Nitol*, Md. Mehedi Hasan Bhuiyan*, Sadman Rahman, Kazi Newaj Faisal', v='IEEE iCACCESS', y=2026, note='(accepted)',
         d='An application that tracks fatigue and exercise form during resistance workouts using phase-graded IMU analysis.'),
    dict(k='audio', t='VoxScope: A Deployment-Oriented Analysis Framework for Extreme Vocal Distortion Techniques in Heavy Metal',
         a='Md. Mehedi Hasan Bhuiyan, Fahmid Amin Zawad, Sadman Rahman, Kazi Newaj Faisal', v='IEEE SPICSCON', y=2026, note='(accepted)',
         d='A deployment-oriented framework for analysing extreme vocal distortion techniques used in heavy metal singing.'),
    dict(k='eeg', t='Exploring Gamma-Band Filtered Features and Machine Learning for Resource-Efficient Multi-Level Cognitive Load Classification Using EEG',
         a='Nur Md. Atiquzzaman Rasel, Sadman Rahman*, Kazi Newaj Faisal', v='IEEE QPAIN', y=2026, award='Best Presenter Award',
         url='https://ieeexplore.ieee.org/abstract/document/11545759',
         d='Gamma-band EEG features with resource-efficient machine learning classify multiple levels of cognitive load.'),
    dict(k='radar', t='Improved FMCW Radar Sensing for HAR Systems: Synchroextracting Transform-Enhanced Time–Frequency Representation and Custom Anisotropic CNN',
         a='Arnob Ghosh, Sadman Rahman*, Labib Siddique Siam, Kazi Newaj Faisal', v='IEEE Sensors Letters', y=2025,
         url='https://ieeexplore.ieee.org/document/11419777',
         d='Synchroextracting-transform time–frequency maps and a custom anisotropic CNN improve human activity recognition with FMCW radar.'),
    dict(k='audio', t='Leveraging Power-Spectrum-Based Features and Machine Learning for Resource-Efficient Cough Classification in Respiratory Disease Monitoring',
         a='Sadman Rahman, Irtiza Mohtasim, Saquib Farhan, Kazi Newaj Faisal', v='IEEE SPICSCON', y=2025, award='Best Paper Award',
         url='https://ieeexplore.ieee.org/document/11504221', hl=True,
         d='Power-spectrum features and lightweight machine learning classify coughs for respiratory disease monitoring.'),
    dict(k='control', t='Neural Network Enhanced PID Control of Automatic Voltage Regulators: A Comparative Study with Classical and Regression Approaches',
         a='Sadman Rahman, Saquib Farhan, Saiba Aabira, Sunjida Sultana', v='IEEE PEEIACON', y=2025,
         url='https://www.researchgate.net/publication/403049814', lname='ResearchGate',
         d='Compares neural-network-enhanced PID control of automatic voltage regulators with classical and regression-based tuning.'),
    dict(k='vision', t='GCAF-Net: An Attention-Enhanced Deep CNN Framework with Grad-CAM for Classifying Rare and Endangered Medicinal Plants in Bangladesh',
         a='Sadman Rahman*, Saquib Farhan*, Saiba Aabira, Kazi Newaj Faisal', v='IEEE QPAIN', y=2025,
         url='https://ieeexplore.ieee.org/abstract/document/11171960',
         d='An attention-enhanced CNN with Grad-CAM explanations that classifies rare and endangered medicinal plants of Bangladesh.'),
    dict(k='circuits', t='High-Speed, Low-Power 8-Bit 12-Function ALU Using Transmission Gate Logic in 90nm Technology',
         a='Saquib Farhan*, Sadman Rahman*, Saiba Aabira, Gourab Datta, Sunjida Sultana, Md. Tawfiq Amin', v='IEEE QPAIN', y=2025,
         url='https://ieeexplore.ieee.org/document/11172017',
         d='A high-speed, low-power 8-bit, 12-function ALU built with transmission-gate logic in 90 nm technology.'),
]



SHORT = {  # short venue tags shown in bold after the venue, Rui-Li style
    'Results in Engineering': 'RINENG', 'Biomedical Signal Processing and Control': 'BSPC',
    'IEEE Sensors Journal': 'IEEE JSEN', 'IEEE Sensors Letters': 'IEEE LSENS',
    'Analog Integrated Circuits and Signal Processing': 'AICSP',
}

NEWS = [
    ('2026.11', 'Paper on activity-aware epilepsy discrimination from wearable EEG published in <b>Results in Engineering</b>.'),
    ('2026', 'Joined <a href="https://mist.ac.bd/">MIST</a> as a <b>Research Assistant</b>, working on a privacy-preserving fingerprint attendance system.'),
    ('2026', 'Wearable-EEG activity recognition in epileptic cohorts accepted in <b>Biomedical Signal Processing and Control</b> (Q1).'),
    ('2026.10', 'Started my <b>M.Sc.</b> in EEE at BUET with Dr. Shaikh Anowarul Fattah.'),
    ('2026.06', 'Graduated from MIST, ranked <b>2nd of 97</b> (CGPA 3.94/4.00).'),
    ('2026', 'Received the <span class="award">Best Presenter Award</span> at IEEE QPAIN 2026.'),
    ('2026', 'Two first-author papers published in <b>IEEE Sensors Journal</b>: HatSeqNet and IMU–MMG gesture recognition.'),
    ('2026', 'Papers accepted at <b>IEEE SPMB</b>, <b>ICACCESS</b> and <b>SPICSCON</b>.'),
    ('2025', 'Received the <span class="award">Best Paper Award</span> at IEEE SPICSCON 2025.'),
    ('2025.06', 'Became Chairperson of the IEEE MIST Student Branch and founded its Signal Processing Society chapter.'),
]

INTERESTS = ['Time–frequency signal processing', 'Efficient deep learning', 'Applied AI &amp; LLM systems',
             'Biomedical &amp; wearable sensing', 'EEG · ECG · IMU · radar · audio']

EXPERIENCE = [
    ('mist', 'MIST', 'Research Assistant', 'Military Institute of Science and Technology (MIST)', '2026 – present',
     'Developing a privacy-preserving, handheld fingerprint-based automated attendance system for MIST and higher education institutions in Bangladesh.'),
    ('insia', 'INSIA Lab', 'Co-founder', '<a href="https://www.insia-lab.com/home">INSIA Lab</a>', 'May 2024 – present',
     'Grew the lab from 3 to 49 members and delivered 15 multidisciplinary projects.'),
    ('gp', 'Grameenphone', 'Industrial Engineering Trainee', 'Grameenphone (Telenor Group)', 'May 2025 – Jun 2025',
     'Studied operational workflows across IT, network and technology functions; presented a KPI-based report.'),
]

EDUCATION = [
    ('buet', 'BUET', 'M.Sc. in Electrical and Electronic Engineering', 'Bangladesh University of Engineering and Technology', 'Oct 2026 – present',
     'Advisor: Dr. Shaikh Anowarul Fattah · Communication and Signal Processing'),
    ('mist', 'MIST', 'B.Sc. in Electrical and Electronics Engineering', 'Military Institute of Science and Technology', 'Aug 2022 – Jun 2026',
     'CGPA 3.94/4.00, ranked 2nd of 97 · Advisor: Dr. Kazi Newaj Faisal · Dean’s List all four years · '
     '<a href="https://drive.google.com/file/d/1nussQ8lhKcv6y55IxThQaBtG5Z_6y9ze/view?usp=sharing">thesis slides</a>'),
    ('milestone', 'Milestone College', 'Higher Secondary Certificate, Science', 'Milestone College, Dhaka', 'Mar 2019 – Jan 2022',
     'GPA 5.00/5.00'),
]

AWARDS = [
    ('Best Paper Award', 'IEEE SPICSCON 2025'), ('Best Presenter Award', 'IEEE QPAIN 2026'),
    ('Finalist', 'BEAR Summit &amp; National Semiconductor Symposium 2025'), ('2nd Runner-up', 'BEAR Summit Biotech Poster Showcase 2025'),
    ('2nd Runner-up', 'IEEE Photonics &amp; EDS Poster Designing Contest 2024'), ('Dean’s List &amp; Merit Scholarship', 'MIST, all four years'),
]

MISC = [
    ('#aaba9e', 'Service', [
        'Reviewer, IEEE Transactions on Affective Computing',
        'Chairperson, IEEE MIST Student Branch, 2025–2026',
        'Founding Chair, IEEE Signal Processing Society MIST SB Chapter, 2025–2026',
        'Secretary General, MIST Robotics Club, 2025–2026']),
    ('#c6b89e', 'Teaching', [
        'Instructor, Hands-on Arduino 3.0 and Pixel Pulse (150+ students)',
        'Organiser, 11+ signal processing workshops with BUET and DU',
        'Interests: Signals and Systems, DSP, Circuits, Digital Logic, Microcontrollers, Machine Learning']),
    ('#b9c9de', 'Design', [
        'Former professional graphic designer: <a href="https://www.behance.net/sadmanrahman1">portfolio on Behance</a>',
        '<a href="../">Interactive version of this site</a>']),
]

ICON = {
    'pin': '<svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>',
    'mail': '<svg viewBox="0 0 24 24"><path d="M3 5h18a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zm9 7.2L4 7.3V17h16V7.3l-8 4.9zM5.2 7l6.8 4.1L18.8 7H5.2z"/></svg>',
    'scholar': '<svg viewBox="0 0 24 24"><path d="M12 3 1 9l11 6 9-4.9V17h2V9L12 3zm-6.8 9.6v3.9L12 20l6.8-3.5v-3.9L12 16.3l-6.8-3.7z"/></svg>',
    'github': '<svg viewBox="0 0 24 24"><path d="M12 .5a11.5 11.5 0 0 0-3.6 22.4c.6.1.8-.3.8-.6v-2c-3.2.7-3.9-1.5-3.9-1.5-.5-1.3-1.3-1.7-1.3-1.7-1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.7-1.6-2.6-.3-5.3-1.3-5.3-5.7 0-1.3.5-2.3 1.2-3.1-.1-.3-.5-1.5.1-3.1 0 0 1-.3 3.2 1.2a11 11 0 0 1 5.8 0c2.2-1.5 3.2-1.2 3.2-1.2.6 1.6.2 2.8.1 3.1.8.8 1.2 1.9 1.2 3.1 0 4.4-2.7 5.4-5.3 5.7.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A11.5 11.5 0 0 0 12 .5z"/></svg>',
    'linkedin': '<svg viewBox="0 0 24 24"><path d="M20.4 2H3.6C2.7 2 2 2.7 2 3.6v16.8c0 .9.7 1.6 1.6 1.6h16.8c.9 0 1.6-.7 1.6-1.6V3.6c0-.9-.7-1.6-1.6-1.6zM8 19H5V9.5h3V19zM6.5 8.2a1.7 1.7 0 1 1 0-3.5 1.7 1.7 0 0 1 0 3.5zM19 19h-3v-4.6c0-1.1 0-2.5-1.5-2.5S12.8 13 12.8 14.3V19h-3V9.5h2.9v1.3c.4-.8 1.4-1.6 2.9-1.6 3.1 0 3.6 2 3.6 4.6V19z"/></svg>',
    'rg': '<svg viewBox="0 0 24 24"><path d="M3 2h18a1 1 0 0 1 1 1v18a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1zm6.9 6.2c-2 0-3.3 1.4-3.3 3.8v.5c0 2.4 1.3 3.8 3.3 3.8 1 0 1.8-.3 2.4-.9v-3.1H9.8v1.2h1.1v1.4c-.2.2-.6.3-1 .3-1.1 0-1.7-.9-1.7-2.6V12c0-1.7.6-2.6 1.7-2.6.8 0 1.2.4 1.3 1.2h1.5c-.2-1.5-1.2-2.4-2.8-2.4zm7.3-2.4c-1.3 0-2.1.8-2.1 2.1v.4h1.2v-.4c0-.6.3-1 .9-1s.9.3.9 1-.3 1-1.1 1.7l-1.8 1.6V12h4.2v-1.1h-2.4l1-.9c1.1-.9 1.6-1.6 1.6-2.5 0-1.1-.9-1.7-2.4-1.7z"/></svg>',
    'cv': '<svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6zm-1 7V3.5L18.5 9H13zM8 13h8v1.5H8V13zm0 3h6v1.5H8V16z"/></svg>',
}

SIDE_LINKS = [
    ('pin', 'Dhaka, Bangladesh', None),
    ('mail', 'Email', 'mailto:sdmrnwashere@gmail.com'),
    ('scholar', 'Google Scholar', 'https://scholar.google.com/citations?user=nHt79bkAAAAJ&amp;hl=en'),
    ('github', 'GitHub', 'https://github.com/sdmrnwashere'),
    ('linkedin', 'LinkedIn', 'https://www.linkedin.com/in/sadman-rahman-2412b0339/'),
    ('rg', 'ResearchGate', 'https://www.researchgate.net/profile/Sadman-Rahman-5'),
    ('cv', 'CV (PDF)', '../assets/Sadman_Rahman_CV.pdf'),
]

SECTIONS = [('about', 'About Me'), ('news', 'News'), ('publications', 'Publications'), ('experience', 'Experience'),
            ('education', 'Education'), ('awards', 'Awards'), ('misc', 'Service &amp; More')]


IMG = {  # title prefix -> figure thumbnail in images/papers/ (main + _b hover), taken from the paper PDFs
    'MODWT-MRA-Based Activity-Aware': 'rie',
    'Single-Channel Wearable EEG for ADL': 'bspc',
    'Short-Term SVMD': 'svmd',
    'Stacking Multi-Variate': 'imummg',
    'HatSeqNet': 'hatseq',
    'Radar-Based Sleep Posture': 'sleep',
    'A Comparative Logic-Style': 'alu_j',
    'Exploring Gamma-Band': 'gamma',
    'Improved FMCW Radar': 'sethar',
    'Leveraging Power-Spectrum': 'cough',
    'Neural Network Enhanced PID': 'pid',
    'GCAF-Net': 'gcaf',
    'High-Speed, Low-Power 8-Bit': 'alu_c',
    'VoxScope': 'vox',
    'FormSense': 'form',
}


def slugify(t, limit=72):  # same rule as tools/papers.py
    import re as _re, unicodedata as _ud
    s = ''.join(c for c in _ud.normalize('NFKD', t) if not _ud.combining(c)).lower()
    s = _re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s[:limit].rsplit('-', 1)[0] if len(s) > limit else s


def thumb(p):
    for prefix, key in IMG.items():
        if p['t'].startswith(prefix):
            return f'images/papers/{key}.jpg', f'images/papers/{key}_b.jpg'
    return f"images/{p['k']}.svg", f"images/{p['k']}_tf.svg"


def authors(a):
    return ', '.join(f'<strong>{E(n)}</strong>' if n.startswith(ME) else f'<span class="author">{E(n)}</span>'
                     for n in a.split(', '))


def article(p):
    url = p.get('url')
    page = f'../research/{slugify(p["t"])}/'
    title = f'<a href="{page}" class="papertitle">{E(p["t"])}</a>'
    tag = SHORT.get(p['v'], p['v'].replace('IEEE ', ''))
    venue = f'<em>{E(p["v"])}</em> (<b>{E(tag)}</b>), {p["y"]}'
    if p.get('note'):
        venue += f' {p["note"]}'
    if p.get('award'):
        venue += f' &nbsp;<strong class="award">{p["award"]}</strong>'
    pills = f'<a class="pill" href="{page}">Abstract</a>' + (f'<a class="pill" href="{url}">{p.get("lname", "Paper")}</a>' if url else '')
    t1, t2 = thumb(p)
    return f'''      <article class="paper{' highlighted' if p.get('hl') else ''}">
        <div class="paper-media">
          <div class="one">
            <div class="two"><img src="{t2}" alt="" width="160" height="160" loading="lazy"></div>
            <img src="{t1}" alt="Figure from: {E(p['t'][:60])}" width="160" height="160" loading="lazy">
          </div>
        </div>
        <div class="paper-info">
          {title}
          <div class="paper-authors">{authors(p["a"])}</div>
          <div class="paper-venue">{venue}</div>
          <div class="pills">{pills}</div>
          <p class="paper-desc"><b class="tldr">TL;DR:</b> {E(p["d"])}</p>
        </div>
      </article>'''


def entry(logo, alt, title, where, when, desc):
    return f'''        <div class="entry">
          <div class="logo"><img src="images/logos/{logo}.png" alt="{alt} logo" loading="lazy"></div>
          <div><div class="entry-head"><b>{title}</b> | {where}<span class="when">{when}</span></div>
          <div class="entry-desc">{desc}</div></div>
        </div>'''


def misc_row(color, title, items):
    rows = '\n'.join(f'            <div>{i}</div>' for i in items)
    return f'''      <div class="misc-row">
        <div class="misc-badge"><div class="colored-box" style="background-color: {color};"><h2>{title}</h2></div></div>
        <div class="misc-links">
{rows}
        </div>
      </div>'''


def side_item(i, t, u):
    label = f'<a href="{u}">{t}</a>' if u else f'<span>{t}</span>'
    return f'          <li>{ICON[i]}{label}</li>'


sidebar = '\n'.join(side_item(*s) for s in SIDE_LINKS)
quick = '\n'.join(f'            <a href="#{k}">{t}</a>' for k, t in SECTIONS)
news = '\n'.join(f'          <li><span class="date">{d}</span><span>{t}</span></li>' for d, t in NEWS)
interests = '\n'.join(f'            <li>{i}</li>' for i in INTERESTS)
awards = '\n'.join(f'          <li><b>{a}</b>, {w}</li>' for a, w in AWARDS)

PAGE = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Sadman Rahman</title>
    <meta name="author" content="Sadman Rahman">
    <meta name="description" content="Sadman Rahman: M.Sc. student in EEE at BUET working on signal processing, deep learning and applied AI for biomedical and wearable sensing.">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="color-scheme" content="light">
    <link rel="icon" href="../assets/favicon.svg?v=2">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" type="text/css" href="stylesheet.css">
    <link rel="stylesheet" type="text/css" href="layout.css?v=5">
  </head>

  <body>
    <header class="topbar">
      <a class="brand" href="#about">Sadman Rahman</a>
      <nav>__TOPNAV__</nav>
    </header>

    <div class="layout">
      <aside class="sidebar">
        <img class="avatar" src="images/sadman.jpg" alt="Sadman Rahman" width="405" height="405">
        <h1 class="side-name">Sadman Rahman</h1>
        <p class="side-role">M.Sc. Student @ BUET<br>Research Assistant @ MIST</p>
        <ul class="side-links">
__SIDEBAR__
        </ul>
        <nav class="quick" aria-label="Quick links">
          <span>Quick links</span>
__QUICK__
        </nav>
      </aside>

      <main class="main">
        <section id="about" class="block">
          <h2>About Me</h2>
          <div class="about">
            <div class="about-text">
              <p>I'm an M.Sc. student in Electrical and Electronic Engineering at <a href="https://www.buet.ac.bd/">Bangladesh University of Engineering and Technology (BUET)</a>, advised by Dr. Shaikh Anowarul Fattah, and a Research Assistant at <a href="https://mist.ac.bd/">MIST</a>, where I'm developing a privacy-preserving, fingerprint-based attendance system for universities in Bangladesh.</p>
              <p>I did my B.Sc. in EEE at the <a href="https://mist.ac.bd/">Military Institute of Science and Technology (MIST)</a> with Dr. Kazi Newaj Faisal, graduating 2nd of 97. My research builds sharper time–frequency representations of non-stationary signals and compact neural networks that learn from them, for biomedical and wearable sensing. I co-founded <a href="https://www.insia-lab.com/home">INSIA Lab</a>.</p>
            </div>
            <div class="interests">
              <h3>Research Interests</h3>
              <ul>
__INTERESTS__
              </ul>
            </div>
          </div>
          <p class="cta">I'm looking for Ph.D. positions in signal processing and AI. If you think we'd be a good fit, feel free to <a href="mailto:sdmrnwashere@gmail.com">email me</a>.</p>
        </section>

        <section id="news" class="block">
          <h2>News</h2>
          <ul class="news">
__NEWS__
          </ul>
        </section>

        <section id="publications" class="block">
          <h2>Publications <a class="h2-link" href="https://scholar.google.com/citations?user=nHt79bkAAAAJ&amp;hl=en">[Google Scholar]</a></h2>
          <p class="note">15 papers: 7 journal articles and 8 IEEE conference papers. Representative papers are <span class="highlight">highlighted</span>; * denotes equal contribution. Hover a thumbnail to see a second figure from the paper.</p>
          <div class="papers">
__PAPERS__
          </div>
        </section>

        <section id="experience" class="block">
          <h2>Experience</h2>
__EXPERIENCE__
        </section>

        <section id="education" class="block">
          <h2>Education</h2>
__EDUCATION__
        </section>

        <section id="awards" class="block">
          <h2>Awards</h2>
          <ul class="awards">
__AWARDS__
          </ul>
        </section>

        <section id="misc" class="block">
          <h2>Service &amp; More</h2>
          <div class="misc">
__MISC__
          </div>
        </section>

        <footer class="site-footer">
          <p>Website template from <a href="https://github.com/jonbarron/jonbarron.github.io">Jon Barron's source code</a>. Thanks, Jon!<br>
          Layout ideas from <a href="https://zhexinliang.github.io/">Zhexin Liang</a>, <a href="https://ruili3.github.io/">Rui Li</a> and <a href="https://ziqihuangg.github.io/">Ziqi Huang</a>.</p>
        </footer>
      </main>
    </div>

    <script>
      // Quick links: highlight the section in view.
      var links = document.querySelectorAll('.quick a, .topbar nav a');
      var spy = new IntersectionObserver(function(entries) {
        entries.forEach(function(e) {
          if (!e.isIntersecting) return;
          links.forEach(function(l) { l.classList.toggle('active', l.getAttribute('href') === '#' + e.target.id); });
        });
      }, {rootMargin: '-35% 0px -60% 0px'});
      document.querySelectorAll('section.block').forEach(function(s) { spy.observe(s); });

      // Tap a thumbnail on touch screens to see its time-frequency view (adapted from the template).
      document.querySelectorAll('.paper').forEach(function(card) {
        var thumb = card.querySelector('.one');
        if (!thumb) return;
        var moved = false;
        thumb.addEventListener('touchstart', function() { moved = false; }, {passive: true});
        thumb.addEventListener('touchmove', function() { moved = true; }, {passive: true});
        thumb.addEventListener('touchend', function() {
          if (moved) return;
          var active = !card.classList.contains('hover-active');
          document.querySelectorAll('.paper.hover-active').forEach(function(o) { o.classList.remove('hover-active'); });
          if (active) card.classList.add('hover-active');
        }, {passive: true});
      });
    </script>
  </body>
</html>
'''

page = (PAGE
        .replace('__TOPNAV__', ''.join(f'<a href="#{k}">{t}</a>' for k, t in SECTIONS[:5]))
        .replace('__SIDEBAR__', sidebar).replace('__QUICK__', quick)
        .replace('__INTERESTS__', interests).replace('__NEWS__', news)
        .replace('__PAPERS__', '\n'.join(article(p) for p in pubs))
        .replace('__EXPERIENCE__', '\n'.join(entry(*e) for e in EXPERIENCE))
        .replace('__EDUCATION__', '\n'.join(entry(*e) for e in EDUCATION))
        .replace('__AWARDS__', awards)
        .replace('__MISC__', '\n'.join(misc_row(*m) for m in MISC)))
with open('academic/index.html', 'w', encoding='utf-8') as f:
    f.write(page)
print(len(pubs), 'papers written')
