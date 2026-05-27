import re
import os

html_path = r"d:\Rk hospitality\nexus.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Logo
new_logo = "https://supremehospitals.in/wp-content/uploads/2026/05/WhatsApp-Image-2026-05-26-at-12.02.54-PM.jpeg"
html = html.replace(
    '<img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-hospitality-logo.jpeg" alt="RK Hospitality Logo">',
    f'<img src="{new_logo}" alt="RK Nexus Logo">'
)
html = html.replace(
    '<img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-hospitality-logo.jpeg" alt="RK Hospitality Logo" class="footer-logo">',
    f'<img src="{new_logo}" alt="RK Nexus Logo" class="footer-logo">'
)

# 2. Add Book Now button
if "btn-book-now" not in html:
    old_cta = '<a href="tel:+919600624445" class="header-cta">Get Details</a>'
    new_cta = '<a href="tel:+919600624445" class="header-cta">Get Details</a>\n    <button class="header-cta btn-book-now" style="margin-left: 1rem; background: var(--gold-primary); color: var(--bg-dark); border: none; cursor: pointer; padding: 0.6rem 1.5rem; font-family: var(--font-body); font-weight: 600; text-transform: uppercase; letter-spacing: 1.5px; border-radius: 4px; transition: background 0.3s ease;">Book Now</button>'
    html = html.replace(old_cta, new_cta)

# 3. Create Modal while keeping the original section
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
    # Insert modal right after the booking section
    html = re.sub(r'(</section>)\s*</main>', r'\1\n\n' + modal_html + '\n  </main>', html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("nexus.html updated successfully.")
