import os
import re

css_dir = r"d:\Rk hospitality\css"
index_css_path = os.path.join(css_dir, "index.css")
global_css_path = os.path.join(css_dir, "global.css")

with open(index_css_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract hero styles
hero_styles_match = re.search(r'(/\* =========================================\s*HOSPITALITY HERO.*?left-align-div {\s*margin: 0 0 1.5rem 0;\s*})', index_content, re.DOTALL)

if hero_styles_match:
    hero_styles = hero_styles_match.group(1)
    
    # Remove from index.css
    new_index_content = index_content.replace(hero_styles, "")
    with open(index_css_path, 'w', encoding='utf-8') as f:
        f.write(new_index_content.strip() + "\n")
        
    # Add to global.css right before COMMON SECTION STYLES
    with open(global_css_path, 'r', encoding='utf-8') as f:
        global_content = f.read()
        
    target_str = "/* =========================================\n   COMMON SECTION STYLES\n   ========================================= */"
    if target_str in global_content:
        new_global_content = global_content.replace(target_str, hero_styles + "\n\n" + target_str)
        with open(global_css_path, 'w', encoding='utf-8') as f:
            f.write(new_global_content)
        print("Successfully moved hero styles to global.css")
    else:
        print("Could not find COMMON SECTION STYLES in global.css")
else:
    print("Could not find hero styles in index.css")
