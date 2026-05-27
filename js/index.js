document.addEventListener("DOMContentLoaded", () => {
  // Initialize AOS
  AOS.init({
    once: true,
    offset: 100,
  });

  // Register ScrollTrigger
  gsap.registerPlugin(ScrollTrigger);

  // We wait for the intro to complete before animating the hero typography
  window.addEventListener('introComplete', () => {
    gsap.from(".hero-title", {
      opacity: 0,
      y: 50,
      filter: "blur(10px)",
      duration: 2,
      ease: "power3.out"
    });
    
    gsap.from(".hero-subtitle", {
      opacity: 0,
      y: 20,
      duration: 1.5,
      delay: 0.5,
      ease: "power2.out"
    });
  });

  // Parallax Hero Video
  gsap.to(".parallax-hero", {
    yPercent: 30,
    ease: "none",
    scrollTrigger: {
      trigger: ".cinematic-hero",
      start: "top top",
      end: "bottom top",
      scrub: true
    }
  });

  // Image Reveal Masks
  const revealMasks = document.querySelectorAll('.img-reveal-mask');
  revealMasks.forEach(mask => {
    gsap.to(mask, {
      scaleX: 0,
      ease: "power3.inOut",
      scrollTrigger: {
        trigger: mask.parentElement,
        start: "top 80%",
        end: "center center",
        scrub: 1
      }
    });
  });

  // GS Parallax items (Glassmorphism overlap image)
  const parallaxItems = document.querySelectorAll('.gs-parallax');
  parallaxItems.forEach(item => {
    gsap.to(item, {
      yPercent: 15,
      ease: "none",
      scrollTrigger: {
        trigger: item.parentElement,
        start: "top bottom",
        end: "bottom top",
        scrub: true
      }
    });
  });

  // Scale images slowly on scroll
  const scaleItems = document.querySelectorAll('.gs-scale');
  scaleItems.forEach(item => {
    gsap.to(item, {
      scale: 1.15,
      ease: "none",
      scrollTrigger: {
        trigger: item.parentElement,
        start: "top bottom",
        end: "bottom top",
        scrub: true
      }
    });
  });
});
