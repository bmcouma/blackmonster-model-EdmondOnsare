const revealElements = document.querySelectorAll(".reveal");
const galleryCards = document.querySelectorAll(".gallery-card");
const filterButtons = document.querySelectorAll(".filter-btn");
const lightbox = document.getElementById("lightbox");
const lightboxImage = lightbox.querySelector(".lightbox-image");
const lightboxClose = lightbox.querySelector(".lightbox-close");
const stickyBookButton = document.querySelector(".sticky-book");
const testimonialCards = document.querySelectorAll(".testimonial-card");
const testimonialDots = document.querySelectorAll(".dot");
const sections = document.querySelectorAll("main section[id]");
const navLinks = document.querySelectorAll('.site-nav a[href^="#"]');
const typedRole = document.getElementById("typed-role");

const revealObserver = new IntersectionObserver(
  (entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.15,
    rootMargin: "0px 0px -50px 0px"
  }
);

revealElements.forEach((el) => revealObserver.observe(el));

filterButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const filter = button.dataset.filter;

    filterButtons.forEach((btn) => btn.classList.remove("is-active"));
    button.classList.add("is-active");

    galleryCards.forEach((card) => {
      const category = card.dataset.category;
      const shouldShow = filter === "all" || category === filter;
      card.style.display = shouldShow ? "block" : "none";
    });
  });
});

document.querySelectorAll(".gallery-overlay").forEach((overlay) => {
  overlay.addEventListener("click", () => {
    const src = overlay.dataset.full;
    lightboxImage.src = src;
    lightbox.classList.add("is-open");
    lightbox.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  });
});

function closeLightbox() {
  lightbox.classList.remove("is-open");
  lightbox.setAttribute("aria-hidden", "true");
  lightboxImage.src = "";
  document.body.style.overflow = "";
}

lightboxClose.addEventListener("click", closeLightbox);
lightbox.addEventListener("click", (event) => {
  if (event.target === lightbox) {
    closeLightbox();
  }
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && lightbox.classList.contains("is-open")) {
    closeLightbox();
  }
});

document.querySelectorAll('[data-scroll-to], a[href^="#"]').forEach((element) => {
  element.addEventListener("click", (event) => {
    const selector = element.getAttribute("data-scroll-to") || element.getAttribute("href");
    if (!selector || selector === "#") return;

    const target = document.querySelector(selector);
    if (!target) return;

    event.preventDefault();
    target.scrollIntoView({ behavior: "smooth", block: "start" });
  });
});

stickyBookButton.addEventListener("click", () => {
  const contactSection = document.querySelector("#contact");
  if (contactSection) {
    contactSection.scrollIntoView({ behavior: "smooth", block: "start" });
  }
});

document.querySelector(".contact-form")?.addEventListener("submit", (event) => {
  event.preventDefault();
});

let testimonialIndex = 0;
let testimonialTimer;

function setActiveTestimonial(index) {
  testimonialCards.forEach((card, cardIndex) => {
    card.classList.toggle("is-active", cardIndex === index);
  });
  testimonialDots.forEach((dot, dotIndex) => {
    dot.classList.toggle("is-active", dotIndex === index);
  });
}

function startTestimonialAutoplay() {
  if (!testimonialCards.length) return;
  testimonialTimer = setInterval(() => {
    testimonialIndex = (testimonialIndex + 1) % testimonialCards.length;
    setActiveTestimonial(testimonialIndex);
  }, 4200);
}

testimonialDots.forEach((dot, index) => {
  dot.addEventListener("click", () => {
    testimonialIndex = index;
    setActiveTestimonial(testimonialIndex);
    clearInterval(testimonialTimer);
    startTestimonialAutoplay();
  });
});

setActiveTestimonial(testimonialIndex);
startTestimonialAutoplay();

document.querySelector(".testimonial-slider")?.addEventListener("mouseenter", () => {
  clearInterval(testimonialTimer);
});

document.querySelector(".testimonial-slider")?.addEventListener("mouseleave", () => {
  startTestimonialAutoplay();
});

const navObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      const id = entry.target.getAttribute("id");
      navLinks.forEach((link) => {
        const isActive = link.getAttribute("href") === `#${id}`;
        link.classList.toggle("is-active", isActive);
      });
    });
  },
  { threshold: 0.45 }
);

sections.forEach((section) => navObserver.observe(section));

const roleText = "Model | Model Judge | Event Organizer | Trainer AND TEAM BUILDER";
let roleIdx = 0;
let deleting = false;

function typeRoleLoop() {
  if (!typedRole) return;
  if (!deleting) {
    roleIdx += 1;
    typedRole.textContent = roleText.slice(0, roleIdx);
    if (roleIdx >= roleText.length) {
      deleting = true;
      setTimeout(typeRoleLoop, 1600);
      return;
    }
  } else {
    roleIdx -= 1;
    typedRole.textContent = roleText.slice(0, roleIdx);
    if (roleIdx <= 0) {
      deleting = false;
    }
  }
  setTimeout(typeRoleLoop, deleting ? 26 : 56);
}

if (typedRole) {
  typedRole.textContent = "";
  typeRoleLoop();
}
