import hashlib
import uuid

from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from app.models import Wheel, Nav, Mustbuy, Shop, MainShow, FoodTypes, Goods, User, CartModel, OrderModel, \
    OrderGoodModel


def home(request):
    wheels=Wheel.objects.all()
    navs=Nav.objects.all()
    mustbuy=Mustbuy.objects.all()
    shopList=Shop.objects.all()
    shop1 = shopList[0]
    shop2 = shopList[1:3]
    shop3 = shopList[3:7]
    shop4 = shopList[7:11]
    mainshow=MainShow.objects.all()
    data={
        'title':'首页',
        'wheels':wheels,
        'navs':navs,
        'mustbuy':mustbuy,
        'shop1':shop1,
        'shop2':shop2,
        'shop3':shop3,
        'shop4':shop4,
        'mainshow':mainshow
    }
    return render(request,'home.html',context=data)


def market(request):
    return redirect(reverse('app:marketparam',args=(104749,0,1)))
def market_param(request,typeid,cid,sortid):
    # 不管重定向还是前端页面传递的url参数  传递过来以后都是str类型
    # 查询出所有的type类型  一级分类
    foodtypes = FoodTypes.objects.all()
    # 根据传递过来的类型id找出二级分类
    typename = FoodTypes.objects.get(typeid=typeid)

    # 拿到二级分类中的字符串
    namestr = typename.childtypenames

    # 对字符串进行切割
    # [全部分类:0,进口水果:103534,国产水果:103533]
    name_list = namestr.split('#')
    names = []
    for i in name_list:
        names.append(i.split(':'))

    # 如果传递过来的cid为0,就拿出所有的商品
    if (cid == '0'):
        goods = Goods.objects.filter(categoryid=typeid).all()

    else:
        # 如果传递过来的cid有值,那么就根据值就行过滤
        goods = Goods.objects.filter(categoryid=typeid).filter(childcid=cid).all()

    if (sortid == '1'):
        goods = goods.order_by()
    elif (sortid == '2'):
        goods = goods.order_by('productnum')
    elif (sortid == '3'):
        goods = goods.order_by('price')
    else:
        goods = goods.order_by('-price')

    data = {
        'foodtypes': foodtypes,
        'typeid': typeid,
        'goods': goods,
        'names': names,
        'cid': cid
    }

    return render(request, 'market.html', context=data)
def cart(request):
    Goods=[]
    user_id = request.COOKIES.get('userid')
    if not user_id:
        return redirect(reverse('app:login'))
    else:
        carts = CartModel.objects.filter(userid=user_id)

    context = {
        "title": '购物车',
        "carts": carts,
    }
    return render(request, 'cart.html', context=context)
def mine(request):
    data = {
        'title': "我的"
    }

    userid = request.COOKIES.get('userid')

    if userid:
        data['is_login'] = True
        user = User.objects.get(pk=userid)
        data['username'] = user.username
        data['icon'] = '/' + user.userImg.url
        return render(request, 'mine.html', context=data)
    return render(request, 'mine.html', context=data)


def register(request):
    if request.method=='GET':
        return render(request,'user/user_register.html')
    username=request.POST.get('username')
    pwd=request.POST.get('password')
    img=request.FILES.get('icon')
    user=User()
    user.username=username
    user.password=pwd
    user.userImg=img
    user.save()
    return redirect(reverse('app:login'))


# 账号验证是否可用
def check_user(request):
    username = request.GET.get('username')
    users = User.objects.filter(username=username).all()

    data = {
        'status':'200',
        'desc':'账号可以注册'
    }
    if users.exists():
        data['status'] = 900
        data['desc'] = '账号已经被注册了,请换一个试试'
    return JsonResponse(data)

def login(request):
    if request.method=='GET':
        return render(request,'user/login.html')
    username=request.POST.get('username')
    pwd=request.POST.get('password')
    data={}
    if username:
        user=User.objects.get(username=username)
        if user.password==pwd:
            data['is_login'] = 'true'
            response = HttpResponseRedirect(reverse('app:mine'))
            response.set_cookie('userid', user.id)
            return response
        return HttpResponse('用户名或密码不存在')
    return HttpResponse('用户名或密码不存在')

def check(request):
    username = request.GET.get('username')

    data = {
        'status': "403",
    }

    if not username:
        return JsonResponse(data)

    users = User.objects.filter(username=username).all()
    if not users.exists():
        data['status'] = '404'
        return JsonResponse(data)
    else:
        data['status'] = '200'
        return JsonResponse(data)

