document.addEventListener("DOMContentLoaded", () => {
  // Initialize AOS
  AOS.init({
    once: true,
    offset: 100,
  });

  // Register ScrollTrigger
  gsap.registerPlugin(ScrollTrigger);

  // Intro completion trigger
  window.addEventListener('introComplete', () => {
    // Reveal Hero Title
    gsap.from(".hero-title", {
      opacity: 0,
      scale: 1.1,
      filter: "blur(20px)",
      duration: 2.5,
      ease: "power3.out"
    });
  });

  // Background Parallax for Hero & Food Sequences
  const bgParallaxItems = document.querySelectorAll('.gs-parallax-bg video, .gs-parallax-bg img');
  bgParallaxItems.forEach(item => {
    gsap.to(item, {
      yPercent: 20,
      ease: "none",
      scrollTrigger: {
        trigger: item.closest('section') || item.closest('.food-sequence'),
        start: "top bottom",
        end: "bottom top",
        scrub: true
      }
    });
  });

  // Form label interaction
  const inputs = document.querySelectorAll('.input-group input, .input-group select');
  inputs.forEach(input => {
    // Initial check
    if (input.value.trim() !== "") input.classList.add('has-value');

    input.addEventListener('blur', () => {
      if (input.value.trim() !== "") {
        input.classList.add('has-value');
      } else {
        input.classList.remove('has-value');
      }
    });
    
    input.addEventListener('change', () => {
      if (input.value.trim() !== "") {
        input.classList.add('has-value');
      }
    });
  });
});
