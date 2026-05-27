import os

css_code = """
/* =========================================
   NEW MENU SHOWCASE (ZIG-ZAG)
   ========================================= */
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

.menu-image-block img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 1s ease;
}

.menu-row:hover .menu-image-block img {
  transform: scale(1.05);
}

.menu-category-title {
  font-family: var(--font-heading);
  font-size: 3.5rem;
  color: var(--gold-primary);
  margin-bottom: 3rem;
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

/* Call to action at the end */
.menu-cta-section {
  text-align: center;
  padding: 8rem 5%;
  background: linear-gradient(to bottom, var(--bg-dark), var(--bg-dark-secondary));
}

.menu-cta-text {
  font-family: var(--font-heading);
  font-size: 3rem;
  color: var(--gold-primary);
  line-height: 1.4;
  max-width: 900px;
  margin: 0 auto 1.5rem;
  font-style: italic;
}

.menu-cta-sub {
  font-size: 1.2rem;
  color: var(--text-light);
  letter-spacing: 2px;
  text-transform: uppercase;
}

@media (max-width: 992px) {
  .menu-row {
    flex-direction: column !important;
  }
  .menu-image-block {
    height: 40vh;
  }
  .menu-content-block {
    padding: 3rem 2rem;
  }
  .menu-items-grid.two-col {
    grid-template-columns: 1fr;
  }
  .menu-category-title {
    font-size: 2.5rem;
  }
  .menu-cta-text {
    font-size: 2rem;
  }
}
"""

css_file = r"d:\Rk hospitality\css\gem.css"
with open(css_file, "a", encoding="utf-8") as f:
    f.write(css_code)
    
print("CSS appended.")
