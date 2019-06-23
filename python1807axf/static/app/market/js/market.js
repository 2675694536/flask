$(function () {
    $("#all_types").click(function () {
        $("#type_container").show()
        $("#all_types_logo").removeClass("glyphicon glyphicon-chevron-down").addClass("glyphicon glyphicon-chevron-up")
        $("#sort_container").hide()
        $("#multiple_sort_logo").removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down")

    })

    $("#type_container").click(function () {
        $(this).hide()
        $("#all_types_logo").removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down")
    })


    $("#multiple_sort").click(function () {
        $("#sort_container").show()
        $("#multiple_sort_logo").removeClass("glyphicon glyphicon-chevron-down").addClass("glyphicon glyphicon-chevron-up")
        $("#type_container").hide()
        $("#all_types_logo").removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down")
    })

    $("#sort_container").click(function () {
        $(this).hide()
        $("#multiple_sort_logo").removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down")
    })

//    1.先拿到传递过来的商品ID
//    2.将商品ID传递到服务器端
//    3.取回服务器段返回的数据
//    根据返回的数据进行标签的重定义

    //这个是增加
    $(".addcart").click(function () {
        //拿到传递过来的商品id
        var goodid = $(this).attr("id")
        //拿到当前的标签名
        var span = $(this)

        //通过getJson方法将数据传递给服务器,getJson默认是get传参4
        //function(data){}这个参数是后台服务器的回调接口  也就是后台给我们返回的数据
        //getJson返回的一定是Json数据
        $.getJSON('/app/addcart/',{"goodid":goodid},function (data) {
            //如果状态吗为900,就让他跳转到登录界面
            if (data["status"] == "900") {
                //target参数  表示是新打开一个窗口还是在原窗口
                window.open("/app/login/",target = "_self")
            //    如果为200  就去往span标签里面设置数据库中对应的值
            }else if (data["status"] == "200") {
                //这一步就是取这是span标签的值
                span.prev().html(data["g_num"])
            }
        })
    })


     //这个是删除
    $(".subcart").click(function () {
        //拿到传递过来的商品id
        var goodid = $(this).attr("id")
        //拿到当前的标签名
        var span = $(this)

        //通过getJson方法将数据传递给服务器,getJson默认是get传参4
        //function(data){}这个参数是后台服务器的回调接口  也就是后台给我们返回的数据
        //getJson返回的一定是Json数据
        $.getJSON('/app/subcart/',{"goodid":goodid},function (data) {
            //如果状态吗为900,就让他跳转到登录界面
            if (data["status"] == "900") {
                //target参数  表示是新打开一个窗口还是在原窗口
                window.open("/app/login/",target = "_self")
            //    如果为200  就去往span标签里面设置数据库中对应的值
            }else if (data["status"] == "200") {
                //这一步就是取这是span标签的值
                span.next().html(data["g_num"])
            }
        })
    })


})