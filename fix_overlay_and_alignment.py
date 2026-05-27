import os

base_dir = r"d:\Rk hospitality"
css_path = os.path.join(base_dir, "css", "global.css")

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Fix the invisible modal overlay blocking clicks
css = css.replace("display: flex !important;\n    align-items: center !important;", "align-items: center !important;")

# Fix image alignment cropping by allowing images to contain instead of cover
# Specifically for about-media images
css += """
/* Fix: Don't crop logos/images that have text inside them */
.about-media img, .about-media video {
  object-fit: contain !important;
  background: var(--bg-dark);
}
"""

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed click-blocking overlay and image alignment issues.")
