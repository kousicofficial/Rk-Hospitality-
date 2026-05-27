document.addEventListener("DOMContentLoaded", () => {
  // Initialize AOS
  AOS.init({
    once: true,
    offset: 100,
  });

  // Register ScrollTrigger
  gsap.registerPlugin(ScrollTrigger);

  window.addEventListener('introComplete', () => {
    // Trigger Confetti upon intro completion
    fireConfetti();
  });

  // Background Parallax
  const bgParallaxItems = document.querySelectorAll('.gs-parallax-bg img');
  bgParallaxItems.forEach(item => {
    gsap.to(item, {
      yPercent: 15,
      ease: "none",
      scrollTrigger: {
        trigger: item.closest('section') || item.closest('.editorial-row'),
        start: "top bottom",
        end: "bottom top",
        scrub: true
      }
    });
  });

  // Confetti Logic
  function fireConfetti() {
    const duration = 3000;
    const end = Date.now() + duration;

    (function frame() {
      confetti({
        particleCount: 5,
        angle: 60,
        spread: 55,
        origin: { x: 0 },
        colors: ['#D4AF37', '#E6C77E', '#ffffff']
      });
      confetti({
        particleCount: 5,
        angle: 120,
        spread: 55,
        origin: { x: 1 },
        colors: ['#D4AF37', '#E6C77E', '#ffffff']
      });

      if (Date.now() < end) {
        requestAnimationFrame(frame);
      }
    }());
  }

  // Form handling (shared logic)
  const inputs = document.querySelectorAll('.input-group input, .input-group select');
  inputs.forEach(input => {
    if (input.value.trim() !== "") input.classList.add('has-value');
    input.addEventListener('blur', () => {
      if (input.value.trim() !== "") {
        input.classList.add('has-value');
      } else {
        input.classList.remove('has-value');
      }
    });
    input.addEventListener('change', () => {
      if (input.value.trim() !== "") input.classList.add('has-value');
    });
  });
});
