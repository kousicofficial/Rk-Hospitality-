import os

base_dir = r"d:\Rk hospitality"
css_path = os.path.join(base_dir, "css", "global.css")

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Add final polish mobile optimizations
final_mobile_fixes = """
/* =========================================
   FINAL POLISH FOR MOBILE VIEW
   ========================================= */
@media (max-width: 768px) {
  /* 1. Gallery Section - Force 1 column so images are not squashed */
  .gallery-grid, .about-media.gallery-split {
    grid-template-columns: 1fr !important;
    display: grid !important;
    gap: 2rem !important;
  }
  
  /* 2. Hero Backgrounds - Use landscape aspect ratio instead of 100vh full screen */
  .hospitality-hero {
    height: 60vh !important; 
    min-height: 400px !important;
  }
  .hero-title {
    font-size: 2.5rem !important;
  }
  .hero-subtitle {
    font-size: 0.9rem !important;
  }

  /* 3. Hamburger CTA Buttons - Make them large, bold, and padded in the menu */
  .nav-links .header-cta {
    display: block !important;
    width: 85%;
    margin: 1rem auto !important;
    text-align: center;
    padding: 1rem !important;
    font-size: 1rem !important;
    border-radius: 8px !important;
  }
  
  /* 4. Welcome Splash - Full screen sweep instead of awkward left-side curve on narrow screens */
  .splash-curtain {
    animation: splashSweepMobile 3.5s cubic-bezier(0.77, 0, 0.175, 1) forwards !important;
  }
  .splash-text {
    font-size: 1.5rem !important;
  }
  .splash-dynamic-text {
    font-size: 2.2rem !important;
  }
}

/* New Keyframe specifically for Mobile Splash Sweep (Center Expanding Circle) */
@keyframes splashSweepMobile {
  0% { clip-path: circle(0% at 50% 50%); }
  25% { clip-path: circle(150% at 50% 50%); } 
  75% { clip-path: circle(150% at 50% 50%); } 
  100% { clip-path: circle(0% at 50% 50%); }
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write(final_mobile_fixes)

print("Final mobile polish applied successfully to global.css.")
