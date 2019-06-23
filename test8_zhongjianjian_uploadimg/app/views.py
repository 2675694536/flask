import random

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from app.models import User
from test8 import settings


def qiang(request):
    r = random.randrange(100)
    if r > 90:
        return HttpResponse('恭喜你抢到优惠券')
    else:
        return HttpResponse('很遗憾没有抢到')


def upload(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
    else:
        image = request.FILES.get('icon')
        name=request.POST.get('name')
        user = User()
        user.name=name
        user.icon=image
        user.save()
        return HttpResponse('图片上传成功')


def show(request):

    user=User.objects.all().first()
    imgurl='timg.jpeg'
    context={
        'imgurl':imgurl
    }
    return render(request,'show.html',context=context)
