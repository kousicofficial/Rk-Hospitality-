import os
import glob
import re

base_dir = r"d:\Rk hospitality"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the massive clamp(4rem,...) with a more mobile-friendly clamp(2.5rem,...)
    content = re.sub(r'clamp\(4rem,\s*8vw,\s*8rem\)', 'clamp(2.5rem, 6vw, 6rem)', content)
    
    # Also replace any clamp(3rem,...) if they exist
    content = re.sub(r'clamp\(3rem,\s*8vw,\s*8rem\)', 'clamp(2rem, 5vw, 5rem)', content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Fixed inline hero title font sizes.")
