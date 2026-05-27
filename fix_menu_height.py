import os

css_path = r"d:\Rk hospitality\css\global.css"

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace the max-height limit on the active mobile menu that was clipping the buttons
css = css.replace("max-height: 500px;", "max-height: 800px;")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Mobile menu max-height fixed successfully.")
