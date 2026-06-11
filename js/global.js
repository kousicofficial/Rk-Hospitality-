// Initialize AOS (Animate on Scroll)
document.addEventListener("DOMContentLoaded", () => {
  if (typeof AOS !== 'undefined') {
    AOS.init({
      once: true,
      offset: 50,
      duration: 600,
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

// WhatsApp Form Submission Logic
document.addEventListener("DOMContentLoaded", () => {
  const forms = document.querySelectorAll('form');
  
  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault(); // Prevent standard submission
      
      // Determine page name
      let pageName = document.body.getAttribute('data-page') || document.title;
      // Format pageName nicely if it's a known data-page attribute
      if (pageName === 'banquet') pageName = 'RK Grande';
      else if (pageName === 'stardom') pageName = 'Stardome';
      else if (pageName === 'regal') pageName = 'RK Regal';
      else if (pageName === 'nexus') pageName = 'RK Nexus';
      else if (pageName === 'gem') pageName = 'GEM Restaurant Royale';
      else if (pageName === 'index') pageName = 'RK Hospitality Home';
      
      let message = `*New Booking Request*\n*From:* ${pageName}\n\n`;
      
      // Get all inputs
      const elements = form.querySelectorAll('input, select, textarea');
      elements.forEach(el => {
        let labelText = '';
        const labelEl = el.previousElementSibling;
        
        if (labelEl && labelEl.tagName.toLowerCase() === 'label') {
          labelText = labelEl.innerText.trim();
        } else if (el.closest('div') && el.closest('div').querySelector('label')) {
          labelText = el.closest('div').querySelector('label').innerText.trim();
        } else {
          labelText = el.getAttribute('name') || el.getAttribute('placeholder') || 'Field';
        }
        
        let val = el.value;
        if (el.tagName.toLowerCase() === 'select' && el.selectedIndex >= 0) {
           val = el.options[el.selectedIndex].text;
        }
        
        if (val) {
          message += `*${labelText}:* ${val}\n`;
        }
      });
      
      const whatsappNumber = "919600624445";
      const encodedMessage = encodeURIComponent(message);
      const whatsappURL = `https://wa.me/${whatsappNumber}?text=${encodedMessage}`;
      
      window.open(whatsappURL, '_blank');
    });
  });
});
