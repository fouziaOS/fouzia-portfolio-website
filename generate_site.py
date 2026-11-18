#!/usr/bin/env python3
"""Build script for Fouzia Hoque's Personal Data Science Portfolio Website.

This site is built with Python + HTML + CSS only — no JavaScript.
Run this file to (re)generate index.html and style.css:

    python generate_site.py

Then open index.html in any browser. The chart images live in images/.
"""

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Fouzia Hoque — Data Science Portfolio</title>
<meta name="description" content="Personal Data Science portfolio of Fouzia Hoque — CSE student at Southeast University. Python projects, NumPy in 50 examples, Data Visualization in 50 examples, and data analysis work.">
<link rel="stylesheet" href="style.css">
</head>
<body>

<header class="nav">
  <a class="logo" href="#home">Fouzia<span>.</span></a>
  <nav>
    <a href="#home">Home</a>
    <a href="#about">About Me</a>
    <a href="#python-projects">Python Projects</a>
    <a href="#numpy">NumPy (50 Codes)</a>
    <a href="#dataviz">Data Visualization (50 Codes)</a>
    <a href="#analysis">Data Analysis</a>
    <a href="#github">GitHub Profile</a>
    <a href="#contact">Contact</a>
  </nav>
  <input type="checkbox" id="menuToggle" class="menu-toggle">
  <label for="menuToggle" class="menu-btn" aria-label="Open menu">☰</label>
</header>

<!-- HOME -->
<section id="home" class="hero">
  <div class="hero-inner reveal">
    <p class="hero-tag">Welcome to my portfolio</p>
    <h1>Hi, I'm <span class="accent">Fouzia Hoque</span></h1>
    <h2 class="typing-line">I am a
      <span class="rotator">
        <span>Aspiring Data Scientist</span>
        <span>Python Programmer</span>
        <span>Data Analyst &amp; Visualizer</span>
        <span>Generative AI Researcher</span>
      </span>
    </h2>
    <p class="hero-text">CSE Student @ Southeast University · Aspiring Data Scientist · Python · AI · ML · Generative AI Research</p>
    <div class="hero-btns">
      <a class="btn primary" href="#python-projects">View My Projects</a>
      <a class="btn ghost" href="https://github.com/fouziaOS" target="_blank" rel="noopener">GitHub Profile</a>
    </div>
    <div class="hero-stats">
      <div><strong>100+</strong><small>Code Examples</small></div>
      <div><strong>8</strong><small>GitHub Repositories</small></div>
      <div><strong>100</strong><small>Survey Responses Analyzed</small></div>
      <div><strong>3</strong><small>Live Web Projects</small></div>
    </div>
  </div>
</section>

<!-- ABOUT -->
<section id="about" class="section">
  <h2 class="section-title reveal">About <span class="accent">Me</span></h2>
  <div class="about-grid">
    <div class="about-card reveal">
      <h3>Who I am</h3>
      <p>I am a Computer Science &amp; Engineering student at <strong>Southeast University, Dhaka, Bangladesh</strong>, passionate about Data Science, Python, and Artificial Intelligence. I enjoy turning raw data into clear stories — cleaning messy datasets, finding patterns, and presenting insights with beautiful charts.</p>
      <p>My final-year research (CSE 460, FYDP-I) studies <strong>the impact of Generative AI on the creativity and performance levels of students</strong> — a quantitative survey study where I designed the questionnaire, ran a pilot survey of 100 students, and analyzed the responses.</p>
    </div>
    <div class="about-card reveal">
      <h3>My skills</h3>
      <div class="chips">
        <span>Python</span><span>NumPy</span><span>Pandas</span><span>Matplotlib</span>
        <span>Data Analysis</span><span>Data Visualization</span><span>Statistics</span>
        <span>Survey Research</span><span>Git &amp; GitHub</span><span>HTML</span>
        <span>CSS</span><span>Arduino</span><span>ESP32</span>
      </div>
      <h3 class="mt">Currently learning</h3>
      <p>Machine Learning fundamentals, SQL for data analysis, and advanced Pandas workflows.</p>
    </div>
  </div>