def loginout(request):
    response = HttpResponseRedirect(reverse('app:mine'))
    response.delete_cookie('userid')
    return response


def addgoods(request):
    goodid=request.GET.get('goodid')
    userid=request.COOKIES.get('userid')
    data={}
    if not userid:
        data['status']='700'
        data['msg']='not login'
        return JsonResponse(data)
    carts=CartModel.objects.filter(userid=userid).filter(goodid=goodid).all()
    if carts.exists():
        cart=carts.first()
        cart.gnum+=1
        cart.save()
        data['status'] = '200'
        data['goodnum'] = cart.gnum
    else:
        gname = Goods.objects.get(pk=goodid).productname
        cart = CartModel()
        cart.userid_id = userid
        cart.goodid_id = goodid
        cart.gnum = 1
        cart.gname = gname
        cart.save()
        data['status'] = '200'
        data['goodnum'] = cart.gnum
    return JsonResponse(data)
def subgoods(request):
    goodid = request.GET.get('goodid')
    userid = request.COOKIES.get('userid')
    data = {

    }

    if not userid:
        data['status'] = '700'
        data['msg'] = 'not login'
        return JsonResponse(data)
    carts = CartModel.objects.filter(userid=userid).filter(goodid=goodid).all()
    if carts.exists():
        cart = carts.first()
        if cart.gnum > 1:
            cart.gnum -= 1
            cart.save()
            data['goodnum'] = cart.gnum
            data['status'] = '200'
        elif cart.gnum == 1:
            cart.delete()
            data['goodnum'] = 0
            data['status'] = '200'
    return JsonResponse(data)


def addshop(request):

    cartid =  request.GET.get('cartid')

    cart = CartModel.objects.get(pk=cartid)

    cart.gnum += 1

    cart.save()

    data = {
        'status':'200',
        'gnum':cart.gnum
    }

    return JsonResponse(data)


def subshop(request):

    data = {

    }
    cartid = request.GET.get('cartid')

    cart = CartModel.objects.get(pk=cartid)

    if cart.gnum == 1:
        cart.delete()
        data['status'] = '202'
    else:
        cart.gnum -= 1
        cart.save()
        data['status'] = '200'
        data['gnum'] = cart.gnum
    return JsonResponse(data)
def changechoosestatu(request):
    cartid=request.GET.get('cartid')
    span=request.GET.get('span1')
    cart = CartModel.objects.get(pk=cartid)
    userid = request.COOKIES.get('userid')
    carts = CartModel.objects.filter(userid=userid).all()
    all=True
    print('--->',carts.first().is_select)


    data={
    'all':all
    }

    if not span:
        cart.is_select=True
        cart.save()
    else:
        cart.is_select = False
        cart.save()
    for ca in carts:
        if ca.is_select==False:
            data['all']=False
    if not cart.is_select:
        data['status']='400'
    else:
        data['status']='200'

    return JsonResponse(data)



def changeallstatu(request):
    span = request.GET.get('span1')

    userid = request.COOKIES.get('userid')

    carts = CartModel.objects.filter(userid=userid).all()
    data = {

    }

    if not span:
        data['status'] = '200'
        for i in carts:
            i.is_select = True
            i.save()
        return JsonResponse(data=data)
    else:
        data['status'] = '404'
        for i in carts:
            i.is_select = False
            i.save()
        return JsonResponse(data=data)


def order(request):
    userid = request.COOKIES.get('userid')

    if not userid:
        return redirect(reverse("app:login"))

    # 通过userid去往usermodel里面过滤
    # 通过usermodel可以直接拿到他在订单表里面的数据
    # 然后再去拿到订单表中对应的商品信息
    user = User.objects.get(pk=userid)
    carts = CartModel.objects.filter(c_user_id=user.id)

    order = OrderModel()
    order.o_num = str(uuid.uuid4())
    order.o_user_id = userid
    order.save()

    for cart in carts:
        if cart.is_selected:
            ordergood = OrderGoodModel()

            ordergood.og_good_id = cart.c_goods_id
            ordergood.og_num = cart.c_num
            ordergood.og_order_id = order.id

            ordergood.save()

            cart.delete()

    data = {
        "status":200,
        "orderid":order.id
    }

    return JsonResponse(data)



def orderinfo(request):
    orderid = request.GET.get("orderid")

    goodlist = OrderGoodModel.objects.filter(og_order_id=orderid)

    data={
        "goodlist":goodlist,
        "orderid":orderid,
    }

    return render(request,'user/order_info.html',context=data)