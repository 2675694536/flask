
from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^home/', views.home,name='home'),

    url(r'^market/', views.market,name='market'),
    url(r'^market_param/(\d+)/(\d+)/(\d+)/', views.market_param,name='market_param'),


    url(r'^cart/', views.cart,name='cart'),
    url(r'^mine/', views.mine,name='mine'),


#     登录注册
    url(r'^register/',views.register,name='register'),
#     验证用户名是否存在
    url(r'^checkuser/',views.check_user),
#     登录
    url(r'^login/',views.login,name='login'),
    url(r'^check_username/',views.check_username),
    url(r'^login_out/',views.login_out,name='login_out'),


    # 添加商品
    url(r'^addgoods/',views.add_goods,name='addgoods'),
    url(r'^subgoods/',views.sub_goods,name='subgoods'),

#     购物车添加商品
    url(r'^addshops/',views.add_shops,name='addshops'),
    url(r'^subshops/',views.sub_shops,name='subshops'),
]
