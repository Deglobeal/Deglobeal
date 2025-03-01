alert("Welcome to Deglobeal profile page more mortifications are yet to come, feel free to send me an email")

document.addEventListener('DOMContentLoaded', () => {
    const verticalNav = document.querySelector('.navi_bar_vertical');
    
    // Toggle nav on click
    verticalNav.addEventListener('click', (e) => {
        e.stopPropagation();
        verticalNav.classList.toggle('active');
    });

    // Close nav when clicking outside
    document.addEventListener('click', (e) => {
        if (!verticalNav.contains(e.target)) {
            verticalNav.classList.remove('active');
        }
    });

    // Optional: Close nav when clicking links
    const navLinks = document.querySelectorAll('.navi_bar_vertical a');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            verticalNav.classList.remove('active');
        });
    });
});

