from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import User


def register(request):
    return render(request,'reg.html')


def do(request):
    username=request.POST.get('username')
    pwd=request.POST.get('password')

    user=User()
    user.name=username
    user.password=pwd

    user.save()
    return HttpResponse('sucessful')



def show(request):
    # use=User.objects.filter(age__gt=18).all()
    use=User.objects.get(pk=2)
    # print(use)
    context={
        'u':use
    }

    return render(request,'show.html',context=context)
