// function to open and close side navigation
function openNav() {
    document.getElementById("mySidenav").style.width = "200px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

// function to listen for scroll event and change
// donation banner to fixed after 100px Y-axis
const setScrollListener = () => {
    document.addEventListener('scroll', event => {
        const cta = document.querySelector('#ctaBanner');

        if (window.scrollY >= 100) {
            cta.style.position = 'fixed'
        } else {
            cta.style.position = 'static';
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
