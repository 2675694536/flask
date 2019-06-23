import hashlib
import uuid

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from app.models import WheelMain, TopMenu, MustBuy, ShopMain, MainShow, FoodType, Good, UserModel, CartModel, \
    OrderModel, OrderGoodModel


def home(request):

    # 首页轮播的
    wheels = WheelMain.objects.all()

    # 顶部菜单的
    menus = TopMenu.objects.all()

    # 返回横向轮播菜单数据
    mustbuys = MustBuy.objects.all()

    # 闪送超市数据
    shops = ShopMain.objects.all()

    #
    shop0 = shops[0]

    shop1_2 = shops[1:3]

    shop3_6 = shops[3:7]

    shop7_ = shops[7:]

    mianshows = MainShow.objects.all()


    context = {
        "wheels":wheels,
        "title" :'首页',
        "menus" : menus,
        "mustbuys":mustbuys,
        "shop0":shop0,
        "shop1_2": shop1_2,
        "shop3_6": shop3_6,
        "shop7_" : shop7_ ,
        "mianshows":mianshows
    }
    return render(request,'home/home.html',context=context)


def cart(request):

    Goods = []

    user_id = request.session.get('user_id')
    if not user_id:
        return redirect(reverse('app:login'))
    else:
        carts = CartModel.objects.filter(c_user=user_id)

    context = {
        "title":'购物车',
        "carts":carts,
    }
    return render(request,'cart/cart.html',context=context)

# 闪购页面的路由
def market(request):

   return redirect(reverse('app:infomarket',args=('104749',0,0)))


# 重定向后的闪购
def infomarket(request,typeid,cid,sortid):
    # 返回所有的侧边列表名称
    types = FoodType.objects.all()

    # 判断二级联动的id值,如果为0  就返回所有的商品
    # 如果不为0  就拿到商品以后进行联合过滤  然后返回
    if cid == '0':
        goods = Good.objects.filter(categoryid=typeid)
    else:
        goods = Good.objects.filter(categoryid=typeid).filter(childcid=cid)


    # 排序id  判断之后返回相对应的结果
    # 记着   一定要去接受排序后的对象  因为排序后的对象是返回了一个obj的结果  所以我们要去拿一个对象接受一下
    if sortid == "0":
        pass
    if sortid == "1":
        # 这里要接受一下排序后的对象
        goods = goods.order_by("productnum")
    if sortid == "2":
        goods = goods.order_by("price")
    if sortid == "3":
        goods = goods.order_by("-price")

    # 根据一级目录传过来的id找出对应的对象
    type = FoodType.objects.get(typeid = typeid)
    # 取出其中的字段
    typenames = type.childtypenames
    # 全部分类:0#个人护理:103576#纸品:103578#日常用品:103580#家居清洁:103577
    # 进行第一次切割
    typenamelist = typenames.split("#")
    print(typenamelist)
    typelist = []
    # 进行第二次切割
    for typename in typenamelist:
        typesmalllist = typename.split(":")
        typelist.append(typesmalllist)

    print(typelist)
    context = {
        "types": types,
        "title": '闪购',
        "goods": goods,
        "typeid" : int(typeid),
        "typelist" : typelist,
        "cid":cid,
    }

    return render(request, 'market/market.html', context=context)


def mine(request):
    user_id = request.session.get("user_id")

    context = {
        "title": "我的",
    }

    if user_id:
        user = UserModel.objects.get(pk=user_id)
        username = user.username
        icon = '/static/upload/' + user.icon.url
        context["username"] = username
        context["icon"] = icon
        context["is_login"] = True


    return render(request, 'mine/mine.html', context=context)


