
from django.conf.urls import url
from django.contrib import admin

from app import views

urlpatterns = [
    url(r'^home/', views.home,name='home'),
    url(r'^cart/', views.cart,name='cart'),
    url(r'^market/', views.market,name='market'),
    url(r'^infomarket/(\d+)/(\d+)/(\d+)/', views.infomarket,name='infomarket'),
    url(r'^mine/', views.mine,name='mine'),

    url(r'login/',views.login,name='login'),
    url(r'register/',views.register,name='register'),
    url(r'checkuser/',views.checkuser,name='checkuser'),
    url(r'loginout/',views.loginout,name='login_out'),

    url(r'^addcart/',views.addCart),
    url(r'^subcart/',views.subCart),

    url(r'^addshop/', views.addShop),
    url(r'^subshop/', views.subShop),

    url(r'^change_choose_statu/',views.changechoosestatu),
    url(r'^changeallstatu/', views.changeallstatu),



    url(r'^goodsinfo/',views.orderinfo),
    url(r'^dingdan/$',views.order),

]
