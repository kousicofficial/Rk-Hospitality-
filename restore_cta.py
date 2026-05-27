import os

css_path = r"d:\Rk hospitality\css\gem.css"

cta_css = """
/* =========================================
   CALL TO ACTION
   ========================================= */
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
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write(cta_css)

print("CTA CSS restored successfully.")
