import re
import os

base_dir = r"d:\Rk hospitality"

# 1. Update stardom.html specific requests
stardom_path = os.path.join(base_dir, "stardom.html")
with open(stardom_path, "r", encoding="utf-8") as f:
    stardom = f.read()

# Replace Header/Footer Logo with stardom-logo
stardom = stardom.replace(
    '<img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-hospitality-logo.jpeg" alt="RK Hospitality Logo">',
    '<img src="https://supremehospitals.in/wp-content/uploads/2026/05/stardom-logo.jpeg" alt="Stardom Logo">'
)
stardom = stardom.replace(
    '<img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-hospitality-logo.jpeg" alt="RK Hospitality Logo" class="footer-logo">',
    '<img src="https://supremehospitals.in/wp-content/uploads/2026/05/stardom-logo.jpeg" alt="Stardom Logo" class="footer-logo">'
)

# Hero Logo -> Text
old_hero = """<img src="https://supremehospitals.in/wp-content/uploads/2026/05/stardom-logo.jpeg" alt="Stardom Logo" class="hero-brand-logo">
        <h1 class="hero-title" style="display:none;">Stardom</h1>"""
new_hero = '<h1 class="hero-title" style="font-family: var(--font-heading); font-size: clamp(4rem, 8vw, 8rem); font-style: italic; font-weight: 700; letter-spacing: 5px;">Stardom</h1>'
stardom = stardom.replace(old_hero, new_hero)

# Nav Link
stardom = stardom.replace('<li><a href="#gallery">Journey</a></li>', '<li><a href="#view-igloo">View Igloo</a></li>')

# Add View Igloo section before booking
igloo_section = """
    <!-- View Igloo Section -->
    <section id="view-igloo" class="section-padding" style="background-color: var(--bg-dark);">
      <div class="section-title-wrapper" data-aos="fade-up">
        <span class="section-subtitle">Dine Under The Stars</span>
        <h2 class="section-title">View Igloo</h2>
        <div class="gold-divider-line small-divider"></div>
      </div>
      <div class="igloo-container" data-aos="zoom-in" style="max-width: 1200px; margin: 0 auto; border: 1px solid var(--border-gold); padding: 10px; background: var(--bg-dark-secondary);">
        <img src="https://supremehospitals.in/wp-content/uploads/2026/05/igloo-scaled.jpg" alt="Stardom Igloo" style="width: 100%; height: auto; display: block; object-fit: cover;">
      </div>
    </section>
"""

# Insert right before booking section
stardom = re.sub(r'(<!-- Booking Section.*?</section>)', igloo_section + r'\n\n    \1', stardom, flags=re.DOTALL)

with open(stardom_path, "w", encoding="utf-8") as f:
    f.write(stardom)

# 2. Add Book Now button & Convert Form to Modal (gem, banquet, stardom)
pages = ["gem.html", "banquet.html", "stardom.html"]

for page in pages:
    page_path = os.path.join(base_dir, page)
    with open(page_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Add Book Now button to header
    # Check if already added to avoid duplicates
    if "btn-book-now" not in html:
        old_cta = '<a href="tel:+919600624445" class="header-cta">Get Details</a>'
        new_cta = '<a href="tel:+919600624445" class="header-cta">Get Details</a>\n    <button class="header-cta btn-book-now" style="margin-left: 1rem; background: var(--gold-primary); color: var(--bg-dark); border: none; cursor: pointer; padding: 0.6rem 1.5rem; font-family: var(--font-body); font-weight: 600; text-transform: uppercase; letter-spacing: 1.5px; border-radius: 4px; transition: background 0.3s ease;">Book Now</button>'
        html = html.replace(old_cta, new_cta)

    # Convert booking section to Modal
    # Extract the booking-container inner HTML
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
        # Replace the entire booking section with the modal
        html = re.sub(r'<!-- Booking Section.*?<section id="booking".*?</section>', modal_html, html, flags=re.DOTALL)
        
    with open(page_path, "w", encoding="utf-8") as f:
        f.write(html)

print("HTML structures updated successfully.")
