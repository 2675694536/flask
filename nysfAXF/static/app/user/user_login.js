
// 前端验证和跳转
function check_input() {
    //第一步  取用户名
    var username = $(".form-control").val();

    //取密码
    var password = $("#password").val();
    //对密码进行加密
    $("#password").val(md5(password));

   if (username.length === 0) {
       $("#jiaoyan").html("用户名或者密码不能为空").css('color','red')
       return false
   }else{
       $("#jiaoyan").html("")
   }

   if (password.length === 0) {
       $("#jiaoyan").html("用户名或者密码不能为空").css('color','red')
       return false
   }else{
       $("#jiaoyan").html("")
   }

    //判断用户名是否存在
    $.getJSON('/check_username/',{'name':name},function (data) {
        if (data['status'] == '200') {
            $("#jiaoyan").html("")
            return true
        }else{
            $("#jiaoyan").html("用户名或者密码有误").css('color','red')
            return false
        }
    })
}