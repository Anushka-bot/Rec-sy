$(window).scroll(function() {
    if ($(document).scrollTop()>180) {
        $('.navbar').addClass('nav-bg');
        console.log(`OK`);
    } else {
        $('.navbar').removeClass('nav-bg');
    }
});
