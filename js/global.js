// Initialize AOS (Animate on Scroll)
document.addEventListener("DOMContentLoaded", () => {
  if (typeof AOS !== 'undefined') {
    AOS.init({
      once: true,
      offset: 50,
      duration: 1000,
      easing: 'ease-in-out',
    });
  }

  // Simple clean body fade-in
  document.body.style.opacity = '0';
  document.body.style.transition = 'opacity 0.8s ease';
  setTimeout(() => {
    document.body.style.opacity = '1';
  }, 100);

  // Sticky Header Logic
  const header = document.querySelector('.global-header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth'
        });
      }
    });
  });
});

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

// Mobile Hamburger Menu Logic & CTA Injection
document.addEventListener("DOMContentLoaded", () => {
  const header = document.querySelector('.global-header');
  const navLinks = document.querySelector('.nav-links');
  
  if (header && navLinks && !document.querySelector('.hamburger')) {
    // Inject hamburger
    const hamburger = document.createElement('div');
    hamburger.className = 'hamburger';
    hamburger.innerHTML = '<span></span><span></span><span></span>';
    header.appendChild(hamburger);
    
    // Clone CTA buttons into the mobile menu dropdown
    const ctas = document.querySelectorAll('.header-cta');
    ctas.forEach(cta => {
      // Only clone if it's a direct child of header (prevents infinite loop if run multiple times)
      if (cta.parentElement === header) {
        const ctaClone = cta.cloneNode(true);
        const li = document.createElement('li');
        li.className = 'mobile-only-cta';
        li.appendChild(ctaClone);
        navLinks.appendChild(li);
        
        // Re-attach modal listener to the cloned "Book Now" button
        if (ctaClone.classList.contains('btn-book-now')) {
          ctaClone.addEventListener('click', (e) => {
            e.preventDefault();
            const modal = document.getElementById("bookingModal");
            if (modal) {
              modal.classList.add("show");
              document.body.style.overflow = "hidden";
              // Close mobile menu when opening modal
              hamburger.classList.remove('active');
              navLinks.classList.remove('active');
            }
          });
        }
      }
    });
    
    // Toggle logic
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('active');
      navLinks.classList.toggle('active');
    });
    
    // Close menu when clicking a standard link
    navLinks.querySelectorAll('a:not(.header-cta)').forEach(link => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navLinks.classList.remove('active');
      });
    });
  }
});
