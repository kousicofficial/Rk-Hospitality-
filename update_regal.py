import re

html_path = r"d:\Rk hospitality\regal.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Header Logo
html = html.replace(
    '<img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-hospitality-logo.jpeg" alt="RK Hospitality Logo">',
    '<img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-regal-logo-.jpeg" alt="RK Regal Logo">'
)

# 2. Update Footer Logo
html = html.replace(
    '<img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-hospitality-logo.jpeg" alt="RK Hospitality Logo" class="footer-logo">',
    '<img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-regal-logo-.jpeg" alt="RK Regal Logo" class="footer-logo">'
)

# 3. Hero Section Logo to Text
old_hero = """<img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-regal-logo-.jpeg" alt="RK Regal Logo" class="hero-brand-logo">
        <h1 class="hero-title" style="display:none;">RK Regal</h1>"""
new_hero = '<h1 class="hero-title" style="font-family: var(--font-heading); font-size: clamp(4rem, 8vw, 8rem); font-style: italic; font-weight: 700; letter-spacing: 5px;">RK Regal</h1>'
if old_hero in html:
    html = html.replace(old_hero, new_hero)
else:
    html = re.sub(r'<img[^>]*class="hero-brand-logo"[^>]*>\s*<h1 class="hero-title"[^>]*>RK Regal</h1>', new_hero, html)

# 4. Replace Journey with View Hall in Header
html = html.replace('<li><a href="#gallery">Journey</a></li>', '<li><a href="#view-hall">View Hall</a></li>')

# 5. Form headings
html = html.replace('<h2>Request an Audience</h2>', '<h2>Book Hall</h2>')
html = html.replace('<button type="submit" class="gold-submit-btn">Secure Table</button>', '<button type="submit" class="gold-submit-btn">Secure Hall</button>')

# 6. Add Book Now button to header if missing
if "btn-book-now" not in html:
    old_cta = '<a href="tel:+919600624445" class="header-cta">Get Details</a>'
    new_cta = '<a href="tel:+919600624445" class="header-cta">Get Details</a>\n    <button class="header-cta btn-book-now" style="margin-left: 1rem; background: var(--gold-primary); color: var(--bg-dark); border: none; cursor: pointer; padding: 0.6rem 1.5rem; font-family: var(--font-body); font-weight: 600; text-transform: uppercase; letter-spacing: 1.5px; border-radius: 4px; transition: background 0.3s ease;">Book Now</button>'
    html = html.replace(old_cta, new_cta)

# 7. Add View Hall section before booking section
view_hall_section = """
    <!-- View Hall Section -->
    <section id="view-hall" class="section-padding" style="background-color: var(--bg-dark-secondary);">
      <div class="section-title-wrapper" data-aos="fade-up">
        <span class="section-subtitle">Majestic Interiors</span>
        <h2 class="section-title">View Hall</h2>
        <div class="gold-divider-line small-divider"></div>
      </div>
      <div class="gallery-grid" data-aos="zoom-in" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; max-width: 1200px; margin: 0 auto;">
        <div class="gallery-item" style="border: 1px solid var(--border-gold); padding: 5px; background: var(--bg-dark);">
          <img src="https://supremehospitals.in/wp-content/uploads/2026/05/035A0318-scaled.jpg" alt="RK Regal Hall 1" style="width: 100%; height: 350px; object-fit: cover;">
        </div>
        <div class="gallery-item" style="border: 1px solid var(--border-gold); padding: 5px; background: var(--bg-dark);">
          <img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-reegal.jpeg" alt="RK Regal Hall 2" style="width: 100%; height: 350px; object-fit: cover;">
        </div>
        <div class="gallery-item" style="border: 1px solid var(--border-gold); padding: 5px; background: var(--bg-dark);">
          <img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-reegal-2.jpeg" alt="RK Regal Hall 3" style="width: 100%; height: 350px; object-fit: cover;">
        </div>
      </div>
    </section>
"""
# Insert right before booking section
html = re.sub(r'(<!-- Booking Section.*?</section>)', view_hall_section + r'\n\n    \1', html, flags=re.DOTALL)

# 8. Convert booking section to Modal
booking_match = re.search(r'<div class="booking-container.*?>(.*?)</div>\s*</section>', html, flags=re.DOTALL)
if booking_match and "id=\"bookingModal\"" not in html:
    inner_content = booking_match.group(1)
    
    modal_html = f"""
    <!-- Booking Modal -->
    <div id="bookingModal" class="booking-modal-overlay">
      <div class="booking-modal-content premium-glass-card">
        <span class="close-modal">&times;</span>
        {inner_content}
      </div>
    </div>
"""
    html = re.sub(r'<!-- Booking Section.*?<section id="booking".*?</section>', modal_html, html, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("regal.html updated successfully.")

# 9. Update regal.css for .gallery-split
css_path = r"d:\Rk hospitality\css\regal.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Make it stack vertically instead of side-by-side to fix squashing
old_split = """
.gallery-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
}

.gallery-split img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border: 1px solid var(--border-gold);
}
"""

new_split = """
.gallery-split {
  display: flex;
  flex-direction: column;
  gap: 20px;
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
}

.gallery-split img {
  width: 100%;
  height: auto;
  max-height: 400px;
  object-fit: contain;
  border: 1px solid var(--border-gold);
}
"""
css = css.replace(old_split.strip(), new_split.strip())

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("regal.css updated successfully.")
