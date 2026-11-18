// Typing animation on the hero
const roles = [
  "Aspiring Data Scientist",
  "Python Programmer",
  "Data Analyst & Visualizer",
  "Generative AI Researcher"
];
const typingEl = document.getElementById("typing");
let roleIdx = 0, charIdx = 0, deleting = false;

function tick() {
  const word = roles[roleIdx];
  typingEl.textContent = word.slice(0, charIdx);
  if (!deleting) {
    if (charIdx < word.length) { charIdx++; setTimeout(tick, 75); }
    else { deleting = true; setTimeout(tick, 1500); }
  } else {
    if (charIdx > 0) { charIdx--; setTimeout(tick, 38); }
    else { deleting = false; roleIdx = (roleIdx + 1) % roles.length; setTimeout(tick, 300); }
  }
}
tick();

// Scroll-reveal animations
const observer = new IntersectionObserver((entries) => {
  entries.forEach((e) => { if (e.isIntersecting) e.target.classList.add("visible"); });
}, { threshold: 0.12 });
document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));

// Mobile menu
const menuBtn = document.getElementById("menuBtn");
const navLinks = document.getElementById("navLinks");
menuBtn.addEventListener("click", () => navLinks.classList.toggle("open"));
navLinks.querySelectorAll("a").forEach((a) =>
  a.addEventListener("click", () => navLinks.classList.remove("open"))
);
