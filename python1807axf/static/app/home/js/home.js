$(function () {
    initTop()
    initMenu()
})

function initTop() {
    var mySwiper = new Swiper('#topSwiper', {
        loop: true,
        // 如果需要分页器
        pagination: '.swiper-pagination',
        autoplay:2000,
    })
}

function initMenu() {
    var mySwiper = new Swiper('#swiperMenu', {
        //显示多少条目
        slidesPerView: 3,
    })
}