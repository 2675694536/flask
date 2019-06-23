$(function () {
    // 判断用户名是否可以注册
    $('#username').blur(function () {
     var username=$('#username').val()
     $.getJSON('/checkuser/',{'username':username},function (data) {
        if (data['status']=='200'){
            $('#username_info').html(data['desc']).css('color','green');
        } else if (data['status']=='900'){
            $('#username_info').html(data['desc']).css('color','red')
        }
     })
    })
    // 判断密码
    $('#password').blur(function () {
        var pwd=$('#password').val()
        if(pwd.length<6){
            $('#password_info').html('密码小于6位数').css('color','red')
        }
        else {
            $('#password_info').html('')
        }
    })
    $('#password_confirm').blur(function () {
       var pwd1=$('#password').val()
       var pwd2=$('#password_confirm').val()
       if(pwd1===pwd2){
           $('#password_confirm_info').html('两次密码相同').css('color','green')
       }
       else {
           $('#password_confirm_info').html('两次密码不同').css('color','red')
        }

    })
    
})

function check_input() {
    var color=$('#username_info').css('color')
    if(color=='rgb(255, 0, 0)'){
        return false
    }
    var pwd1=$('#password').val()
    var pwd2=$('#password_confirm').val()
    if(pwd1.length<6||pwd1.length>18){
        return false
    }
    if(pwd1!==pwd2){
        return false
    }
    if(pwd1==pwd2){
        pwd1=md5(pwd1)
        $('#password').val(pwd1)
        return true

    }return false
}