import os
import glob

directory = r"d:\Rk hospitality"
html_files = glob.glob(os.path.join(directory, "*.html"))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace Gallery with Journey
    new_content = content.replace('>Gallery<', '>Journey<')
    
    # Just to be safe, also replace any #gallery hrefs to #journey if it makes sense, but we'll stick to just the text first.
    # Actually, the section ID is #gallery in index.html, so replacing the text is perfectly fine.
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes for {filepath}")
