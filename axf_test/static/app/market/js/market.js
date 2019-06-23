$(function () {
    $('#alltypes').click(function () {
        var name= $('#typedown').attr('class')
        d='glyphicon glyphicon-chevron-down'
        u='glyphicon glyphicon-chevron-up'
        if (name===d) {
            $('#goodscontainer').show()
            $('#typedown').removeClass(d).addClass(u)
            if ($('#sortdown').attr('class')===u){
                $('#sortdown').removeClass(u).addClass(d)
                $('#sort').hide()
            }
        }
        else if(name===u){
            $('#goodscontainer').hide()
            $('#typedown').removeClass(u).addClass(d)
        }

    })
})

$(function () {
    $('#allsort').click(function () {
        var name= $('#sortdown').attr('class')
        d='glyphicon glyphicon-chevron-down'
        u='glyphicon glyphicon-chevron-up'
        if (name===d) {
            $('#sort').show()
            $('#sortdown').removeClass(d).addClass(u)
            if ($('#typedown').attr('class')===u){
                $('#typedown').removeClass(u).addClass(d)
                $('#goodscontainer').hide()
            }
        }

        else if(name===u){
            $('#sort').hide()
            $('#sortdown').removeClass(u).addClass(d)
        }

    })
    $('.addgood').click(function () {
       goodid=$(this).attr('id')
       span=$(this)
       $.getJSON('/addgoods/',{'goodid':goodid},function (data) {
        if(data['status']=='700'){
            window.open('/login/','_self')
        }
        else if (data['status'] === '200'){
                span.prev().html(data['goodnum'])
            }
       })
    })
    $('.subgood').click(function () {
       goodid=$(this).attr('id')
       span=$(this)
       $.getJSON('/subgoods/',{'goodid':goodid},function (data) {
        if(data['status']=='700'){
            window.open('/login/','_self')
        }
        else if (data['status'] === '200'){
                span.next().html(data['goodnum'])
            }
       })
    })
})