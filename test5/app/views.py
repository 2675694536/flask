import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import User, Book, Person, People, Card, Room, Student, Good, Custom
# 注册
def register(request):
    if request.method=='GET':
        return render(request,'register.html')

    user_name=request.POST.get('username')

    user=User.objects.filter(username=user_name).all()
    if user.exists():
        return render(request, 'fail.html')
    pwd=request.POST.get('password')
    u=User()
    u.username=user_name
    u.password=pwd
    u.save()
    return render(request,'login.html')

# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    user_name = request.POST.get('username')

    user = User.objects.filter(username=user_name).all()

    if user.exists():
        pwd=request.POST.get('password')
        user=user.first()
        if user.password==pwd:
            return render(request,'book.html')
    return HttpResponse('你的用户名或密码有误')

# 图书
def book(request):
    book=Book.objects.all()
    context={
        'book':book
    }

    return render(request,'bookinfo.html',context=context)

# 人物
def person(request):
    id=request.GET.get('id')
    print(id)
    persons=Person.objects.filter(books=id).all()
    print(persons)
    context={
        'persons':persons
    }
    return render(request,'person.html',context=context)

#一对一添加
def add_people(request):
    people=People()
    people.name='后羿%d'%random.randrange(100)
    people.sex='男'
    people.save()
    card=Card()
    card.num=random.randrange(100000,200000)
    card.cid=people
    card.save()
    return HttpResponse('添加成功')
#一对一删除 删从
def delpeople(request):
    id=request.GET.get('id')
    print(id)
    cid=Card.objects.filter(cid=id).all()
    print(cid)
    cid.delete()

    return HttpResponse('删除成功')

# 一对多添加
def add_stu(request):
    room=Room()
    room.roomname='python班'
    room.save()
    stu=Student()
    stu.name='张飞%d'%random.randrange(10)
    stu.sex='男'
    stu.roomid=room
    stu.save()
    return HttpResponse('添加成功')
# 一对多主删从
def del_room(request):
    id=request.GET.get('id')
    roomId=Room.objects.get(id=id)
    roomId.delete()
    return HttpResponse('删除成功')
# 修改
def change_room(request):
    id=request.GET.get('id')
    room=Room.objects.filter(id=id).first()
    room.roomname='python&java'
    room.save()
    return HttpResponse('修改成功')
# 查询

def get_stu(request):
    return render(request,'getstu.html')
def stu_info(request):
    stu=Student.objects.all()
    context={
        'stu':stu
    }
    return render(request,'stuinfo.html',context=context)
# 多对多添加
def addgood(request):
    goods=Good()
    goods.name='运动鞋%d'%random.randrange(5)
    goods.brand='耐克'
    goods.save()

    custom=Custom()
    custom.name='张三%d'%random.randrange(5)
    custom.sex='男'
    custom.save()
    #注意要在保存后添加 而且要用外键.add(主表对象)
    custom.good.add(goods)

    return HttpResponse('添加成功')


def get_room(request):
    room=Room.objects.filter(id=6).first()
    print(room)
    stu=room.student_set.all()
    print(stu)
    return HttpResponse('查询成功')