</section>

<!-- PYTHON PROJECTS -->
<section id="python-projects" class="section alt">
  <h2 class="section-title reveal">Python <span class="accent">Projects</span></h2>
  <div class="cards">
    <article class="card reveal">
      <div class="card-emoji">📚</div>
      <h3>FocusFlow — Study Planner</h3>
      <p>A study planner web app with task management, a Pomodoro focus timer, and a weekly progress chart — runs fully offline in the browser.</p>
      <a href="https://github.com/fouziaOS/focusflow-study-planner" target="_blank" rel="noopener">View on GitHub →</a>
    </article>
    <article class="card reveal">
      <div class="card-emoji">🧠</div>
      <h3>QuizMaster — Python Quiz</h3>
      <p>An interactive quiz app with 24 questions in 3 categories (Python Basics, NumPy &amp; Pandas, Data Visualization), a per-question timer, explanations, and best-score tracking.</p>
      <a href="https://github.com/fouziaOS/quizmaster-python-quiz" target="_blank" rel="noopener">View on GitHub →</a>
    </article>
    <article class="card reveal">
      <div class="card-emoji">💰</div>
      <h3>KharchaTrack — Expense Tracker</h3>
      <p>A BDT income &amp; expense tracker with category charts and month filtering — a small personal-finance data tool that runs fully offline.</p>
      <a href="https://github.com/fouziaOS/kharchatrack-expense-tracker" target="_blank" rel="noopener">View on GitHub →</a>
    </article>
    <article class="card reveal">
      <div class="card-emoji">🗺️</div>
      <h3>Bellman-Ford &amp; the Yen-BF Technique</h3>
      <p>Advanced Algorithm research poster: an efficient improvement of the Bellman-Ford shortest-path algorithm using the Yen-BF technique, with a verified case study.</p>
      <a href="https://github.com/fouziaOS/bellman-ford-yen-bf-poster" target="_blank" rel="noopener">View on GitHub →</a>
    </article>
  </div>
</section>

<!-- NUMPY -->
<section id="numpy" class="section">
  <h2 class="section-title reveal">NumPy <span class="accent">(50 Codes)</span></h2>
  <div class="feature reveal">
    <p><strong>NumPy in 50 Examples</strong> — my hands-on collection of 50 NumPy examples with 8 runnable Python scripts and a Jupyter notebook. It covers everything from creating arrays to linear algebra, statistics, and random simulations — the foundation of all my data work.</p>
    <div class="chips">
      <span>Array Creation</span><span>Indexing &amp; Slicing</span><span>Broadcasting</span>
      <span>Math Operations</span><span>Linear Algebra</span><span>Statistics</span>
      <span>Random Numbers</span><span>Sorting &amp; Searching</span><span>Reshaping</span>
    </div>
    <a class="btn primary mt" href="https://github.com/fouziaOS/numpy-50-examples" target="_blank" rel="noopener">Open the NumPy Repository</a>
  </div>
</section>

<!-- DATA VISUALIZATION -->
<section id="dataviz" class="section alt">
  <h2 class="section-title reveal">Data Visualization <span class="accent">(50 Codes)</span></h2>
  <div class="feature reveal">
    <p><strong>Data Visualization in 50 Examples (Matplotlib)</strong> — 50 chart examples with full code and a gallery: line plots, scatter plots, bar charts, histograms, box plots, violin plots, and more. A few favorites:</p>
  </div>
  <div class="gallery">
    <figure class="reveal"><img src="images/01_simple_line_plot.png" alt="Simple line plot"><figcaption>Line Plot</figcaption></figure>
    <figure class="reveal"><img src="images/04_scatter_plot.png" alt="Scatter plot"><figcaption>Scatter Plot</figcaption></figure>
    <figure class="reveal"><img src="images/06_bar_chart_with_value_labels.png" alt="Bar chart with value labels"><figcaption>Bar Chart</figcaption></figure>
    <figure class="reveal"><img src="images/09_histogram_with_mean_line.png" alt="Histogram with mean line"><figcaption>Histogram</figcaption></figure>
    <figure class="reveal"><img src="images/11_box_plot.png" alt="Box plot"><figcaption>Box Plot</figcaption></figure>
    <figure class="reveal"><img src="images/12_violin_plot.png" alt="Violin plot"><figcaption>Violin Plot</figcaption></figure>
  </div>
  <div class="center reveal">
    <a class="btn primary" href="https://github.com/fouziaOS/data-visualization-50-examples" target="_blank" rel="noopener">See All 50 Charts on GitHub</a>
  </div>
