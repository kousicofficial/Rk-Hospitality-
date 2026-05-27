import re

html_path = r"d:\Rk hospitality\banquet.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Header Logo
html = html.replace(
    '<img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-hospitality-logo.jpeg" alt="RK Hospitality Logo">',
    '<img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-grande-banquet-hall-logo-.jpeg" alt="RK Grande Logo">'
)

# 2. Update Footer Logo
html = html.replace(
    '<img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-hospitality-logo.jpeg" alt="RK Hospitality Logo" class="footer-logo">',
    '<img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-grande-banquet-hall-logo-.jpeg" alt="RK Grande Logo" class="footer-logo">'
)

# 3. Update Hero Background Image
html = html.replace(
    '<img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-grande-outerimage-scaled.jpg" alt="RK Grande Hero">',
    '<img src="https://supremehospitals.in/wp-content/uploads/2026/05/Rk-grande-hero-section-image-scaled.jpg" alt="RK Grande Hero">'
)

# 4. Replace Journey with Gallery in Header
html = html.replace('<li><a href="#gallery">Journey</a></li>', '<li><a href="#gallery">Gallery</a></li>')

# 5. Hero Section Logo to Text
hero_logo_block = """<img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-grande-banquet-hall-logo-.jpeg" alt="RK Grande Logo" class="hero-brand-logo">
        <h1 class="hero-title" style="display:none;">RK Grande</h1>"""
new_hero_text = '<h1 class="hero-title" style="font-family: var(--font-heading); font-size: clamp(4rem, 8vw, 8rem); font-style: italic; font-weight: 700; letter-spacing: 5px;">RK Grande</h1>'
html = html.replace(hero_logo_block, new_hero_text)

# 6. The Grand Gallery updates
old_gallery = """<div class="gallery-container" data-aos="zoom-in">
        <img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-grande-banquet-hal-ggallery-scaled.jpg" alt="RK Grande Gallery">
        <div class="gallery-gold-border"></div>
      </div>"""

new_gallery = """<div class="gallery-grid" data-aos="zoom-in" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 2rem; max-width: 1200px; margin: 0 auto;">
        <div class="gallery-item" style="border: 1px solid var(--border-gold); padding: 5px; background: var(--bg-dark);">
          <img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-grande-banquet-hal-ggallery-scaled.jpg" alt="RK Grande Gallery 1" style="width: 100%; height: 350px; object-fit: cover;">
        </div>
        <div class="gallery-item" style="border: 1px solid var(--border-gold); padding: 5px; background: var(--bg-dark);">
          <img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-grande-gallery-2-scaled.jpg" alt="RK Grande Gallery 2" style="width: 100%; height: 350px; object-fit: cover;">
        </div>
        <div class="gallery-item" style="border: 1px solid var(--border-gold); padding: 5px; background: var(--bg-dark);">
          <img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-grande-gallery-image-scaled.jpg" alt="RK Grande Gallery 3" style="width: 100%; height: 350px; object-fit: cover;">
        </div>
        <div class="gallery-item" style="border: 1px solid var(--border-gold); padding: 5px; background: var(--bg-dark);">
          <img src="https://supremehospitals.in/wp-content/uploads/2026/05/rkgrande-gallery-3-scaled.jpg" alt="RK Grande Gallery 4" style="width: 100%; height: 350px; object-fit: cover;">
        </div>
      </div>"""

html = html.replace(old_gallery, new_gallery)

# 7. Form Updates
old_select = """<select required style="color: var(--text-light); background: transparent;">
                <option value="" disabled selected style="color: black;">Select Event</option>
                <option value="Wedding" style="color: black;">Wedding</option>
                <option value="Corporate" style="color: black;">Corporate Event</option>
                <option value="Party" style="color: black;">Private Party</option>
              </select>"""
new_input = '<input type="text" placeholder="Please tell your function type" required>'
html = html.replace(old_select, new_input)

# Add Start Time and End Time fields
old_date_field = """<div class="input-group">
              <label>Event Date</label>
              <input type="date" required>
            </div>"""

new_date_time = """<div class="input-group">
              <label>Event Date</label>
              <input type="date" required>
            </div>
            <div class="input-group">
              <label>Start Time</label>
              <input type="time" required>
            </div>
            <div class="input-group">
              <label>End Time</label>
              <input type="time" required>
            </div>"""

html = html.replace(old_date_field, new_date_time)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated banquet.html successfully.")
