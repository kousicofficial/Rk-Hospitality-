import os
import re

css_path = r"d:\Rk hospitality\css\gem.css"
html_path = r"d:\Rk hospitality\gem.html"

# 1. Update gem.html
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

header_html = """
    <section id="menu" class="gem-menu-new" style="background-color: var(--bg-dark);">
      <div class="section-title-wrapper" data-aos="fade-up" style="padding-top: 6rem; margin-bottom: 0;">
        <span class="section-subtitle">A Culinary Masterpiece</span>
        <h2 class="section-title">Our Menu</h2>
        <div class="gold-divider-line small-divider"></div>
      </div>
      <div class="menu-showcase-container">
"""

new_html_content = html_content.replace('<section id="menu" class="gem-menu-new">\n      <div class="menu-showcase-container">', header_html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_html_content)

# 2. Update gem.css
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

# Replace the layout block
old_block = """
.menu-showcase-container {
  display: flex;
  flex-direction: column;
}

.menu-row {
  display: flex;
  min-height: 80vh;
  background-color: var(--bg-dark);
}

.menu-row:nth-child(even) {
  background-color: var(--bg-dark-secondary);
}

.menu-content-block {
  flex: 1;
  padding: 5rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.menu-image-block {
  flex: 1;
  position: relative;
  overflow: hidden;
}
"""

new_block = """
.menu-showcase-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 4rem 5%;
  display: flex;
  flex-direction: column;
  gap: 6rem;
}

.menu-row {
  display: flex;
  align-items: stretch;
  gap: 4rem;
  background-color: transparent !important;
  min-height: auto;
}

.menu-content-block {
  flex: 1;
  background-color: var(--bg-dark-secondary);
  border: 1px solid var(--border-gold);
  border-radius: 12px;
  padding: 4rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  box-shadow: 0 15px 40px rgba(0,0,0,0.6);
}

.menu-image-block {
  flex: 1;
  border: 1px solid var(--border-gold);
  border-radius: 12px;
  overflow: hidden;
  position: relative;
  box-shadow: 0 15px 40px rgba(0,0,0,0.6);
  min-height: 500px;
}
"""

# Try to replace
if old_block.strip() in css_content:
    new_css = css_content.replace(old_block.strip(), new_block.strip())
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(new_css)
    print("CSS updated successfully.")
else:
    # If exact string replace fails, use regex
    print("Could not find exact block, attempting regex.")
    css_content = re.sub(r'\.menu-showcase-container.*?\.menu-image-block\s*{\s*flex: 1;\s*position: relative;\s*overflow: hidden;\s*}', new_block.strip(), css_content, flags=re.DOTALL)
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Regex CSS update applied.")

print("HTML updated successfully.")
