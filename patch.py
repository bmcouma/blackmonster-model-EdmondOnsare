import re

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update Hero to include slider and remove static text
    hero_slider_html = """
    <div class="hero-slider">
      <img src="assets/pictures/RUNWAY/DSC_9806.jpg" class="hero-bg active" alt="Slide 1">
      <img src="assets/pictures/FASHION CAMPAIGN/DSC_2034.jpg" class="hero-bg" alt="Slide 2">
      <img src="assets/pictures/AWARDS'/DSC_1712.jpg" class="hero-bg" alt="Slide 3">
      <img src="assets/pictures/JUDGING EVENT/DSC_9524.jpg" class="hero-bg" alt="Slide 4">
    </div>
    """
    
    html = re.sub(
        r'(<img[^>]*class="hero-bg"[^>]*>)',
        hero_slider_html,
        html
    )
    
    html = html.replace('<p class="hero-meta-secondary">Model | Model Judge | Event Organizer | Trainer | Team Builder</p>', '')

    # 2. Inject Big Stats Section before About
    stats_html = """
    <section id="stats" class="section stats-section">
      <div class="container stats-grid reveal reveal-up">
        <div class="stat-item">
          <span class="stat-number auto-count" data-target="22">0</span><span class="stat-plus">+</span>
          <p class="stat-label">Events Judged</p>
        </div>
        <div class="stat-item">
          <span class="stat-number auto-count" data-target="18">0</span><span class="stat-plus">+</span>
          <p class="stat-label">Solo Titles Won</p>
        </div>
        <div class="stat-item">
          <span class="stat-number auto-count" data-target="6">0</span><span class="stat-plus">+</span>
          <p class="stat-label">Years Active</p>
        </div>
      </div>
    </section>
    """
    html = html.replace('<section id="about" class="section about">', stats_html + '\n<section id="about" class="section about">')

    # 3. Update About Badges
    html = html.replace('<span>5+ Years Experience</span>', '<span><strong class="auto-count" data-target="5">0</strong>+ Years Experience</span>')
    html = html.replace('<span>100+ Models Trained</span>', '<span><strong class="auto-count" data-target="100">0</strong>+ Models Trained</span>')

    # 4. TikTok embeds in Media
    tiktok_embeds = """
        <div class="tiktok-grid">
          <div class="tiktok-embed-wrapper reveal reveal-up">
            <blockquote class="tiktok-embed" cite="https://www.tiktok.com/@blackmonster_9428/video/7438497645169495302" data-video-id="7438497645169495302"> <section> <a target="_blank" href="https://www.tiktok.com/@blackmonster_9428">@blackmonster_9428</a> </section> </blockquote> 
          </div>
          <div class="tiktok-embed-wrapper reveal reveal-up">
            <blockquote class="tiktok-embed" cite="https://www.tiktok.com/@blackmonster_9428/video/7438501235164895318" data-video-id="7438501235164895318"> <section> <a target="_blank" href="https://www.tiktok.com/@blackmonster_9428">@blackmonster_9428</a> </section> </blockquote> 
          </div>
          <div class="tiktok-embed-wrapper reveal reveal-up">
            <blockquote class="tiktok-embed" cite="https://www.tiktok.com/@blackmonster_9428/video/7438502345164895318" data-video-id="7438502345164895318"> <section> <a target="_blank" href="https://www.tiktok.com/@blackmonster_9428">@blackmonster_9428</a> </section> </blockquote> 
          </div>
        </div>
    """
    
    html = re.sub(
        r'<div class="video-grid">.*?</video>\s*</div>',
        tiktok_embeds,
        html,
        flags=re.DOTALL
    )

    # 5. Services Icons update
    services_html = """
        <div class="services-row" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">
          <article class="service-card reveal reveal-up service-bg-1" style="background: var(--card); padding: 2rem; border-radius: 8px; text-align: center;">
            <div class="service-overlay-dark"></div>
            <div class="service-icon" style="color: var(--gold); margin-bottom: 1rem;">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>
            </div>
            <h3>Model</h3>
            <p style="color: var(--muted); font-size: 0.95rem;">Signature runway command, high fashion editorial presence, and consistent delivery on any stage.</p>
          </article>
          <article class="service-card reveal reveal-up service-bg-2" style="background: var(--card); padding: 2rem; border-radius: 8px; text-align: center;">
            <div class="service-overlay-dark"></div>
            <div class="service-icon" style="color: var(--gold); margin-bottom: 1rem;">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect><path d="M9 14l2 2 4-4"></path></svg>
            </div>
            <h3>Judge</h3>
            <p style="color: var(--muted); font-size: 0.95rem;">Delivering fair, professional evaluation on confidence, posture, and performance potential at national events.</p>
          </article>
          <article class="service-card reveal reveal-up service-bg-3" style="background: var(--card); padding: 2rem; border-radius: 8px; text-align: center;">
            <div class="service-overlay-dark"></div>
            <div class="service-icon" style="color: var(--gold); margin-bottom: 1rem;">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line><polyline points="8 10 12 6 16 10"></polyline><line x1="12" y1="6" x2="12" y2="14"></line></svg>
            </div>
            <h3>Trainer</h3>
            <p style="color: var(--muted); font-size: 0.95rem;">Mentoring upcoming models on runway techniques, camera confidence, and professional industry conduct.</p>
          </article>
          <article class="service-card reveal reveal-up service-bg-4" style="background: var(--card); padding: 2rem; border-radius: 8px; text-align: center;">
            <div class="service-overlay-dark"></div>
            <div class="service-icon" style="color: var(--gold); margin-bottom: 1rem;">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
            </div>
            <h3>Event Organizer</h3>
            <p style="color: var(--muted); font-size: 0.95rem;">Producing premium talent showcases and managing teams for smooth, memorable fashion events.</p>
          </article>
        </div>
    """
    
    html = re.sub(
        r'<div class="services-grid">.*?</div>\s*</div>\s*</section>',
        services_html + '\n      </div>\n    </section>',
        html,
        flags=re.DOTALL
    )

    # 6. Add TikTok script at body end
    if '<script async src="https://www.tiktok.com/embed.js"></script>' not in html:
        html = html.replace('</body>', '  <script async src="https://www.tiktok.com/embed.js"></script>\n</body>')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

