import os
import re

base_dir = r"d:\Rk hospitality"

# 1. Update global.css
css_path = os.path.join(base_dir, "css", "global.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Add new mobile optimizations to the end of the file
mobile_fixes = """
/* =========================================
   FURTHER MOBILE OPTIMIZATIONS
   ========================================= */
@media (max-width: 768px) {
  /* Fix logo line interruption by constraining height so it doesn't overflow header */
  .header-logo img {
    height: 55px !important;
    background: transparent !important;
  }
  
  /* Optimize Popup Modal for Mobile */
  .booking-modal-content {
    padding: 2rem 1.5rem !important;
    width: 95% !important;
    max-height: 85vh !important;
    overflow-y: auto !important;
    border-radius: 8px;
  }
  
  /* Force all form grids to 1 column on mobile */
  .form-grid {
    grid-template-columns: 1fr !important;
    gap: 1.5rem !important;
  }
  
  /* Ensure CTAs look great inside the mobile menu */
  .nav-links .header-cta {
    display: inline-block !important;
    width: 80%;
    margin: 0.5rem auto !important;
    text-align: center;
  }
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write(mobile_fixes)


# 2. Update global.js to clone CTAs into the mobile menu
js_path = os.path.join(base_dir, "js", "global.js")
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

# Find the existing mobile menu logic and replace it with an enhanced version
old_js_regex = r'// Mobile Hamburger Menu Logic.*?\}\);\s*\}\s*\}\);'

new_js = """
// Mobile Hamburger Menu Logic & CTA Injection
document.addEventListener("DOMContentLoaded", () => {
  const header = document.querySelector('.global-header');
  const navLinks = document.querySelector('.nav-links');
  
  if (header && navLinks && !document.querySelector('.hamburger')) {
    // Inject hamburger
    const hamburger = document.createElement('div');
    hamburger.className = 'hamburger';
    hamburger.innerHTML = '<span></span><span></span><span></span>';
    header.appendChild(hamburger);
    
    // Clone CTA buttons into the mobile menu dropdown
    const ctas = document.querySelectorAll('.header-cta');
    ctas.forEach(cta => {
      // Only clone if it's a direct child of header (prevents infinite loop if run multiple times)
      if (cta.parentElement === header) {
        const ctaClone = cta.cloneNode(true);
        const li = document.createElement('li');
        li.appendChild(ctaClone);
        navLinks.appendChild(li);
        
        // Re-attach modal listener to the cloned "Book Now" button
        if (ctaClone.classList.contains('btn-book-now')) {
          ctaClone.addEventListener('click', (e) => {
            e.preventDefault();
            const modal = document.getElementById("bookingModal");
            if (modal) {
              modal.classList.add("show");
              document.body.style.overflow = "hidden";
              // Close mobile menu when opening modal
              hamburger.classList.remove('active');
              navLinks.classList.remove('active');
            }
          });
        }
      }
    });
    
    // Toggle logic
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('active');
      navLinks.classList.toggle('active');
    });
    
    // Close menu when clicking a standard link
    navLinks.querySelectorAll('a:not(.header-cta)').forEach(link => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navLinks.classList.remove('active');
      });
    });
  }
});
"""

# If the old logic exists, replace it. Otherwise append.
if re.search(old_js_regex, js, flags=re.DOTALL):
    js = re.sub(old_js_regex, new_js.strip(), js, flags=re.DOTALL)
else:
    js += "\n" + new_js

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js)

print("Mobile optimizations applied successfully.")
