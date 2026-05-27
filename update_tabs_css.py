import os

css_path = r"d:\Rk hospitality\css\gem.css"
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

# We want to replace the `.menu-showcase-container` and below with the tabbed CSS.
# So we can just split at `.menu-showcase-container` and append the new rules.

new_css = """
/* =========================================
   TABBED MENU SHOWCASE
   ========================================= */
.menu-tabs-container {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 1rem;
  padding: 3rem 5%;
  max-width: 1200px;
  margin: 0 auto;
}

.menu-tab {
  background: transparent;
  border: 1px solid var(--border-gold);
  color: var(--gold-primary);
  padding: 0.8rem 2rem;
  font-family: var(--font-body);
  font-size: 0.9rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 2px;
  cursor: pointer;
  border-radius: 4px;
  transition: all 0.3s ease;
}

.menu-tab:hover, .menu-tab.active {
  background: var(--gold-primary);
  color: var(--bg-dark);
}

.tab-content {
  display: none !important;
  opacity: 0;
  transition: opacity 0.5s ease;
}

.tab-content.active {
  display: flex !important;
  opacity: 1;
  animation: fadeInTab 0.6s forwards;
}

@keyframes fadeInTab {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.menu-showcase-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 5% 4rem;
}

.menu-row {
  align-items: stretch;
  gap: 4rem;
  background-color: transparent !important;
}

.menu-content-block {
  flex: 1;
  background-color: var(--bg-dark-secondary);
  border: 1px solid var(--border-gold);
  border-radius: 12px;
  padding: 3rem;
  display: flex;
  flex-direction: column;
  box-shadow: 0 15px 40px rgba(0,0,0,0.6);
  max-height: 650px;
  overflow-y: auto;
}

/* Custom scrollbar for menu text block */
.menu-content-block::-webkit-scrollbar {
  width: 6px;
}
.menu-content-block::-webkit-scrollbar-track {
  background: var(--bg-dark); 
  border-radius: 10px;
}
.menu-content-block::-webkit-scrollbar-thumb {
  background: var(--border-gold); 
  border-radius: 10px;
}
.menu-content-block::-webkit-scrollbar-thumb:hover {
  background: var(--gold-primary); 
}

.menu-image-block {
  flex: 1;
  border: 1px solid var(--border-gold);
  border-radius: 12px;
  overflow: hidden;
  position: relative;
  box-shadow: 0 15px 40px rgba(0,0,0,0.6);
  height: 650px;
}

.menu-image-block img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.8s ease;
}

.menu-row:hover .menu-image-block img {
  transform: scale(1.05);
}

.menu-category-title {
  font-family: var(--font-heading);
  font-size: 2.5rem;
  color: var(--gold-primary);
  margin-top: 0;
  margin-bottom: 2rem;
  text-align: center;
  position: relative;
  text-transform: uppercase;
  letter-spacing: 2px;
}

.menu-category-title::after {
  content: '';
  display: block;
  width: 100px;
  height: 2px;
  background: var(--gold-primary);
  margin: 1.5rem auto 0;
}

.menu-items-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
}

.menu-items-grid.two-col {
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.menu-item-row {
  display: flex;
  flex-direction: column;
}

.menu-item-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 0.3rem;
  border-bottom: 1px dashed rgba(255, 255, 255, 0.2);
  padding-bottom: 0.3rem;
}

.menu-item-name {
  font-family: var(--font-heading);
  font-size: 1.15rem;
  font-weight: 600;
  color: var(--text-light);
}

.menu-item-price {
  font-family: var(--font-body);
  font-weight: 600;
  color: var(--gold-primary);
  font-size: 1.1rem;
}

.menu-item-desc {
  font-size: 0.85rem;
  color: var(--text-muted);
  line-height: 1.4;
  margin-top: 0.3rem;
}

@media (max-width: 992px) {
  .menu-row {
    flex-direction: column !important;
  }
  .menu-image-block {
    height: 350px;
  }
  .menu-content-block {
    padding: 2rem;
    max-height: 500px;
  }
  .menu-items-grid.two-col {
    grid-template-columns: 1fr;
  }
  .menu-tabs-container {
    padding: 2rem 5%;
  }
}
"""

if ".menu-showcase-container {" in css_content:
    parts = css_content.split(".menu-showcase-container {")
    base_css = parts[0]
    final_css = base_css + new_css
    
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(final_css)
    print("CSS replaced successfully.")
else:
    print("Could not find showcase container block.")