</section>

<!-- DATA ANALYSIS -->
<section id="analysis" class="section">
  <h2 class="section-title reveal">Data <span class="accent">Analysis</span></h2>
  <div class="feature reveal">
    <p>Data analysis is at the heart of my research. For my FYDP-I study on Generative AI and students, I designed a 17-question survey, collected pilot responses from <strong>100 students</strong>, and analyzed which AI tools students use (ChatGPT 88%, Gemini 56%, Claude 40%…) and how usage relates to their creativity and academic performance.</p>
  </div>
  <div class="steps">
    <div class="step reveal"><strong>1</strong><h4>Collect</h4><p>Survey design &amp; data collection</p></div>
    <div class="step reveal"><strong>2</strong><h4>Clean</h4><p>Missing values, coding, validation</p></div>
    <div class="step reveal"><strong>3</strong><h4>Analyze</h4><p>Frequencies, correlations, comparisons</p></div>
    <div class="step reveal"><strong>4</strong><h4>Visualize</h4><p>Charts that make patterns obvious</p></div>
    <div class="step reveal"><strong>5</strong><h4>Conclude</h4><p>Insights, limits &amp; honest reporting</p></div>
  </div>
  <div class="chips center-chips reveal">
    <span>Pandas</span><span>NumPy</span><span>Matplotlib</span><span>Microsoft Excel</span><span>Google Sheets</span><span>Survey Data</span><span>Statistical Analysis</span>
  </div>
</section>

<!-- GITHUB -->
<section id="github" class="section alt">
  <h2 class="section-title reveal">GitHub <span class="accent">Profile</span></h2>
  <div class="github-card reveal">
    <div class="gh-avatar">FH</div>
    <div>
      <h3>Fouzia Hoque · <a href="https://github.com/fouziaOS" target="_blank" rel="noopener">@fouziaOS</a></h3>
      <p>CSE Student @ Southeast University | Aspiring Data Scientist | Python · AI · ML | Generative AI Research</p>
      <div class="gh-repos">
        <a href="https://github.com/fouziaOS/numpy-50-examples" target="_blank" rel="noopener">numpy-50-examples</a>
        <a href="https://github.com/fouziaOS/data-visualization-50-examples" target="_blank" rel="noopener">data-visualization-50-examples</a>
        <a href="https://github.com/fouziaOS/bellman-ford-yen-bf-poster" target="_blank" rel="noopener">bellman-ford-yen-bf-poster</a>
        <a href="https://github.com/fouziaOS/focusflow-study-planner" target="_blank" rel="noopener">focusflow-study-planner</a>
        <a href="https://github.com/fouziaOS/quizmaster-python-quiz" target="_blank" rel="noopener">quizmaster-python-quiz</a>
        <a href="https://github.com/fouziaOS/kharchatrack-expense-tracker" target="_blank" rel="noopener">kharchatrack-expense-tracker</a>
      </div>
    </div>
  </div>
</section>

