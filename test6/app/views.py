from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import User, Book, Person

# 注册
def reister(request):
    if request.method=='GET':
        return render(request,'register.html')
    username=request.POST.get('name')
    user=User.objects.filter(name=username).all()
    if user.exists():
        return render(request,'fail.html')
    pwd=request.POST.get('password')
    user=User()
    user.name=username
    user.password=pwd
    user.save()
    return render(request,'login.html')
# 登录
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    username=request.POST.get('name')
    user=User.objects.filter(name=username).all()
    if user.exists():
        pwd=request.POST.get('password')
        user=user.first()
        if user.password==pwd:
            return render(request,'book.html')
    return HttpResponse('用户名或密码错误')
# 图书
def book(request):
    book=Book.objects.all()
    context={
        'book':book
    }
    return render(request,'bookinfo.html',context=context)
# 添加书籍
def addbook(request):
    print(request.method)
    if request.method=='GET':
        return render(request,'addbook.html')
    name=request.POST.get('name')
    author=request.POST.get('author')
    book=Book()
    book.name=name
    book.author=author
    book.save()
    return HttpResponse('添加成功')
# 人物
def person(request):
    id=request.GET.get('id')
    p=Person.objects.filter(id=id).all()
    context={
        'p':p
    }
    return render(request,'person.html',context=context)


