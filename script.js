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

const roleText = "Model | Model Judge | Event Organizer | Trainer & Team Builder";
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


// HERO SLIDER LOGIC
const slides = document.querySelectorAll(".hero-bg");
let currentSlide = 0;
if(slides.length > 0) {
  setInterval(() => {
    slides[currentSlide].classList.remove("active");
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add("active");
  }, 4000);
}

// AUTO COUNTER LOGIC
const countEls = document.querySelectorAll('.auto-count');
if (countEls.length > 0) {
    const ob = new IntersectionObserver(entries => {
        entries.forEach(e => {
            if(e.isIntersecting) {
                const el = e.target;
                const target = +el.getAttribute('data-target');
                let count = 0;
                let inc = Math.ceil(target / 40);
                let timer = setInterval(() => {
                    count += inc;
                    if(count >= target) { el.innerText = target; clearInterval(timer); }
                    else { el.innerText = count; }
                }, 40);
                ob.unobserve(el);
            }
        });
    });
    countEls.forEach(el => ob.observe(el));
}

// HORIZONTAL GALLERY AUTOSCROLL
const gTracks = document.querySelectorAll('.gallery-track');
let gDirs = [1, -1, 1]; // alternating directions
let gPaused = false;
let gSpeed = 1.2;

// Auto-push the middle track to the right side so it scrolls left
if(gTracks[1]) {
    setTimeout(() => { gTracks[1].scrollLeft = gTracks[1].scrollWidth; }, 500);
}

function slideG() {
    if (!gPaused) {
        gTracks.forEach((track, i) => {
            if (track.scrollWidth > track.clientWidth) {
                track.scrollLeft += (gSpeed * gDirs[i]);
                if (track.scrollLeft >= (track.scrollWidth - track.clientWidth - 1)) {
                    gDirs[i] = -1;
                } else if (track.scrollLeft <= 1) {
                    gDirs[i] = 1;
                }
            }
        });
    }
    requestAnimationFrame(slideG);
}
requestAnimationFrame(slideG);

gTracks.forEach(t => {
    t.addEventListener('mouseenter', () => gPaused = true);
    t.addEventListener('mouseleave', () => gPaused = false);
    
    // Convert vertical mouse wheel to horizontal scroll inside these tracks
    t.addEventListener('wheel', (e) => {
        gPaused = true;
        t.scrollLeft += e.deltaY * 2;
        e.preventDefault();
        // Resume auto scroll after scrolling
        clearTimeout(t.resumeTimer);
        t.resumeTimer = setTimeout(() => { gPaused = false; }, 1000);
    });
});

// MOBILE NAV TOGGLE
const mobileToggle = document.querySelector('.mobile-nav-toggle');
const siteNav = document.querySelector('.site-nav');
const navLinksAll = document.querySelectorAll('.site-nav a');

if (mobileToggle && siteNav) {
    mobileToggle.addEventListener('click', () => {
        mobileToggle.classList.toggle('is-active');
        siteNav.classList.toggle('is-open');
        document.body.style.overflow = siteNav.classList.contains('is-open') ? 'hidden' : '';
    });

    navLinksAll.forEach(link => {
        link.addEventListener('click', () => {
            mobileToggle.classList.remove('is-active');
            siteNav.classList.remove('is-open');
            document.body.style.overflow = '';
        });
    });
}