def update_css():
    css_append = """
/* NEW HERO SLIDER AND STATS */
.hero-slider { position: absolute; inset: 0; width: 100%; height: 100%; z-index: 0; }
.hero-bg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0; transition: opacity 1.5s ease-in-out; }
.hero-bg.active { opacity: 1; }
.hero-overlay { position: absolute; inset: 0; background: linear-gradient(110deg, rgba(0, 0, 0, 0.75), rgba(7, 16, 11, 0.46)); z-index: 1; }

.stats-section { padding: 40px 0; background: rgba(5, 7, 5, 0.8); border-bottom: 1px solid rgba(214, 185, 106, 0.2); }
.stats-grid { display: flex; justify-content: space-around; flex-wrap: wrap; gap: 2rem; text-align: center; }
.stat-number, .stat-plus { font-family: "Cormorant Garamond", serif; font-size: clamp(3rem, 5vw, 4rem); color: var(--gold); font-weight: bold; line-height: 1; }
.stat-label { color: var(--muted); text-transform: uppercase; font-size: 0.9rem; letter-spacing: 0.1em; margin-top: 10px; }

/* FIX IMAGE SIZES GLOBALLY */
img { max-width: 100%; object-fit: cover; }
.gallery-card img { max-height: 400px; width: 100%; }

/* TIKTOK GRID */
.tiktok-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; justify-items: center; }
.tiktok-embed-wrapper { width: 100%; max-width: 325px; border-radius: 8px; overflow: hidden; background: #000; }
"""
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write(css_append)

def update_js():
    js_append = """
// HERO SLIDER LOGIC
const slides = document.querySelectorAll(".hero-bg");
let currentSlide = 0;
if(slides.length > 0) {
  setInterval(() => {
    slides[currentSlide].classList.remove("active");
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add("active");
  }, 4000);
}

// AUTO COUNTER LOGIC
const countEls = document.querySelectorAll('.auto-count');
if (countEls.length > 0) {
    const ob = new IntersectionObserver(entries => {
        entries.forEach(e => {
            if(e.isIntersecting) {
                const el = e.target;
                const target = +el.getAttribute('data-target');
                let count = 0;
                let inc = Math.ceil(target / 40);
                let timer = setInterval(() => {
                    count += inc;
                    if(count >= target) { el.innerText = target; clearInterval(timer); }
                    else { el.innerText = count; }
                }, 40);
                ob.unobserve(el);
            }
        });
    });
    countEls.forEach(el => ob.observe(el));
}
"""
    with open('script.js', 'r', encoding='utf-8') as f:
        js = f.read()
    
    js = js.replace('Trainer AND TEAM BUILDER', 'Trainer & Team Builder')
    js = js.replace('Trainer | Team Builder', 'Trainer & Team Builder')

    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(js + "\n" + js_append)

if __name__ == "__main__":
    update_html()
    update_css()
    update_js()
    print("Patch applied cleanly.")
