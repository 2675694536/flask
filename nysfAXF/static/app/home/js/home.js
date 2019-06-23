$(function () {
    //顶部轮播图
    initTopSwiper()

//    菜单轮播图
    initMenuSwiper()

})

function initTopSwiper() {
    var mySwiper = new Swiper('#topSwiper', {
        loop: true,
        autoplay: 4000
    })
}

function initMenuSwiper() {
    var mySwiper = new Swiper('#swiperMenu', {
        slidesPerView: 3,
    })
}