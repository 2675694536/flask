from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from app.models import Wheel, Nav, MustBuy, Shop, MainShow, FoodTypes, Goods, UserModel, CartModel


def home(request):
    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    mustbuys = MustBuy.objects.all()
    shops = Shop.objects.all()

    shops3_7 = Shop.objects.all()[3:7]
    shops7_ = Shop.objects.all()[7:]
    mainshows = MainShow.objects.all()

    data = {
        'title':"首页",
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shops':shops,
        'shops3_7':shops3_7,
        'shops7_':shops7_,
        'mainshows':mainshows
    }
    return render(request,'home.html',context=data)


def market(request):

    data = {
        'title': "闪购",
    }
    return redirect(reverse('app:market_param',args=(104749,0,1)))


def market_param(request,typeid,cid,sortid):
    # 不管重定向还是前端页面传递的url参数  传递过来以后都是str类型
    # 查询出所有的type类型  一级分类
    foodtypes = FoodTypes.objects.all()
    print(foodtypes)
    # 根据传递过来的类型id找出二级分类
    typename = FoodTypes.objects.get(typeid = typeid)


    #   拿到二级分类中的字符串
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
    elif(sortid == '2'):
        goods = goods.order_by('productnum')
    elif(sortid == '3'):
        goods = goods.order_by('price')
    else:
        goods = goods.order_by('-price')

    userid = request.COOKIES.get('userid')


    data = {
        'foodtypes':foodtypes,
        'typeid':typeid,
        'goods':goods,
        'names':names,
        'cid':cid,
        'userid':userid,

    }

    return render(request,'market.html',context=data)

def cart(request):

    userid = request.COOKIES.get('userid')

    if not userid:
        return redirect(reverse('app:login'))

    carts = CartModel.objects.filter(userid=userid).all()



    data = {
        'title': "购物车",
        'carts':carts
    }
    return render(request, 'cart.html', context=data)


def mine(request):

    data = {
        'title': "我的"
    }

    userid = request.COOKIES.get('userid')

    if userid:
        data['is_login'] = True
        user = UserModel.objects.get(pk=userid)
        data['username'] = user.username
        data['icon'] = '/'+ user.icon.url


        return render(request,'mine.html',context=data)


    return render(request, 'mine.html', context=data)


# 注册
def register(request):
    if request.method == 'GET':
        return render(request,'user/user_register.html')
    else:
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon')

        user = UserModel()
        user.username = username
        user.password = pwd
        user.mail = email
        user.icon = icon

        user.save()
        return redirect(reverse('app:login'))

# 账号验证是否可用
def check_user(request):
    username = request.GET.get('username')
    users = UserModel.objects.filter(username=username).all()

    data = {
        'status':'200',
        'desc':'账号可以注册'
    }

    if users.exists():
        data['status'] = 900
        data['desc'] = '账号已经被注册了,请换一个试试'

    return JsonResponse(data)


def login(request):
    if request.method == 'GET':
        return render(request,'user/user_login.html')
    else:
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        data = {

        }

        if uname:
            user = UserModel.objects.get(username=uname)
            if pwd == user.password:
                data['is_login'] = 'true'
                response = HttpResponseRedirect(reverse('app:mine'))
                response.set_cookie('userid',user.id)
                return response


        return render(request,'error.html')




# 前端跳转验证的函数
def check_username(request):
    name = request.GET.get('name')

    data = {
        'status': "403",
    }

    if not name:
        return JsonResponse(data)

    users = UserModel.objects.filter(username=name).all()
    if not users.exists():
        data['status']='404'
        return JsonResponse(data)
    else:
        data['status'] = '200'
        return JsonResponse(data)


def login_out(request):
    response = HttpResponseRedirect(reverse('app:mine'))
    response.delete_cookie('userid')
    return response



# 闪购页面添加商品按钮
def add_goods(request):
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

        cart.gnum += 1

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

# 闪购页面减少商品按钮
def sub_goods(request):
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


def add_shops(request):

    cartid =  request.GET.get('cartid')

    cart = CartModel.objects.get(pk=cartid)

    cart.gnum += 1

    cart.save()

    data = {
        'status':'200',
        'gnum':cart.gnum
    }

    return JsonResponse(data)


def sub_shops(request):

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
    cartid = request.GET.get("cartid")

    cart = CartModel.objects.get(pk=cartid)

    cart.is_selected = not cart.is_selected

    cart.save()

    userid = request.session.get('user_id')

    carts = CartModel.objects.filter(id=userid)

    # 创建一个变量用于接受全选操作
    is_select_all = True

    # 循环遍历用户对应的商品是否被选中
    # 如果有一个没有被选中
    for ca in carts:
        if not ca.is_selected:
            is_select_all = False

    data = {
        "status":200,
        "is_select":cart.is_selected,
        "is_select_all":is_select_all,
    }
    return JsonResponse(data)


def changeallstatu(request):
    no_select = request.GET.get('selectlist')
    sta = request.GET.get("select")

    select_list = no_select.split("#")

    data = {
        "status":200,
    }

    for select in select_list:
        cart = CartModel.objects.get(pk=select)

        if sta == "select":
            cart.is_selected = False
            cart.save()
            data["is_select"] = "False"
        else :
            cart.is_selected = True
            cart.save()
            data["is_select"] = "True"

    return JsonResponse(data)


def order(request):
    userid = request.session.get('user_id')

    if not userid:
        return redirect(reverse("app:login"))

    # 通过userid去往usermodel里面过滤
    # 通过usermodel可以直接拿到他在订单表里面的数据
    # 然后再去拿到订单表中对应的商品信息
    user = UserModel.objects.get(pk=userid)
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

    return render(request,'order/order_info.html',context=data)