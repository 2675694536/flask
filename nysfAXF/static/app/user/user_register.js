
$(function() {
    $("#password").blur(function () {
        //取得是文本框中的文本值
        var password = $("#password").val();

        if (password.length < 6 || password.length > 18){
            $("#password_info").html("长度小于6位或者大于18位").css("color","red");
        }else{
            $("#password_info").html("")
        }
    })

    $("#password_confirm").blur(function () {
        //取得是文本框中的文本值
        var password = $("#password").val();

        var password_confirm = $(this).val()


        if (password === password_confirm){
            $("#password_confirm_info").html("两次密码一致").css("color","green");
        }else{
            $("#password_confirm_info").html("两次输入不一致").css("color","red");
        }
    })

    $("#username").blur(function () {

    //
        var username = $("#username").val();
        //getJson 就是前端确定请求方式是get的情况下  请求服务器的一种方法
        //而且这种请求方法服务器返回的数据必定是Json数据
        //getJson第一个参数是他的`请求路径
        //第二个参数是请求的时候传递的参数
        //第三个参数是我们给他返回的数据
        $.getJSON("/checkuser/",{"username":username},function (data) {

            if(data["status"] == "200"){
                $("#username_info").html(data["desc"]).css("color","green");
            }else if(data["status"] == "900"){
                $("#username_info").html(data["desc"]).css("color","red");
            }


        })


    })

})


function check_input() {

    var color = $("#username_info").css("color")

    //一定要注意比对的字符串
    if (color === "rgb(255, 0, 0)") {
        return false
    }

    var password = $("#password").val();

    var password_confirm = $("#password_confirm").val()

    if (password.length < 6 || password.length > 18) {
        return false
    }

    if (password != password_confirm) {
        alert(password)
        alert(password_confirm)
        return false
    }


    if (password == password_confirm){
        password = md5(password);
        $("#password").val(password);
        return true
    }
    return false
}
