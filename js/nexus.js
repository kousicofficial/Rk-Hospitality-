document.addEventListener("DOMContentLoaded", () => {
  AOS.init({ once: true, offset: 100 });
  gsap.registerPlugin(ScrollTrigger);

  window.addEventListener('introComplete', () => {
    gsap.from(".hero-title", {
      opacity: 0,
      scale: 1.05,
      filter: "blur(10px)",
      duration: 2.5,
      ease: "power3.out"
    });
  });

  const bgParallaxItems = document.querySelectorAll('.gs-parallax-bg img');
  bgParallaxItems.forEach(item => {
    gsap.to(item, {
      yPercent: 15,
      ease: "none",
      scrollTrigger: {
        trigger: item.closest('section') || item.closest('.nexus-split-layout'),
        start: "top bottom",
        end: "bottom top",
        scrub: true
      }
    });
  });

  gsap.to(".gs-parallax-grid", {
    rotationX: 45,
    ease: "none",
    scrollTrigger: {
      trigger: ".nexus-hero",
      start: "top top",
      end: "bottom top",
      scrub: true
    }
  });

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