def login(request):
    if request.method == 'GET':
        return  render(request,'user/user_login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = make_password(request.POST.get('password'))

        if username != None:
            # 因为使用get的时候  必须要保证数据库里面有一个值  不能为None和多值
            users = UserModel.objects.filter(username=username)
            if users.exists():
                user = users.first()
                if user.password == password:
                    request.session['user_id'] = user.id
                    return redirect(reverse('app:mine'))
                else:
                    return HttpResponse("账户或者密码错误")
            else:
                return redirect(reverse('app:register'))
        else:
            return HttpResponse("对不起,你的用户名不能为空")
    else:
        return HttpResponse("该请求方式不被支持")


def register(request):
    if request.method == 'GET':
        return render(request,'user/user_register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = make_password(request.POST.get('password'))

        users = UserModel.objects.filter(username=username)

        if  users.exists():
            return HttpResponse("此用户已经存在")

        email = request.POST.get('email')
        icon = request.FILES["icon"]

        user = UserModel()
        user.username = username
        user.password = password
        user.mail = email
        user.icon = icon

        user.save()

        request.session['user_id'] = user.id

        return redirect(reverse('app:mine'))

def make_password(password):
    md55 = hashlib.md5()
    md55.update(password.encode('utf-8'))
    return md55.hexdigest()


def checkuser(request):
    # 第一步  取出getJson传递过来的数据
    username = request.GET.get("username")
    # 第二步  封装Json数据
    data = {
        "status":"200",
        "desc":"此用户可以被使用"
    }

    # 第三步  过滤姓名对应的信息
    users = UserModel.objects.filter(username=username)
    # 第四步 判断信息是否存在 如果存在  修改Json数据
    if users.exists():
        data["status"] = "900"
        data["desc"] = "此用户已经存在"

    #     第五步  原样返回数据
    return JsonResponse(data=data)


def loginout(request):
    request.session.flush()
    return redirect(reverse('app:mine'))


def addCart(request):
    # 取出JS传递过来的商品id值
    good_id = request.GET.get("goodid")
    # 取出session中的id值
    user_id = request.session.get("user_id")

    data = {
        "status":"200",
    }
    # 如果session中不存在用户id
    # 那么证明没有用户登陆过
    if not user_id:
        data["status"] = "900"
        return JsonResponse(data)
    else:
        # 如果已经登录  就去过滤
        carts = CartModel.objects.filter(c_goods=good_id).filter(c_user=user_id)
        if carts.exists():
            cart = carts.first()
            cart.c_num += 1
            data["g_num"] = cart.c_num

        else:
            cart = CartModel()
            cart.c_goods_id = good_id
            cart.c_user_id = user_id
            cart.c_num = 1
            data["g_num"] = 1
        cart.save()
    return JsonResponse(data)


def subCart(request):
    # 取出JS传递过来的商品id值
    good_id = request.GET.get("goodid")
    # 取出session中的id值
    user_id = request.session.get("user_id")

    data = {
        "status": "200",
    }
    # 如果session中不存在用户id
    # 那么证明没有用户登陆过
    if not user_id:
        data["status"] = "900"
        return JsonResponse(data)
    else:
        # 如果已经登录  就去过滤
        carts = CartModel.objects.filter(c_goods=good_id).filter(c_user=user_id)
        if carts.exists():
            cart = carts.first()
            if cart.c_num == 1:
                cart.delete()
                data["g_num"] = 0
            else:
                cart.c_num -= 1
                cart.save()
                data["g_num"] = cart.c_num

    return JsonResponse(data)


def addShop(request):
    # 取出带过来的id参数值
    cartid = request.GET.get("cartid")
    # 过滤
    cart = CartModel.objects.get(pk=cartid)

    # 在原值上面进行+1操作
    cart.c_num += 1

    # 保存到数据库
    cart.save()

    data = {
        "status":200,
    }
    # 返回对应的数量
    data["g_num"] = cart.c_num

    return JsonResponse(data)


def subShop(request):
    # 取出带过来的id参数值
    cartid = request.GET.get("cartid")
    # 过滤
    cart = CartModel.objects.get(pk=cartid)

    data = {
        "status": 200,
    }

    if cart.c_num == 1:
        cart.delete()
        data["g_num"] = 0
    else:
        # 在原值上面进行+1操作
        cart.c_num -= 1

        # 保存到数据库
        cart.save()

        # 返回对应的数量
        data["g_num"] = cart.c_num

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