import os
import re

base_dir = r"d:\Rk hospitality"
pages = ["index.html", "gem.html", "banquet.html", "stardom.html", "regal.html", "nexus.html"]

page_titles = {
    "index.html": "RK Hospitality",
    "gem.html": "GEM Restaurant",
    "banquet.html": "RK Grande",
    "stardom.html": "Stardom",
    "regal.html": "RK Regal",
    "nexus.html": "RK Nexus"
}

# 1. Restore Booking Sections & Add Splash Screen HTML & Update Footer
for page in pages:
    path = os.path.join(base_dir, page)
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
        
    # --- Restore Booking Section (except index.html, regal already done but we check) ---
    if page != "index.html" and '<section id="booking" class="booking-section' not in html:
        match = re.search(r'<span class="close-modal">&times;</span>\s*(.*?)\s*</div>\s*</div>\s*</main>', html, flags=re.DOTALL)
        if match:
            inner_content = match.group(1)
            booking_section = f"""
    <!-- Booking Section (Restored) -->
    <section id="booking" class="booking-section section-padding">
      <div class="booking-container premium-glass-card" data-aos="fade-up">
        {inner_content}
      </div>
    </section>
"""
            html = html.replace('<!-- Booking Modal -->', booking_section + '\n    <!-- Booking Modal -->')
            
    # --- Update Footer ---
    old_footer_links = """<li><a href="banquet.html">RK Grande</a></li>
          <li><a href="stardom.html">Stardom</a></li>"""
    new_footer_links = """<li><a href="banquet.html">RK Grande</a></li>
          <li><a href="stardom.html">Stardom</a></li>
          <li><a href="regal.html">RK Regal</a></li>
          <li><a href="nexus.html">RK Nexus</a></li>"""
    html = html.replace(old_footer_links, new_footer_links)
    
    # --- Inject Splash Screen ---
    if 'class="welcome-splash"' not in html:
        splash_text = page_titles[page]
        splash_html = f"""
  <!-- Welcome Splash Animation -->
  <div class="welcome-splash">
    <div class="splash-curtain"></div>
    <h2 class="splash-text">Welcome to <span class="splash-dynamic-text">{splash_text}</span></h2>
  </div>
"""
        # Inject right after body tag
        html = re.sub(r'(<body[^>]*>)', r'\1\n' + splash_html, html)
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


# 2. Add Stardom Timings Next to Booking Form
stardom_path = os.path.join(base_dir, "stardom.html")
with open(stardom_path, "r", encoding="utf-8") as f:
    stardom = f.read()

# Replace the restored booking section with the split layout version
old_stardom_booking = re.search(r'(<!-- Booking Section \(Restored\) -->\s*<section id="booking" class="booking-section section-padding">)\s*<div class="booking-container premium-glass-card" data-aos="fade-up">', stardom, flags=re.DOTALL)
if old_stardom_booking:
    new_booking_start = """<!-- Booking Section (Restored) -->
    <section id="booking" class="booking-section section-padding stardom-booking">
      <div class="stardom-booking-wrapper" style="display: flex; gap: 3rem; max-width: 1200px; margin: 0 auto; align-items: flex-start; flex-wrap: wrap;">
        
        <!-- Timings Card -->
        <div class="stardom-timings premium-glass-card" data-aos="fade-right" style="flex: 1; min-width: 300px; padding: 3rem;">
          <div class="booking-header" style="text-align: left;">
            <h2 style="font-size: 2rem;">Stardom Timings</h2>
            <div class="gold-divider-line small-divider left-align-div"></div>
          </div>
          <ul class="gem-features" style="margin-top: 2rem;">
            <li style="margin-bottom: 1.5rem; font-size: 1.2rem;"><span class="gold-bullet"></span> Slot 1: 4.00 pm to 6.00 pm</li>
            <li style="margin-bottom: 1.5rem; font-size: 1.2rem;"><span class="gold-bullet"></span> Slot 2: 6.30 pm to 8.30 pm</li>
            <li style="margin-bottom: 1.5rem; font-size: 1.2rem;"><span class="gold-bullet"></span> Slot 3: 9.00 pm to 11.00 pm</li>
          </ul>
        </div>
        
        <div class="booking-container premium-glass-card" data-aos="fade-left" style="flex: 2; min-width: 300px; margin: 0; padding: 3rem;">
"""
    stardom = stardom.replace(old_stardom_booking.group(0), new_booking_start)
    
    # We also need to close the new wrapper div at the end of the section
    stardom = re.sub(r'(</form>\s*</div>\s*)\n\s*</section>', r'\1\n      </div>\n    </section>', stardom)

with open(stardom_path, "w", encoding="utf-8") as f:
    f.write(stardom)


# 3. Add Splash CSS to global.css
css_path = os.path.join(base_dir, "css", "global.css")
with open(css_path, "a", encoding="utf-8") as f:
    splash_css = """
/* =========================================
   WELCOME SPLASH ANIMATION
   ========================================= */
.welcome-splash {
  position: fixed;
  top: 0; left: 0; width: 100vw; height: 100vh;
  z-index: 999999;
  pointer-events: none;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.splash-curtain {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background: var(--bg-dark); /* Deep brown/black */
  clip-path: ellipse(0% 0% at 0% 0%);
  animation: splashSweep 3.5s cubic-bezier(0.77, 0, 0.175, 1) forwards;
}

.splash-text {
  position: relative;
  color: var(--text-light);
  font-family: var(--font-heading);
  font-size: clamp(2rem, 5vw, 4rem);
  letter-spacing: 2px;
  text-align: center;
  opacity: 0;
  transform: translateY(20px);
  animation: splashTextAppear 3.5s ease-in-out forwards;
}

.splash-dynamic-text {
  color: var(--gold-primary);
  font-style: italic;
  display: block;
  margin-top: 0.5rem;
  font-size: clamp(2.5rem, 6vw, 5rem);
}

@keyframes splashSweep {
  0% { clip-path: ellipse(0% 0% at 0% 0%); }
  25% { clip-path: ellipse(80% 120% at 0% 50%); } 
  75% { clip-path: ellipse(80% 120% at 0% 50%); } 
  100% { clip-path: ellipse(0% 0% at 0% 0%); }
}

@keyframes splashTextAppear {
  0%, 20% { opacity: 0; transform: translateY(20px); }
  35%, 65% { opacity: 1; transform: translateY(0); }
  80%, 100% { opacity: 0; transform: translateY(-20px); }
}

/* Base mobile responsive tweaks */
@media (max-width: 768px) {
  .about-container, .hero-content, .booking-container {
    padding: 1rem;
  }
  .global-header {
    padding: 1rem;
    flex-wrap: wrap;
  }
  .nav-links {
    display: none; /* Hide or make hamburger on real mobile */
  }
  h1.hero-title {
    font-size: 3rem !important;
  }
}
"""
    f.write(splash_css)

print("Massive global updates executed successfully.")
