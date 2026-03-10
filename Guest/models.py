from django.db import models
from Admin.models import *
# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=30)
    user_email=models.CharField(max_length=30)
    user_contact=models.CharField(max_length=30)
    user_address=models.CharField(max_length=30)
    user_photo= models.FileField(upload_to="Assets/User/")
    user_password=models.CharField(max_length=60)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    user_status=models.IntegerField(default=0)

class tbl_seller(models.Model):
    seller_name=models.CharField(max_length=30)
    seller_email=models.CharField(max_length=30)
    seller_contact=models.CharField(max_length=30)
    seller_address=models.CharField(max_length=30)
    seller_photo=models.FileField(upload_to="Assets/Seller/Photo/")
    seller_proof=models.FileField(upload_to="Assets/Seller/proof/")
    seller_passsword=models.CharField(max_length=60)
    seller_status=models.IntegerField(default=0)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)


