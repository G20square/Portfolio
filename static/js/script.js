// Custom Scripts

document.addEventListener('DOMContentLoaded', function () {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Skill Bar Animation on Scroll
    // Skill Bar Animation on Scroll
    const skillCards = document.querySelectorAll('.skill-card');
    if (skillCards.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    // Staggered animation for cards
                    setTimeout(() => {
                        entry.target.classList.add('visible');
                        const progressBar = entry.target.querySelector('.skill-progress');
                        if (progressBar) {
                            const width = progressBar.getAttribute('data-width');
                            progressBar.style.width = width + '%';
                        }
                    }, index * 100); // 100ms delay between each card

                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.2 });

        skillCards.forEach(card => observer.observe(card));
    }
});


