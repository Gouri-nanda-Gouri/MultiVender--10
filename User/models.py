from django.db import models
from Seller.models import*
from Guest.models  import *
# Create your models here.
class tbl_booking(models.Model):
    booking_date=models.DateField(auto_now_add=True)
    booking_amount=models.IntegerField(default=0)
    booking_status=models.IntegerField(default=0)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=30)
    complaint_content=models.CharField(max_length=30)
    complaint_reply=models.CharField(max_length=30)
    complaint_status=models.IntegerField(default=0)
    complaint_date=models.DateField(auto_now_add=True)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    seller_id=models.ForeignKey(tbl_seller,on_delete=models.CASCADE,null=True)

class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=30)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_cart(models.Model):
    cart_quantity=models.IntegerField(default=0)
    product_id=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    booking_id=models.ForeignKey(tbl_booking,on_delete=models.CASCADE)
    cart_status=models.IntegerField(default=0)

class tbl_payment(models.Model):
    payment_amount = models.FloatField(default=100)
    payment_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    
class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    user_review=models.CharField(max_length=500)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)    

class tbl_assign(models.Model):
   assign_date=models.DateField(auto_now_add=True)
   deliveryboy_id=models.ForeignKey(tbl_deliveryboy,on_delete=models.CASCADE)
   booking_id=models.ForeignKey(tbl_booking,on_delete=models.CASCADE)