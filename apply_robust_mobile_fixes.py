import os

base_dir = r"d:\Rk hospitality"
css_path = os.path.join(base_dir, "css", "global.css")

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

robust_mobile_fixes = """
/* Robust Mobile Fixes for Modal and Hero Backgrounds */
@media (max-width: 768px) {
  /* 1. Modal Centering: Ditch flexbox and use foolproof block centering */
  .booking-modal-overlay.show {
    display: block !important; /* Force block layout */
    padding: 10vh 5% 5vh 5% !important; /* Top padding acts as positioning */
    overflow-y: auto !important; /* Allow scrolling if needed */
  }
  
  .booking-modal-content {
    display: block !important;
    position: relative !important;
    margin: 0 auto !important; /* Perfect horizontal center */
    left: auto !important;
    right: auto !important;
    width: 100% !important;
    max-width: 400px !important;
    transform: none !important;
  }
  
  /* Prevent 'X' button from overlapping text on narrow screens */
  .close-modal {
    top: 10px !important;
    right: 15px !important;
    z-index: 10;
  }

  /* 2. Fix Hero Backgrounds (like RK Grande Grassy Wall) being cropped */
  .hero-background img, .hero-background video {
    object-fit: contain !important;
    background-color: var(--bg-dark);
  }
  
  /* Ensure the hero container is more landscape so it fits the contained image nicely */
  .hospitality-hero {
    height: 50vw !important;
    min-height: 250px !important;
  }
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write(robust_mobile_fixes)

print("Robust mobile fixes applied.")
