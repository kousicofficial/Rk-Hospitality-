import os

css_path = r"d:\Rk hospitality\css\global.css"

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Add explicit centering fixes for the modal on mobile
modal_centering_fix = """
/* Fix: Explicit centering for Popup Modal on Mobile */
@media (max-width: 768px) {
  .booking-modal-overlay {
    padding: 1rem !important; /* Reduce padding that might push the content */
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
  }
  
  .booking-modal-content {
    margin: 0 auto !important; /* Fallback centering if flex fails */
    left: 0 !important;
    right: 0 !important;
    width: 90% !important; /* Leave a small predictable gap */
    max-width: 400px !important; /* Prevent it from stretching weirdly */
    padding: 2rem 1.5rem !important;
    transform: none !important; /* Remove translateY which can cause layout shifts on mobile */
  }
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write(modal_centering_fix)

print("Modal mobile centering fixed successfully.")
