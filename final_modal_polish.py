import os
import re

base_dir = r"d:\Rk hospitality"
css_path = os.path.join(base_dir, "css", "global.css")

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Make sure box-sizing is explicitly applied to the modal content
if "box-sizing: border-box !important;" not in css:
    css = css.replace(".booking-modal-content {\n    margin: 0 !important;", ".booking-modal-content {\n    box-sizing: border-box !important;\n    margin: 0 !important;")

# Adjust the close button size and padding so it NEVER overlaps the text
if "font-size: 1.5rem !important;" not in css:
    css = css.replace(".close-modal {\n    top: 15px !important;", ".close-modal {\n    top: 15px !important;\n    font-size: 1.5rem !important;\n    padding: 5px !important;\n    background: rgba(0,0,0,0.5) !important;\n    border-radius: 50% !important;\n    width: 30px !important;\n    height: 30px !important;\n    display: flex !important;\n    align-items: center !important;\n    justify-content: center !important;")

# Ensure the h2 text inside the modal is a reasonable size on mobile
css += """
@media (max-width: 768px) {
  .booking-modal-content h2 {
    font-size: 1.6rem !important;
    padding-right: 20px; /* Space for the X button */
  }
}
"""

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Final bulletproof CSS applied.")
