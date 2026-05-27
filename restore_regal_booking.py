import re

html_path = r"d:\Rk hospitality\regal.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Check if it's already there
if '<section id="booking" class="booking-section' not in html:
    # Extract the inner content of the modal
    modal_content_match = re.search(r'<span class="close-modal">&times;</span>\s*(.*?)\s*</div>\s*</div>\s*</main>', html, flags=re.DOTALL)
    
    if modal_content_match:
        inner_content = modal_content_match.group(1)
        
        booking_section = f"""
    <!-- Booking Section (Restored) -->
    <section id="booking" class="booking-section section-padding">
      <div class="booking-container premium-glass-card" data-aos="fade-up">
        {inner_content}
      </div>
    </section>
"""
        
        # Insert right before the modal
        html = html.replace('<!-- Booking Modal -->', booking_section + '\n    <!-- Booking Modal -->')
        
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("Booking section successfully restored to regal.html")
    else:
        print("Could not find modal content to duplicate.")
else:
    print("Booking section is already in regal.html")
