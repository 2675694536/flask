$(function () {


    $("#password_confirm").change(function () {

        var password = $("#password").val();
        var password_confirm = $(this).val()

        if (password == password_confirm){
            $("#password_confirm_info").html("两次一致").css("color","green");
        }else{
            $("#password_confirm_info").html("两次输入不一致").css("color","red");
        }
    })

    $("#username").change(function () {

    //
        var username = $("#username").val();
        //getJson 就是前端确定请求方式是get的情况下  请求服务器的一种方法
        //而且这种请求方法服务器返回的数据必定是Json数据
        //getJson第一个参数是他的`请求路径
        //第二个参数是请求的时候传递的参数
        //第三个参数是我们给他返回的数据
        $.getJSON("/app/checkuser/",{"username":username},function (data) {

            console.log(data);

            if(data["status"] == "200"){
                $("#username_info").html(data["desc"]).css("color","green");
            }else if(data["status"] == "900"){
                $("#username_info").html(data["desc"]).css("color","red");
            }


        })


    })






})


function check_input() {

    var color = $("#username_info").css("color");
    console.log(color);
    if (color == "rgb(255, 0, 0)"){
        console.log("红色的");
        return false
    }else {
        console.log("绿色的");
    }

    var password = $("#password").val();
    if (password.length < 6){
        return false
    }

    var password_confirm = $("#password_confirm").val();

    if (password == password_confirm){
        password = md5(password);
        console.log(password);
        $("#password").val(password);
        return true
    }

    return false

}
