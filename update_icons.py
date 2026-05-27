import os
import glob

directory = r"d:\Rk hospitality"
html_files = glob.glob(os.path.join(directory, "*.html"))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace YT and IG with icons
    new_content = content.replace('>YT<', '><i class="fa-brands fa-youtube"></i><')
    new_content = new_content.replace('>IG<', '><i class="fa-brands fa-instagram"></i><')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes for {filepath}")
