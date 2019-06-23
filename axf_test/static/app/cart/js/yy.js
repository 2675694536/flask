$(function () {

    //购物车的加数量
    $(".addshop").click(function () {
        //找到所有当前元素的父标签是li的元素
        var li = $(this).parents("li");
        //拿到li的对应的id值
        var cartid = $(this).parents("li").attr("id");

        //通过getJSON方法请求服务器
        $.getJSON('/addshop/', {"cartid": cartid}, function (data) {
            if (data["status"] == 200) {
                //如果状态码为200  通过li找到span标签 然后将span标签中的内容进行修改
                li.find("span").last().html(data["gnum"])
            }
        })
    });


    //购物车减数量
    $(".subshop").click(function () {
        //找到所有当前元素的父标签是li的元素
        var li = $(this).parents("li");
        //拿到li的对应的id值
        var cartid = $(this).parents("li").attr("id");

        //通过getJSON方法请求服务器
        $.getJSON('/subshop/', {"cartid": cartid}, function (data) {
            if (data["gnum"] == 0) {
                li.remove()
            } else {
                //如果状态码为200  通过li找到span标签 然后将span标签中的内容进行修改
                li.find("span").last().html(data["gnum"])
            }
        })
    })

    $(".is_choosed").click(function () {
        var li = $(this).parents("li");
        var cartid = $(this).parents("li").attr("id");
        var all=$('.all_select')
        var span=$(this)
        var span1=span.html()

        $.getJSON('/change_choose_statu/',{'span1':span1,'cartid':cartid},function (data) {
            if(data['status']==='200'){
                span.html('√');}
            if(data['all']){
                    all.html('√')
            }
             if (data['status']==='400'){
                span.html('');
                all.html('')
            }
        })

    })
    $('.all_select').click(function () {
        var cart=$('.is_choosed')
        var span=$(this)
        var span1=span.html()
        $.getJSON('/all_select/',{'span1':span1},function (data) {if (data['status'] === '200'){
                span.html('√');
                cart.html('√');
            }else if (data['status'] === '404'){
                span.html('');
                cart.html('')
            }
        })
    })
})