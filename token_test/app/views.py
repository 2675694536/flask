import hashlib
import uuid
from audioop import reverse

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import User


def register(request):
    return render(request,'register.html')


def make_pwd(password):
    md_5=hashlib.md5
    md_5.update(password.encode('utf-8'))
    password=md_5.hexdigest()
    return password


def make_token():
    # 生成uuid唯一标识
    uid=str(uuid.uuid4())
    md_55=hashlib.md5()
    md_55.update(uid.encode('utf-8'))
    token=md_55.hexdigest()
    return token
def save(request):
    name=request.POST.get('name')
    password=request.POST.get('password')
    uer=User()
    uer.name=name
    uer.password=make_pwd(password)
    token=make_token()
    uer.token=token
    uer.save()
    # 重定向到首页,并将token值放在cookie里
    response=HttpResponseRedirect(reverse('app:index'))
    response.set_cookie('utoken',token)
    return response

def index(request):
    token=request.COOKIES.get('utoken')
    if token:
        users=User.objects.filter(token=token).all()
        name=users.first().name
        return render(request,'index.html',context={'name':name})
    return HttpResponse('请去注册')

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        name=request.POST.get('name')
        user=User.objects.filter(name=name).all()
        if user.exists():
            user=user.first()
            pwd=request.POST.get('password')
            if user.password==make_pwd(pwd):
                newtoken=make_token()
                user.token=newtoken
                user.save()
                response=HttpResponseRedirect(reverse('app:index'))
                response.set_cookie('utoken',newtoken)
                return response
        return HttpResponse('账号或密码有误')
