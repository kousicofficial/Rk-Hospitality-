import os

base_dir = r"d:\Rk hospitality"

# 1. Update JS to add 'mobile-only-cta' class to the cloned LI
js_path = os.path.join(base_dir, "js", "global.js")
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

# Replace the LI creation in global.js
js = js.replace("const li = document.createElement('li');\n        li.appendChild(ctaClone);", 
                "const li = document.createElement('li');\n        li.className = 'mobile-only-cta';\n        li.appendChild(ctaClone);")

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js)

# 2. Update CSS to hide .mobile-only-cta on desktop
css_path = os.path.join(base_dir, "css", "global.css")
with open(css_path, "a", encoding="utf-8") as f:
    css_fix = """
/* Fix: Hide cloned mobile CTAs on desktop view */
@media (min-width: 769px) {
  .mobile-only-cta {
    display: none !important;
  }
}
"""
    f.write(css_fix)

print("Duplicate buttons on desktop fixed successfully.")
