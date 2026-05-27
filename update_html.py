import os
import re

directory = r"d:\Rk hospitality"
files = ["gem.html", "banquet.html", "stardom.html", "regal.html", "nexus.html"]

footer_template = """  <!-- Professional Footer -->
  <footer class="global-footer">
    <div class="footer-top">
      <div class="footer-brand">
        <img src="https://supremehospitals.in/wp-content/uploads/2026/05/rk-hospitality-logo.jpeg" alt="RK Hospitality Logo" class="footer-logo">
        <p>Experience the epitome of luxury and royal hospitality across our premium dining and event spaces.</p>
      </div>
      
      <div class="footer-col">
        <h4>Quick Links</h4>
        <ul class="footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="gem.html">GEM Restaurant</a></li>
          <li><a href="banquet.html">RK Grande</a></li>
          <li><a href="stardom.html">Stardom</a></li>
        </ul>
      </div>
      
      <div class="footer-col footer-contact">
        <h4>Contact Us</h4>
        <p>Phone: <a href="tel:+919600624445" style="color:var(--text-muted);">+91 9600624445</a></p>
        <p>Email: <a href="mailto:reservations@rkhospitality.com" style="color:var(--text-muted);">reservations@rkhospitality.com</a></p>
        <p>Location: RK Grande, No. 3/543, Bus Stand, Rajiv Gandhi Salai, opposite Kelambakkam, near HP Petrol Pump, Kittu Nagar, Kelambakkam, Tamil Nadu 603103</p>
        
        <div class="social-icons">
          <a href="#" aria-label="YouTube">YT</a>
          <a href="#" aria-label="Instagram">IG</a>
        </div>
      </div>
      
      <div class="footer-col footer-map">
        <h4>Find Us</h4>
        <div class="map-container">
          <a href="https://maps.google.com/?q=RK+Grande,+No.+3/543,+Bus+Stand,+Rajiv+Gandhi+Salai,+opposite+Kelambakkam,+near+HP+Petrol+Pump,+Kittu+Nagar,+Kelambakkam,+Tamil+Nadu+603103" target="_blank" class="map-overlay"></a>
          <iframe src="https://maps.google.com/maps?q=RK%20Grande,%20Kelambakkam,%20Tamil%20Nadu&t=&z=13&ie=UTF8&iwloc=&output=embed" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        </div>
      </div>
    </div>
    
    <div class="footer-bottom">
      <p>&copy; 2026 RK Hospitality. All Rights Reserved. Designed for Luxury.</p>
    </div>
  </footer>"""

for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace header CTA
    content = re.sub(
        r'<button class="header-cta"[^>]*>.*?</button>', 
        '<a href="tel:+919600624445" class="header-cta">Get Details</a>', 
        content
    )
    
    # Replace footer
    content = re.sub(
        r'<!-- Professional Footer -->.*?</footer>',
        footer_template,
        content,
        flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated all files successfully.")
