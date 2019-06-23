from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse

from app.models import Room, Student


def login(request):
    #url路径传参,
    return redirect(reverse('app:dologin',args=[1]))

def dologin(request,age):
    return HttpResponse('大家好%s'%age)

def get_room(request):
    room=Room.objects.all()
    return render(request,'rooms.html',context={'room':room})
def get_stu(request,id):
    stu=Student.objects.filter(rid=id).all()
    return render (request,'stu.html',context={'stu':stu})


def logins(request):
    return render(request,'logins.html')


def dologins(request):
    # 取出用户名
    name=request.POST.get('name')
    # 做重定向跳转
    respon=HttpResponseRedirect(reverse('app:index'))
    # 将用户名保存到cookie中
    # respon.set_cookie('name',name,max_age=100)

    # 将用户名设置到session里面
    request.session['name']=name

    return respon


def index(request):
    # 从cookies中取出用户名
    # name=request.COOKIES.get('name')
    # 从session中取出用户名
    name=request.session.get('name')
    return render(request,'index.html',context={'name':name})


def logout(request):
    respon=HttpResponseRedirect(reverse('app:index'))
    # 删除cookie
    # respon.delete_cookie('name')
    # 删除session
    request.session.flush()
    return respon