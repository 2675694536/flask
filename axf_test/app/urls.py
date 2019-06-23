
from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^home/',views.home,name='home'),
    url(r'^market/',views.market,name='market'),
    url(r'^market_param/(\d+)/(\d+)/(\d+)/',views.market_param,name='marketparam'),
    url(r'^cart/',views.cart,name='cart'),
    url(r'^mine/',views.mine,name='mine'),
    url(r'^register/',views.register,name='register'),
    url(r'^checkuser/',views.check_user,name='check_user'),
    url(r'^login/',views.login,name='login'),
    url(r'^check/',views.check,name='check'),
    url(r'^loginout',views.loginout,name='loginout'),
    url(r'^addgoods/',views.addgoods,name='addgoods'),
    url(r'^subgoods/',views.subgoods,name='subgoods'),
    url(r'^addshop/',views.addshop,name='addshop'),
    url(r'^subshop/',views.subshop,name='subshop'),
    url(r'^change_choose_statu/', views.changechoosestatu),
    url(r'^all_select/', views.changeallstatu,name='all_select'),
    url(r'^goodsinfo/', views.orderinfo),
    url(r'^dingdan/$', views.order),
]
