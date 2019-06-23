function check_input() {
    $('.form-control').blur(function () {
         var pp=$('.form-control').val()
        if(pp.length==0){
            $('#jiaoyan').html('用户名或密码不能为空').css('color', 'red')
            return false
        }
    })
    var password = $('#password').val()
    $("#password").val(md5(password));
    var username=$('#username').val()
    $.getJSON('/check/', {'username': username}, function (data) {
        if (data['status'] == 200) {
            return true
        } else {
            $('#jiaoyan').html('用户名或密码错误').css('color', 'red')
            return false
        }
    })

}
