// ========= SWIPER JS CAROUSELS ========

// <!-- Initialize Swiperjs --> 
// home-page: main carousel
let homeSwiper = new Swiper('.swiper-container.main-swiper', {
    effect: 'coverflow',
    grabCursor: true,
    centeredSlides: true,
    loop: true,
    slidesPerView: 'auto',
    coverflowEffect: {
        rotate: 50,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows: true,
    },
    // autoplay: {
    //     delay: 4500,
    //     disableOnInteraction: false,
    // },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
});
// home-page: about section carousel
let aboutSwiper = new Swiper('.swiper-container.about-swiper', {
    effect: 'cube',
    grabCursor: true,
    loop: true,
    cubeEffect: {
        shadow: true,
        slideShadows: true,
        shadowOffset: 20,
        shadowScale: 0.94,
    },
    //     autoplay: {
    //     delay: 2000,
    //     disableOnInteraction: false,
    // },
    pagination: false,
});
// home-page: featured projects carousel
let featuredProjectSwiper = new Swiper('.swiper-container.featured-project-swiper', {
    slidesPerView: 1,
    spaceBetween: 10,
    init: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    loop: true,
    breakpoints: {
        640: {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        768: {
            slidesPerView: 4,
            spaceBetween: 40,
        },
        1024: {
            slidesPerView: 5,
            spaceBetween: 50,
        },
    }
});
// home-page: featured blogs carousel
let featuredBlogSwiper = new Swiper('.swiper-container.featured-blog-swiper', {
    slidesPerView: 1,
    spaceBetween: 10,
    init: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    loop: true,
    breakpoints: {
        640: {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        768: {
            slidesPerView: 4,
            spaceBetween: 40,
        },
        1024: {
            slidesPerView: 5,
            spaceBetween: 50,
        },
    }
});
// END SWIPER JS CAROUSELS

// function to open and close side navigation
function openNav() {
    document.getElementById("sideNav").style.width = "75%";
}

function closeNav() {
    document.getElementById("sideNav").style.width = "0";
}

// function to listen for scroll events 
const setScrollListener = () => {
    document.addEventListener('scroll', event => {
        // change donation banner to fixed after 100px Y-axis
        const cta = document.querySelector('#ctaBanner');
        if (window.scrollY >= 100) {
            cta.style.position = 'fixed'
        } else {
            cta.style.position = 'static';
        }
        // show back-to-top button on scroll
        const btt = document.querySelector('#back-to-top');
        if (window.scrollY >= 300) {
            btt.style.display = 'grid';
        } else {
            btt.style.display = 'none';
        }
    });
}

// close donation banner on button click and store in local 
const closeBanner = () => {
    const cta = document.querySelector('#ctaBanner');
    const closeButton = document.querySelector('#closeBanner');
    closeButton.onclick = () => {
        cta.style.display = 'none';
        localStorage.setItem('show-cta-banner', JSON.stringify({
            show: false
        }));
    };
}

// check local storage and if banner close instance is there,
// keep until page refresh
// NB - This function MUST come last
function init() {
    const cta = document.querySelector('#ctaBanner');

    // check localStorage for banner
    if (localStorage.getItem('show-cta-banner')) {
        const showBanner = JSON.parse(localStorage.getItem('show-cta-banner'));

        // check whether to show banner or not
        if (!showBanner.show) cta.style.display = 'none';
        // do show banner
        else {
            setScrollListener();
            closeBanner();
        };
    }
    // if not there set into localStorage
    else {
        localStorage.setItem('show-cta-banner', JSON.stringify({
            show: true
        }))
        setScrollListener();
        closeBanner();
    }

    window.onbeforeunload = () => {
        localStorage.setItem('show-cta-banner', JSON.stringify({
            show: true
        }));
    }
}
init();