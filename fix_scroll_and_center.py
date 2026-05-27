import os

base_dir = r"d:\Rk hospitality"
css_path = os.path.join(base_dir, "css", "global.css")

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# 1. Global fix for horizontal scrolling (screen can be moved)
# We need to add this to the top of the file after the body rule.
if "html, body {" not in css:
    css = css.replace("body {\n  font-family", "html, body {\n  overflow-x: hidden !important;\n  width: 100%;\n  max-width: 100vw;\n  position: relative;\n}\n\nbody {\n  font-family")

# 2. Fix the modal centering by reverting to a clean flexbox layout without padding
# First, remove my previous 'robust' block fix
if "/* Robust Mobile Fixes for Modal and Hero Backgrounds */" in css:
    css = css.split("/* Robust Mobile Fixes for Modal and Hero Backgrounds */")[0]

clean_modal_fix = """
/* Robust Mobile Fixes for Modal and Hero Backgrounds */
@media (max-width: 768px) {
  /* 1. Modal Centering: Bulletproof flex layout */
  .booking-modal-overlay.show {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 0 !important; /* No padding to mess up width */
    overflow: hidden !important; /* Prevent overlay from scrolling */
  }
  
  .booking-modal-content {
    margin: 0 !important;
    width: 90% !important;
    max-width: 380px !important;
    max-height: 90vh !important;
    overflow-y: auto !important; /* Internal scrolling only */
    transform: none !important; /* Remove any translate animations */
    padding: 2.5rem 1.5rem !important;
  }
  
  .close-modal {
    top: 15px !important;
    right: 20px !important;
    z-index: 10;
  }

  /* 2. Fix Hero Backgrounds (like RK Grande Grassy Wall) being cropped */
  .hero-background img, .hero-background video {
    object-fit: contain !important;
    background-color: var(--bg-dark);
  }
  
  .hospitality-hero {
    height: 56.25vw !important; /* Perfect 16:9 landscape aspect ratio */
    min-height: 250px !important;
    max-height: 350px !important;
  }
}
"""

css += clean_modal_fix

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Horizontal scroll and modal centering fixed.")
