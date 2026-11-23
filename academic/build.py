"""Builds academic/index.html (Jon Barron template layout) from the paper list below.
Run from the repo root: python -I <this file>"""
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
         a='Abdullah Al Mahi, Munawar Arif Nitol, Md Mehedi Hasan Bhuiyan, Sadman Rahman, Kazi Newaj Faisal', v='IEEE ICACCESS', y=2026, note='(accepted)',
         d='An application that tracks fatigue and exercise form during resistance workouts using phase-graded IMU analysis.'),
    dict(k='audio', t='VoxScope: A Deployment-Oriented Analysis Framework for Extreme Vocal Distortion Techniques in Heavy Metal',
         a='Sadman Rahman, Kazi Newaj Faisal', v='IEEE SPICSCON', y=2026, note='(accepted)',
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


def authors(a):
    return ', '.join(f'<strong>{E(n)}</strong>' if n.startswith(ME) else f'<span class="author">{E(n)}</span>'
                     for n in a.split(', '))


def article(p):
    url = p.get('url')
    title = f'<a href="{url}" class="papertitle">{E(p["t"])}</a>' if url else f'<span class="papertitle">{E(p["t"])}</span>'
    venue = f'<em>{E(p["v"])}</em>, {p["y"]}'
    if p.get('note'):
        venue += f' {p["note"]}'
    if p.get('award'):
        venue += f' &nbsp;<strong class="award">({p["award"]})</strong>'
    links = f'\n          <div class="paper-links"><a href="{url}">{p.get("lname", "paper")}</a></div>' if url else ''
    k = p['k']
    return f'''      <article class="paper{' highlighted' if p.get('hl') else ''}">
        <div class="paper-media">
          <div class="one">
            <div class="two"><img src="images/{k}_tf.svg" alt="" width="160" height="160"></div>
            <img src="images/{k}.svg" alt="{k.upper()} signal" width="160" height="160">
          </div>
        </div>
        <div class="paper-info">
          {title}
          <div class="paper-authors">{authors(p["a"])}</div>
          <div class="paper-venue">{venue}</div>{links}
          <p class="paper-desc">{E(p["d"])}</p>
        </div>
      </article>'''


def misc_row(color, title, items):
    rows = '\n'.join(f'            <div>{i}</div>' for i in items)
    return f'''      <div class="misc-row">
        <div class="misc-badge">
          <div class="colored-box" style="background-color: {color};">
            <h2>{title}</h2>
          </div>
        </div>
        <div class="misc-links">
{rows}
        </div>
      </div>'''


MISC = [
    ('#fcb97d', 'Experience', [
        'Research Assistant, <a href="https://mist.ac.bd/">MIST</a>, 2026–present',
        'Co-founder, <a href="https://www.insia-lab.com/home">INSIA Lab</a>, 2024–present',
        'Industrial Engineering Trainee, Grameenphone (Telenor Group), 2025']),
    ('#aaba9e', 'Service', [
        'Reviewer, IEEE Transactions on Affective Computing',
        'Chairperson, IEEE MIST Student Branch, 2025–2026',
        'Founding Chair, IEEE Signal Processing Society MIST SB Chapter, 2025–2026',
        'Secretary General, MIST Robotics Club, 2025–2026']),
    ('#c6b89e', 'Teaching', [
        'Instructor, Hands-on Arduino 3.0 and Pixel Pulse (150+ students)',
        'Organiser, 11+ signal processing workshops with BUET and DU',
        'Teaching interests: Signals and Systems, DSP, Circuits, Digital Logic, Microcontrollers, Machine Learning']),
    ('#edd892', 'Awards', [
        'Best Paper Award, IEEE SPICSCON 2025',
        'Best Presenter Award, IEEE QPAIN 2026',
        'Finalist and 2nd Runner-up (Biotech Poster), BEAR Summit, 2025',
        "Dean's List and Merit Scholarship, MIST, all four years"]),
    ('#b9c9de', 'Design', [
        'Former professional graphic designer: <a href="https://www.behance.net/sadmanrahman1">portfolio on Behance</a>',
        '<a href="../">Interactive version of this site</a>']),
]

PAGE = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Sadman Rahman</title>
    <meta name="author" content="Sadman Rahman">
    <meta name="description" content="Sadman Rahman: M.Sc. student in EEE at BUET working on signal processing, deep learning and applied AI for biomedical and wearable sensing.">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="color-scheme" content="light">
    <meta property="og:title" content="Sadman Rahman">
    <meta property="og:description" content="Signal processing, deep learning and applied AI for biomedical and wearable sensing.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://sdmrnwashere.github.io/academic/">
    <meta property="og:image" content="https://sdmrnwashere.github.io/academic/images/sadman.jpg">
    <link rel="icon" href="../assets/favicon.svg?v=2">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" type="text/css" href="stylesheet.css">
    <style>
      .paper-media .one img { border: 1px solid var(--border); }
      .misc-links > div { margin: 2px 0; }
    </style>
  </head>

  <body>
    <main class="page">
      <header class="bio">
        <div class="bio-text">
          <h1 class="name">Sadman Rahman</h1>
          <p>
            I'm an M.Sc. student in Electrical and Electronic Engineering at <a href="https://www.buet.ac.bd/">Bangladesh University of Engineering and Technology (BUET)</a>, advised by Dr. Shaikh Anowarul Fattah, and a Research Assistant at <a href="https://mist.ac.bd/">MIST</a>, where I'm developing a privacy-preserving, fingerprint-based attendance system for universities in Bangladesh.
          </p>
          <p>
            I did my B.Sc. in Electrical and Electronic Engineering at the <a href="https://mist.ac.bd/">Military Institute of Science and Technology (MIST)</a> with Dr. Kazi Newaj Faisal, graduating 2nd of 97 with a CGPA of 3.94/4.00. I co-founded <a href="https://www.insia-lab.com/home">INSIA Lab</a>, and my work has received the Best Paper Award at IEEE SPICSCON 2025 and the Best Presenter Award at IEEE QPAIN 2026.
          </p>
          <p class="bio-links">
            <a href="mailto:sdmrnwashere@gmail.com">Email</a> &nbsp;/&nbsp;
            <a href="../assets/Sadman_Rahman_CV.pdf">CV</a> &nbsp;/&nbsp;
            <a href="https://scholar.google.com/citations?user=nHt79bkAAAAJ&amp;hl=en">Scholar</a> &nbsp;/&nbsp;
            <a href="https://github.com/sdmrnwashere">GitHub</a> &nbsp;/&nbsp;
            <a href="https://www.linkedin.com/in/sadman-rahman-2412b0339/">LinkedIn</a> &nbsp;/&nbsp;
            <a href="https://www.researchgate.net/profile/Sadman-Rahman-5">ResearchGate</a>
          </p>
        </div>
        <div class="bio-photo">
          <a href="images/sadman.jpg"><img src="images/sadman.jpg" alt="Sadman Rahman" width="405" height="405"></a>
        </div>
      </header>

      <section class="section-header">
        <h2>Research</h2>
        <p>
          I'm interested in signal processing, deep learning, and applied AI, especially for biomedical and wearable sensing. Much of my work builds sharper time–frequency representations of non-stationary signals (EEG, ECG, IMU, radar, and audio) and compact neural networks that learn from them and can run on edge devices. I'm looking for Ph.D. positions. Representative papers are <span class="highlight">highlighted</span>; * denotes equal contribution.
        </p>
      </section>

      <section class="papers">
__PAPERS__
      </section>

      <section class="section-header">
        <h2>Miscellanea</h2>
      </section>

      <section class="misc">
__MISC__
      </section>

      <footer class="site-footer">
        <p>
          Website template from <a href="https://github.com/jonbarron/jonbarron.github.io">Jon Barron's source code</a>. Thanks, Jon!
        </p>
      </footer>
    </main>

    <script>
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
          document.querySelectorAll('.paper.hover-active').forEach(function(other) { other.classList.remove('hover-active'); });
          if (active) card.classList.add('hover-active');
        }, {passive: true});
      });
    </script>
  </body>
</html>
'''

page = PAGE.replace('__PAPERS__', '\n'.join(article(p) for p in pubs)).replace('__MISC__', '\n'.join(misc_row(*m) for m in MISC))
with open('academic/index.html', 'w', encoding='utf-8') as f:
    f.write(page)
print(len(pubs), 'papers written')
