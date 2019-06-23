$(function () {
    $(".addshop").click(function () {
        cartid = $(this).attr('id')
        button = $(this)

        $.getJSON('/addshops/',{'cartid':cartid},function (data) {
            if (data['status'] === '200'){
                button.prev().html(data['gnum'])
            }
        })
    })

    $(".subshop").click(function () {
        cartid = $(this).attr('id')
        button = $(this)

        $.getJSON('/subshops/',{'cartid':cartid},function (data) {
            if (data['status'] === '200'){
                button.next().html(data['gnum'])
            }else{
                button.parents('li')[0].remove()
            }
        })
    })
})