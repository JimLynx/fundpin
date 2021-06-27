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
    autoplay: {
        delay: 4500,
        disableOnInteraction: false,
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
        renderBullet: function (index, className) {
            if (index < 8) {
                return '<span class="' + className + '">' + (index + 1) + '</span>';
            }
            return '';
        }
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
    pagination: false,
});

// home-page: featured projects carousel
let featuredProjectSwiper = new Swiper('.swiper-container.featured-project-swiper', {
    slidesPerView: 1,
    spaceBetween: 0,
    init: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: false,
        renderBullet: function (index, className) {
            if (index < 8) {
                return '<span class="' + className + '">' + (index + 1) + '</span>';
            }
            return '';
        }
    },
    loop: true,
    autoplay: {
        delay: 2000,
        disableOnInteraction: false,
    },
    breakpoints: {
        576: {
            slidesPerView: 2,
        },
        768: {
            slidesPerView: 3,
        },
        1024: {
            slidesPerView: 4,
        },
        1200: {
            slidesPerView: 5,
        },
    },
});

// home-page: featured blogs carousel
let featuredBlogSwiper = new Swiper('.swiper-container.featured-blog-swiper', {
    slidesPerView: 1,
    spaceBetween: 10,
    init: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
        renderBullet: function (index, className) {
            if (index < 8) {
                return '<span class="' + className + '">' + (index + 1) + '</span>';
            }
            return '';
        }
    },
    loop: true,
    autoplay: {
        delay: 2000,
        disableOnInteraction: false,
    },
    breakpoints: {
        575: {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        768: {
            slidesPerView: 3,
            spaceBetween: 40,
        },
        1024: {
            slidesPerView: 4,
            spaceBetween: 50,
        },
        1200: {
            slidesPerView: 5,
            spaceBetween: 50,
        },
    }
});