<!-- CONTACT -->
<section id="contact" class="section">
  <h2 class="section-title reveal">Contact</h2>
  <div class="contact-grid reveal">
    <a class="contact-item" href="mailto:fouziahoque12@gmail.com">
      <strong>✉️ Email</strong><span>fouziahoque12@gmail.com</span>
    </a>
    <a class="contact-item" href="https://github.com/fouziaOS" target="_blank" rel="noopener">
      <strong>🐙 GitHub</strong><span>github.com/fouziaOS</span>
    </a>
    <div class="contact-item">
      <strong>📍 Location</strong><span>Dhaka, Bangladesh</span>
    </div>
    <div class="contact-item">
      <strong>🎓 University</strong><span>Southeast University</span>
    </div>
  </div>
  <p class="contact-note reveal">I am open to internships, research collaboration, and data projects. Feel free to reach out by email!</p>
</section>

<footer>
  <p>© 2026 Fouzia Hoque · Built with Python, HTML &amp; CSS — no JavaScript · <a href="https://github.com/fouziaOS" target="_blank" rel="noopener">github.com/fouziaOS</a></p>
</footer>

</body>
</html>
'''

CSS = r''':root{
  --bg:#0b1220; --bg2:#0f1a2e; --surface:#132239; --surface2:#182a47;
  --text:#e8eef7; --muted:#9db2cc; --accent:#22d3ee; --accent2:#2e75b6;
  --border:#22365a; --radius:14px;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:'Segoe UI',system-ui,Arial,sans-serif;background:var(--bg);color:var(--text);line-height:1.6}
a{color:var(--accent);text-decoration:none}
.accent{color:var(--accent)}
.mt{margin-top:18px}
.center{text-align:center;margin-top:26px}

/* NAV */
.nav{position:sticky;top:0;z-index:50;display:flex;align-items:center;justify-content:space-between;
  padding:12px 26px;background:rgba(11,18,32,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--border)}
.logo{font-size:24px;font-weight:800;color:var(--text)}
.logo span{color:var(--accent)}
.nav nav{display:flex;gap:18px;flex-wrap:wrap}
.nav nav a{color:var(--muted);font-size:14.5px;font-weight:600}
.nav nav a:hover{color:var(--accent)}
.menu-toggle{display:none}
.menu-btn{display:none;background:none;border:1px solid var(--border);color:var(--text);
  border-radius:8px;font-size:18px;padding:4px 10px;cursor:pointer}

/* HERO */
.hero{min-height:88vh;display:flex;align-items:center;justify-content:center;text-align:center;
  padding:60px 20px;background:radial-gradient(900px 480px at 50% -10%,#164e63 0%,var(--bg) 60%)}
.hero-tag{letter-spacing:3px;text-transform:uppercase;color:var(--accent);font-size:13px;font-weight:700}
.hero h1{font-size:52px;margin:10px 0 4px}
.typing-line{font-size:26px;color:var(--muted);min-height:38px;font-weight:600}
.rotator{display:inline-grid;text-align:left;vertical-align:bottom}
.rotator>span{grid-area:1/1;color:var(--accent);opacity:0;white-space:nowrap;animation:rotateWord 12s infinite}
.rotator>span:nth-child(2){animation-delay:3s}
.rotator>span:nth-child(3){animation-delay:6s}
.rotator>span:nth-child(4){animation-delay:9s}
@keyframes rotateWord{0%{opacity:0;transform:translateY(8px)}4%{opacity:1;transform:none}25%{opacity:1}29%{opacity:0;transform:translateY(-8px)}100%{opacity:0}}
.hero-text{color:var(--muted);max-width:640px;margin:12px auto 0}
.hero-btns{margin-top:26px;display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.btn{display:inline-block;padding:12px 24px;border-radius:999px;font-weight:700;font-size:15px}
.btn.primary{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#04121f}
.btn.primary:hover{filter:brightness(1.12)}
.btn.ghost{border:1.5px solid var(--accent);color:var(--accent)}
.btn.ghost:hover{background:rgba(34,211,238,.1)}
.hero-stats{display:flex;gap:38px;justify-content:center;margin-top:44px;flex-wrap:wrap}
.hero-stats div{text-align:center}
.hero-stats strong{display:block;font-size:30px;color:var(--accent)}
.hero-stats small{color:var(--muted);font-size:13px}

/* SECTIONS */
.section{padding:78px 22px;max-width:1080px;margin:0 auto}
.section.alt{max-width:none;background:var(--bg2)}
.section.alt>*{max-width:1080px;margin-left:auto;margin-right:auto}
.section-title{font-size:34px;text-align:center;margin-bottom:34px}
.about-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.about-card,.feature{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:26px}
.about-card h3{color:var(--accent);margin-bottom:10px}
.about-card p{color:var(--muted);margin-bottom:10px}
.about-card p strong{color:var(--text)}
.feature p{color:var(--muted)}
.feature p strong{color:var(--text)}
.chips{display:flex;flex-wrap:wrap;gap:9px;margin-top:8px}
.chips span{background:var(--surface2);border:1px solid var(--border);color:var(--text);
  padding:6px 13px;border-radius:999px;font-size:13.5px;font-weight:600}
.center-chips{justify-content:center;margin-top:24px}

/* PROJECT CARDS */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:20px}
.card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:24px;
  transition:transform .18s ease,border-color .18s ease}
.card:hover{transform:translateY(-5px);border-color:var(--accent)}
.card-emoji{font-size:34px;margin-bottom:8px}
.card h3{margin-bottom:8px;font-size:18px}
.card p{color:var(--muted);font-size:14.5px;margin-bottom:14px}

/* GALLERY */
.gallery{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:18px;margin-top:24px}
.gallery figure{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden}
.gallery img{width:100%;display:block;background:#fff}
.gallery figcaption{padding:10px 14px;font-weight:700;font-size:14px;color:var(--muted)}

/* STEPS */
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:16px;margin-top:24px}
.step{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:20px;text-align:center}
.step strong{display:inline-flex;align-items:center;justify-content:center;width:38px;height:38px;
  border-radius:50%;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#04121f;font-size:18px}
.step h4{margin:10px 0 4px}
.step p{color:var(--muted);font-size:13.5px}

/* GITHUB CARD */
.github-card{display:flex;gap:22px;align-items:flex-start;background:var(--surface);
  border:1px solid var(--border);border-radius:var(--radius);padding:26px}
.gh-avatar{flex:0 0 auto;width:74px;height:74px;border-radius:50%;display:flex;align-items:center;justify-content:center;
  background:linear-gradient(135deg,var(--accent),var(--accent2));color:#04121f;font-size:26px;font-weight:800}
.github-card p{color:var(--muted);margin:6px 0 14px}
.gh-repos{display:flex;flex-wrap:wrap;gap:9px}
.gh-repos a{background:var(--surface2);border:1px solid var(--border);padding:6px 13px;border-radius:999px;font-size:13.5px;font-weight:600}

/* CONTACT */
.contact-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px}
.contact-item{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
  padding:20px;display:flex;flex-direction:column;gap:4px;color:var(--text)}
.contact-item span{color:var(--muted);font-size:14.5px}
a.contact-item:hover{border-color:var(--accent)}
.contact-note{text-align:center;color:var(--muted);margin-top:24px}

footer{text-align:center;padding:26px 16px;border-top:1px solid var(--border);color:var(--muted);font-size:14px}

/* REVEAL ANIMATION */
.reveal{animation:fadeUp .7s ease both}
@keyframes fadeUp{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:none}}

/* RESPONSIVE */
@media (max-width:860px){
  .hero h1{font-size:38px}
  .typing-line{font-size:20px}
  .about-grid{grid-template-columns:1fr}
  .github-card{flex-direction:column}
  .menu-btn{display:block}
  .nav nav{display:none;position:absolute;top:58px;left:0;right:0;flex-direction:column;gap:0;
    background:var(--bg2);border-bottom:1px solid var(--border);padding:8px 0}
  .menu-toggle:checked~nav{display:flex}
  .nav nav a{padding:10px 26px}
}
'''

def main():
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(HTML)
    with open("style.css", "w", encoding="utf-8") as f:
        f.write(CSS)
    print("Built index.html and style.css — open index.html in a browser.")

if __name__ == "__main__":
    main()
