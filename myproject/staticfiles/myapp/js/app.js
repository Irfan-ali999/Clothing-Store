let circle = document.querySelector('.circle');
let slider = document.querySelector('.slider');
let list = document.querySelector('.list');
let prev = document.getElementById('prev');
let next = document.getElementById('next');
let items = document.querySelectorAll('.list .item');
let count = items.length;
let active = 1;
let leftTransform = 0;
let width_item = items[active].offsetWidth;

// Automatic sliding interval (in milliseconds)
const slideInterval = 3000; // Adjust the time between slides (e.g., 3000ms = 3 seconds)

// Manual navigation
next.onclick = () => {
    active = active >= count - 1 ? count - 1 : active + 1;
    runCarousel();
    resetAutoSlide(); // Reset auto-slide timer after manual navigation
};

prev.onclick = () => {
    active = active <= 0 ? active : active - 1;
    runCarousel();
    resetAutoSlide(); // Reset auto-slide timer after manual navigation
};

// Carousel logic
function runCarousel() {
    prev.style.display = active === 0 ? 'none' : 'block';
    next.style.display = active === count - 1 ? 'none' : 'block';

    let old_active = document.querySelector('.item.active');
    if (old_active) old_active.classList.remove('active');
    items[active].classList.add('active');

    leftTransform = width_item * (active - 1) * -1;
    list.style.transform = `translateX(${leftTransform}px)`;
}
runCarousel();

// Automatic sliding
let autoSlide = setInterval(() => {
    active = active >= count - 1 ? 0 : active + 1;
    runCarousel();
}, slideInterval);

// Reset auto-slide timer after manual interaction
function resetAutoSlide() {
    clearInterval(autoSlide); // Clear the existing interval
    autoSlide = setInterval(() => {
        active = active >= count - 1 ? 0 : active + 1;
        runCarousel();
    }, slideInterval);
}

// Set Text on a Circle
let textCircle = circle.innerText.split('');
circle.innerText = '';
textCircle.forEach((value, key) => {
    let newSpan = document.createElement('span');
    newSpan.innerText = value;
    let rotateThisSpan = (360 / textCircle.length) * (key + 1);
    newSpan.style.setProperty('--rotate', rotateThisSpan + 'deg');
    circle.appendChild(newSpan);
});


function scrollToSection(ps1) {
    const section = document.querySelector(ps1);
    if (ps1) {
        section.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

function scrollToSection(ps3) {
    const section = document.querySelector(ps3);
    if (ps3) {
        section.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

function scrollToSection(Home) {
    const section = document.querySelector(Home);
    if (Home) {
        section.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

function scrollToSection(ps4) {
    const section = document.querySelector(ps4);
    if (ps4) {
        section.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

function scrollToSection(ps2) {
    const section = document.querySelector(ps2);
    if (ps2) {
        section.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}
