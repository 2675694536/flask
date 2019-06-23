from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import User


def regist(request):
    if request.method == 'GET':
        return render(request,'regist.html')
    elif request.method == 'POST':
        username=request.POST.get('username')
        pwd = request.POST.get('password')
        users=User.objects.filter(username=username).all()
        if users.exists():
            return HttpResponse('账户名已存在')

        user=User()
        user.username=username
        user.password=pwd
        user.save()
        return render(request,'index.html')


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        username=request.POST.get('username')
        pwd = request.POST.get('password')
        users=User.objects.filter(username=username).all()
        if users.exists():
            user=users.first()
            if user.password == pwd:
                return HttpResponse('登录成功')
            return HttpResponse('用户名或密码不正确')
        return render(request,'regist.html')