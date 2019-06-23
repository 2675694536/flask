import io
import random

from PIL import Image, ImageDraw, ImageFont
from django.core.management import color
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Person

# 分页
def fenye(request,num):
    person=Person.objects.all()
    paginator=Paginator(person,2)
    pages=paginator.page(num)
    return render(request,'fenye.html',context={'pages':pages})


def login(request):
    return render(request,'login.html')


def make_color():
    red=random.randrange(255)
    blue=random.randrange(255)
    green=random.randrange(255)
    return (red,blue,green)


def make_point():
    weight=random.randrange(100)
    hight=random.randrange(50)
    return (weight,hight)

def huahua(request):
    size=(100,50)
    # 创建画布
    image=Image.new('RGB',size,color=make_color())
    # 创建画笔
    draw=ImageDraw.Draw(image,'RGB')
    # 选择字体
    font=ImageFont.truetype('/home/xiong/Desktop/projects/test9_yzm/static/uploadefile/fonts/ADOBEARABIC-BOLD.OTF',size=32)
    source='qwertyuiopasdfghjklzxcvbnm1234567890'
    yzm=''
    # 随机获取四位验证码
    for i in range(4):
        yzm+=source[random.randrange(len(source))]
    # 开始画
    for item in range(4):
        draw.text((20 + item * 20, 10), yzm[item], fill=make_color(), font=font)
    # 创建模糊度
    for a in range(600):
        draw.point(make_point(),fill=make_color())
    bytes_io=io.BytesIO()
    image.save(bytes_io,'png')
    response=HttpResponse(bytes_io.getvalue())
    response.set_cookie('yzm',yzm,max_age=60)
    return response


def dologin(request):
    yzm=request.POST.get('yzm')
    c_yzm=request.COOKIES.get('yzm')
    if yzm==c_yzm:
        return HttpResponse('登陆成功')
    return HttpResponse('请重新输入验证码')
