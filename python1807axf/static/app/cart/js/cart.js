$(function () {

    //购物车的加数量
    $(".addshop").click(function () {
        //找到所有当前元素的父标签是li的元素
        var li = $(this).parents("li");
        //拿到li的对应的id值
        var cartid = $(this).parents("li").attr("id");

        //通过getJSON方法请求服务器
        $.getJSON('/app/addshop/',{"cartid":cartid},function (data) {
            if (data["status"] == 200) {
                //如果状态码为200  通过li找到span标签 然后将span标签中的内容进行修改
                li.find("span").last().html(data["g_num"])
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
        $.getJSON('/app/subshop/',{"cartid":cartid},function (data) {
            if (data["g_num"] == 0) {
                li.remove()
            } else {
                //如果状态码为200  通过li找到span标签 然后将span标签中的内容进行修改
                li.find("span").last().html(data["g_num"])
            }
        })
    });


    //选中状态
    $(".is_choosed").click(function () {
        //找到父标签
        var li = $(this).parents("li");
        var cartid = $(this).parents("li").attr("id");
         //通过getJSON方法请求服务器
        $.getJSON('/app/change_choose_statu/',{"cartid":cartid},function (data) {
            //根据状态码解析
            if (data["status"] == 200) {
                if (data["is_select"]){
                    li.find("span").first().html("<span>√</span>")
                    li.find("span").first().attr('id','True')
                    if (data["is_select_all"]) {
                        $(".all_select").find("span").html(" <span>√</span>")
                    }
                }else{
                    li.find("span").first().html("<span></span>")
                    li.find("span").first().attr('id','False')
                    $(".all_select").find("span").html(" <span></span>")
                }
            }

        })
    })



//全选按钮
    $(".all_select").click(function () {
    //    创建两个数组
        var select = []
        var no_select = []


        //找到某个标签下面所有的对应的元素
        $(".is_choosed").each(function () {
            if ($(this).attr("id").toLowerCase() == "false") {
                no_select.push($(this).parents("li").attr("id"))
            }else if ($(this).attr("id").toLowerCase() == "true") {
                select.push($(this).parents("li").attr("id"))

            }
        })
        console.log(no_select)
        console.log(select)

        //如果你的选中数据里面长度为0  那么都处于未选中状态
        if (select.length == 0) {
            $.getJSON('/app/changeallstatu/',{"selectlist":no_select.join("#"),"select":"unselect"},function (data) {
                if (data["status"] == 200) {
                    if (data["is_select"] == "True") {
                         $(".is_choosed").each(function () {
                             $(this).html(" <span>√</span>")
                             $(this).attr('id','True')
                             $(".all_select").html(" <span>√</span>")
                        })
                    }
                }
            })
        }

        //如果你的未选中数据里面长度为0  那么都处于选中状态
        if (no_select.length == 0) {
            $.getJSON('/app/changeallstatu/',{"selectlist":select.join("#"),"select":"select"},function (data) {
                if (data["status"] == 200) {
                    if (data["is_select"] == "False") {
                         $(".is_choosed").each(function () {
                             $(this).html("<span></span>")
                             $(this).attr('id','False')
                             $(".all_select").html(" <span></span>")
                        })
                    }
                }
            })
        }

    })


//    JS点击下单操作
    $("#getorder").click(function () {
        $.getJSON('/app/dingdan/',function (data) {
            alert("我有问题")
            if (data["status"] == 200) {
                var orderid = data["orderid"]
                window.open("/app/goodsinfo/?orderid="+orderid,target="_self",)
            }
        })
    })
})