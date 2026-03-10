from django.db import models
from Admin.models import *
from Guest.models import *
# Create your models here.
class tbl_product(models.Model):
   product_name=models.CharField(max_length=30)
   product_details=models.CharField(max_length=30)
   product_price=models.CharField(max_length=30)
   seller_id=models.ForeignKey(tbl_seller,on_delete=models.CASCADE)
   product_photo=models.FileField(upload_to="Assets/product/Photo/")
   category_id=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_stock(models.Model):
   stock_count=models.CharField(max_length=30)
   product_id=models.ForeignKey(tbl_product,on_delete=models.CASCADE)

class tbl_gallery(models.Model):
   gallery_file=models.FileField(upload_to="Assets/gallery/photo/")
   product_id=models.ForeignKey(tbl_product,on_delete=models.CASCADE)

class tbl_deliveryboy(models.Model):
   deliveryboy_name=models.CharField(max_length=30)
   deliveryboy_email=models.CharField(max_length=30)
   deliveryboy_contact=models.CharField(max_length=30)
   deliveryboy_address=models.CharField(max_length=30)
   deliveryboy_photo=models.FileField(upload_to="Assets/Seller/Photo/")
   deliveryboy_proof=models.FileField(upload_to="Assets/Seller/proof/")
   deliveryboy_password=models.CharField(max_length=60)
   place_id=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
   seller_id=models.ForeignKey(tbl_seller,on_delete=models.CASCADE)
   deliveryboy_status=models.IntegerField(default=0)

