$(function () {
    //给分类div点击事件
    $("#alltypes").click(function () {
        //拿到span也就是那个箭头的class值
        var name = $("#typesdown").attr('class')
        //判断 如果你的箭头朝下
        if (name === 'glyphicon glyphicon-chevron-down') {
            //让div展示出来
            $("#goodscontainer").show()
            //让箭头变为朝上
            $("#typesdown").removeClass("glyphicon glyphicon-chevron-down").addClass("glyphicon glyphicon-chevron-up")
            //如果排序的div此时为显现状态  那么将排序的div进行隐藏  并且将排序的箭头变为朝下
            if ($("#sortdown").attr('class') === 'glyphicon glyphicon-chevron-up') {
                $("#sortdown").removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down")
                $("#sort").hide()
            }
        // 跟上面的判断相反
        }else if (name === 'glyphicon glyphicon-chevron-up'){
            $("#goodscontainer").hide()
            $("#typesdown").removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down")
        }
    })


    $("#allsort").click(function () {
        var sortname = $("#sortdown").attr('class')
        if (sortname === 'glyphicon glyphicon-chevron-down') {
            $("#sort").show()
            $("#sortdown").removeClass("glyphicon glyphicon-chevron-down").addClass("glyphicon glyphicon-chevron-up")
            if ($("#typesdown").attr('class') === 'glyphicon glyphicon-chevron-up') {
                $("#typesdown").removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down")
                $("#goodscontainer").hide()
            }
        }else if (sortname === 'glyphicon glyphicon-chevron-up'){
            $("#sort").hide()
            $("#sortdown").removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down")
        }
    })

    //点击容器div的空白部分  隐藏
    $("#goodscontainer").click(function () {
       $("#goodscontainer").hide()
        $("#typesdown").removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down")
    })


    $("#sort").click(function () {
        $("#sort").hide()
        $("#sortdown").removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down")
    })

    $(".subgood").click(function () {
        goodid = $(this).attr('id')
        span = $(this)

        $.getJSON('/subgoods/',{'goodid':goodid},function (data) {
            if (data['status'] === '700') {
                window.open('/login/',target='_self')
            }else if (data['status'] === '200'){
                span.next().html(data['goodnum'])
            }
        })
    })


    $(".addgood").click(function () {
        goodid = $(this).attr('id')
        span = $(this)

        $.getJSON('/addgoods/',{'goodid':goodid},function (data) {
            if (data['status'] === '700') {
                window.open('/login/',target='_self')
            }else if (data['status'] === '200'){
                span.prev().html(data['goodnum'])
            }
        })
    })
})