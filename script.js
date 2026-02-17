document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    // Mobile Menu Toggle
    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        hamburger.classList.toggle('active'); // Optional: Add animation to hamburger
    });

    // Smooth Scroll for Navigation Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            navLinks.classList.remove('active'); // Close mobile menu on click

            const targetSection = document.querySelector(this.getAttribute('href'));
            const headerOffset = 80; // Adjust for fixed header
            const elementPosition = targetSection.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
        });
    });

    // Skill Bar Animation
    const skillSection = document.getElementById('skills');
    const skillBars = document.querySelectorAll('.progress-line span');

    function showProgress() {
        skillBars.forEach(progressBar => {
            const value = progressBar.parentElement.getAttribute('data-percent');
            progressBar.style.width = value;
        });
    }

    function hideProgress() {
        skillBars.forEach(progressBar => {
            progressBar.style.width = 0;
        });
    }

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                showProgress();
            } else {
                hideProgress();
            }
        });
    }, { threshold: 0.2 });

    if (skillSection) {
        observer.observe(skillSection);
    }

    // Active Link Highlighting
    const sections = document.querySelectorAll('section');
    const navItems = document.querySelectorAll('.nav-links a');

    window.addEventListener('scroll', () => {
        let current = '';
        const scrollY = window.pageYOffset;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            const headerOffset = 100; // Adjust slightly larger than fixed header

            if (scrollY >= (sectionTop - headerOffset)) {
                current = section.getAttribute('id');
            }
        });

        navItems.forEach(item => {
            item.classList.remove('active');
            if (item.getAttribute('href').includes(current)) {
                item.classList.add('active');
            }
        });
    });
});
