import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Card, Person


def add_person(request):
    per=Person()
    per.name='郭靖%d'%random.randrange(100)
    per.sex='男'
    per.age='%d'%random.randrange(18,40)
    per.save()
    card=Card()
    card.num='413016199701219876'
    card.pid=per
    card.save()
    return HttpResponse('数据关联成功')


def get_person(request):
    r_name=request.GET.get('name')
    perid=Person.objects.get(name=r_name).id

    cid=Card.objects.get(id=perid)
    context={
        'cid':cid
    }

    return render(request,'get.html',context=context)


def del_person(request):
    name=Card.objects.filter(id=2)
    name.delete()


    return HttpResponse('删除成功')