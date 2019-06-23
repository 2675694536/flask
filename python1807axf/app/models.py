from django.db import models

# Create your models here.
class MainModel(models.Model):
    # img, name, trackid
    img = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    trackid = models.CharField(max_length=16)

    # 元信息
    # 它里面包含了整个模型的model层里面的所有属性
    class Meta:
        abstract = True

class WheelMain(MainModel):
    class Meta:
        db_table = 'axf_wheel'


class TopMenu(MainModel):
    class Meta:
        db_table = "axf_nav"


class MustBuy(MainModel):
    class Meta:
        db_table = "axf_mustbuy"


class ShopMain(MainModel):
    class Meta:
        db_table = "axf_shop"



# 创建列表展示的商品model
# insert into axf_mainshow(trackid,name,img,categoryid,brandname,
#                          img1,childcid1,productid1,longname1,price1,
#                          marketprice1,img2,childcid2,productid2,longname2,
#                          price2,marketprice2,img3,childcid3,productid3,
#                          longname3,price3,marketprice3) values\
#                 ("21782","优选水果",
#                  "http://img01.bqstatic.com//upload/activity/2017031018205492.jpg@90Q.jpg",
#                  "103532","爱鲜蜂",
#                  "http://img01.bqstatic.com/upload/goods/201/701/1916/20170119164159_996462.jpg@200w_200h_90Q","103533","118824","爱鲜蜂·特小凤西瓜1.5-2.5kg/粒","25.80","25.8","http://img01.bqstatic.com/upload/goods/201/611/1617/20161116173544_219028.jpg@200w_200h_90Q","103534","116950","蜂觅·越南直采红心火龙果350-450g/盒","15.3","15.8","http://img01.bqstatic.com/upload/goods/201/701/1916/20170119164119_550363.jpg@200w_200h_90Q","103533","118826","爱鲜蜂·海南千禧果400-450g/盒","9.9","13.8");


class MainShow(models.Model):
    trackid = models.IntegerField()
    name = models.CharField(max_length=32)
    img = models.CharField(max_length=256)
    categoryid = models.IntegerField()
    brandname = models.CharField(max_length=128)
    img1 = models.CharField(max_length=256)
    childcid1 = models.IntegerField()
    productid1 = models.IntegerField()
    longname1 = models.CharField(max_length=128)
    price1 = models.CharField(max_length=54)
    marketprice1 = models.CharField(max_length=54)
    img2 = models.CharField(max_length=256)
    childcid2 = models.IntegerField()
    productid2 = models.IntegerField()
    longname2 = models.CharField(max_length=256)
    price2 = models.CharField(max_length=32)
    marketprice2 = models.CharField(max_length=36)
    img3 = models.CharField(max_length=256)
    childcid3 = models.IntegerField()
    productid3 = models.IntegerField()
    longname3 = models.CharField(max_length=256)
    price3 = models.CharField(max_length=32)
    marketprice3 = models.CharField(max_length=32)


    class Meta:
        db_table = 'axf_mainshow'



class FoodType(models.Model):
    # typeid, typename, childtypenames, typesort
    typeid = models.IntegerField()
    typename = models.CharField(max_length=32)
    childtypenames = models.CharField(max_length=256)
    typesort = models.IntegerField()

    class Meta:
        db_table='axf_foodtypes'


    # axf_goods(productid, productimg, productname, productlongname, isxf, pmdesc, specifics, price, marketprice,
    #           categoryid, childcid, childcidname, dealerid, storenums, productnum)
    # values("11951", "http://img01.bqstatic.com/upload/goods/000/001/1951/0000011951_63930.jpg@200w_200h_90Q", "",
    #        "乐吧薯片鲜虾味50.0g", 0, 0, "50g", 2.00, 2.500000, 103541, 103543, "膨化食品", "4858", 200, 4);


class Good(models.Model):
    productid= models.IntegerField()
    productimg= models.CharField(max_length=256)
    productname= models.CharField(max_length=256)
    productlongname= models.CharField(max_length=256)
    isxf= models.IntegerField()
    pmdesc= models.IntegerField()
    specifics= models.CharField(max_length=256)
    price= models.FloatField(max_length=256)
    marketprice= models.FloatField(max_length=256)
    categoryid= models.IntegerField()
    childcid= models.IntegerField()
    childcidname= models.CharField(max_length=256)
    dealerid= models.CharField(max_length=256)
    storenums= models.IntegerField()
    productnum= models.IntegerField()

    class Meta:
        db_table='axf_goods'


class UserModel(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=256)
    mail = models.CharField(max_length=64)
    sex = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    icon = models.ImageField()


class CartModel(models.Model):
    c_user = models.ForeignKey(UserModel)
    c_goods = models.ForeignKey(Good)

    c_num = models.IntegerField(default=1)
    is_selected = models.BooleanField(default=True)


class OrderModel(models.Model):
    o_user = models.ForeignKey(UserModel)
    o_num = models.CharField(max_length=128)
    o_time = models.DateTimeField(auto_now=True)
    o_stau = models.IntegerField(default=1)


# 订单商品表
# 第一个字段  购买的商品ID
# 第二个字段  谁购买的商品  也就是用户的ID
# 第三个字段  每个商品购买的数量
class OrderGoodModel(models.Model):
    og_order = models.ForeignKey(OrderModel)
    og_good = models.ForeignKey(Good)
    og_num = models.IntegerField()