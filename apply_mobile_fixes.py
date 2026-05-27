import os

base_dir = r"d:\Rk hospitality"

# 1. Update CSS
css_path = os.path.join(base_dir, "css", "global.css")
with open(css_path, "a", encoding="utf-8") as f:
    mobile_fixes_css = """
/* =========================================
   MOBILE FIXES (Hamburger & Footer)
   ========================================= */

.hamburger {
  display: none;
  flex-direction: column;
  gap: 6px;
  cursor: pointer;
  z-index: 1000;
  margin-right: auto;
  margin-left: 1rem;
}
.hamburger span {
  width: 28px;
  height: 3px;
  background-color: var(--gold-primary);
  transition: transform 0.3s ease, opacity 0.3s ease;
  border-radius: 2px;
}

@media (max-width: 768px) {
  /* Fix footer logo centering */
  .footer-brand {
    text-align: center;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .footer-logo {
    margin: 0 auto 1.5rem auto !important;
    display: block;
  }

  /* Hamburger & Mobile Nav */
  .global-header {
    position: relative;
    justify-content: flex-end;
  }
  .header-logo {
    margin-right: auto;
  }
  .hamburger {
    display: flex;
    order: 3;
    margin-left: 1rem;
    margin-right: 0;
  }
  .nav-links {
    display: flex !important; /* Override previous display: none */
    flex-direction: column;
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    background: rgba(10, 10, 10, 0.95);
    backdrop-filter: blur(10px);
    padding: 0;
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.4s ease, padding 0.4s ease;
    border-bottom: 1px solid transparent;
  }
  .nav-links.active {
    max-height: 500px;
    padding: 1.5rem 0;
    border-bottom: 1px solid var(--border-gold);
  }
  .nav-links li {
    width: 100%;
    text-align: center;
    padding: 0.8rem 0;
    margin: 0;
  }
  
  /* Hamburger Animation */
  .hamburger.active span:nth-child(1) {
    transform: translateY(9px) rotate(45deg);
  }
  .hamburger.active span:nth-child(2) {
    opacity: 0;
  }
  .hamburger.active span:nth-child(3) {
    transform: translateY(-9px) rotate(-45deg);
  }
  
  /* Header Buttons order */
  .header-cta {
    order: 2;
    padding: 0.5rem 1rem !important;
    font-size: 0.8rem !important;
  }
}
"""
    f.write(mobile_fixes_css)


# 2. Update JS for Hamburger Logic
js_path = os.path.join(base_dir, "js", "global.js")
with open(js_path, "a", encoding="utf-8") as f:
    mobile_fixes_js = """
// Mobile Hamburger Menu Logic
document.addEventListener("DOMContentLoaded", () => {
  const header = document.querySelector('.global-header');
  const navLinks = document.querySelector('.nav-links');
  
  if (header && navLinks && !document.querySelector('.hamburger')) {
    // Dynamically inject hamburger to avoid modifying all HTML files
    const hamburger = document.createElement('div');
    hamburger.className = 'hamburger';
    hamburger.innerHTML = '<span></span><span></span><span></span>';
    
    // Insert it
    header.appendChild(hamburger);
    
    // Toggle logic
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('active');
      navLinks.classList.toggle('active');
    });
    
    // Close menu when clicking a link
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navLinks.classList.remove('active');
      });
    });
  }
});
"""
    f.write(mobile_fixes_js)

print("Mobile fixes added successfully.")
