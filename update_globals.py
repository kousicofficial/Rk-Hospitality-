import os

base_dir = r"d:\Rk hospitality"

# 1. Update global.css
css_path = os.path.join(base_dir, "css", "global.css")
with open(css_path, "a", encoding="utf-8") as f:
    modal_css = """
/* =========================================
   POPUP MODAL STYLES
   ========================================= */
.booking-modal-overlay {
  display: none;
  position: fixed;
  z-index: 9999;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(1, 10, 6, 0.85);
  backdrop-filter: blur(8px);
  overflow-y: auto;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  opacity: 0;
  transition: opacity 0.4s ease;
}

.booking-modal-overlay.show {
  display: flex;
  opacity: 1;
}

.booking-modal-content {
  position: relative;
  background: var(--bg-dark);
  border: 1px solid var(--gold-primary);
  padding: 4rem;
  width: 100%;
  max-width: 800px;
  transform: translateY(-50px);
  transition: transform 0.4s ease;
  box-shadow: 0 25px 50px rgba(0,0,0,0.8);
}

.booking-modal-overlay.show .booking-modal-content {
  transform: translateY(0);
}

.close-modal {
  position: absolute;
  top: 20px;
  right: 30px;
  color: var(--text-muted);
  font-size: 2.5rem;
  font-weight: bold;
  cursor: pointer;
  transition: color 0.3s ease;
}

.close-modal:hover {
  color: var(--gold-primary);
}

.btn-book-now:hover {
  background: var(--gold-hover) !important;
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
}

@media (max-width: 768px) {
  .booking-modal-content {
    padding: 2.5rem 1.5rem;
  }
}
"""
    f.write(modal_css)

# 2. Update global.js
js_path = os.path.join(base_dir, "js", "global.js")
with open(js_path, "a", encoding="utf-8") as f:
    modal_js = """
// Modal Logic
document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("bookingModal");
  const bookBtns = document.querySelectorAll(".btn-book-now");
  const closeBtn = document.querySelector(".close-modal");

  if (modal && bookBtns.length > 0) {
    // Open Modal
    bookBtns.forEach(btn => {
      btn.addEventListener("click", (e) => {
        e.preventDefault();
        modal.classList.add("show");
        document.body.style.overflow = "hidden"; // Prevent background scrolling
      });
    });

    // Close Modal via X button
    if (closeBtn) {
      closeBtn.addEventListener("click", () => {
        modal.classList.remove("show");
        document.body.style.overflow = "auto";
      });
    }

    // Close Modal via outside click
    window.addEventListener("click", (e) => {
      if (e.target === modal) {
        modal.classList.remove("show");
        document.body.style.overflow = "auto";
      }
    });
  }
});
"""
    f.write(modal_js)

print("Global CSS and JS updated successfully.")
