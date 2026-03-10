from django.shortcuts import render,redirect
from Guest.models import *
from Seller.models import *
from User.models import *
# Create your views here.
def Homepage(request):
        return render(request,'Seller/Homepage.html')

def MyProfile(request):
        sellerdata=tbl_seller.objects.get(id=request.session['sid'])
        return render(request,'Seller/MyProfile.html',{"sellerdata":sellerdata})
     
def editMyProfile(request):
    editData=tbl_seller.objects.get(id=request.session['sid'])

    if request.method == 'POST':
        name=request.POST.get('txtname')
        email=request.POST.get('txtemail')
        contact=request.POST.get('enterNo')
        address=request.POST.get('txtaddress')
        editData.seller_name=name
        editData.seller_email=email
        editData.seller_contact=contact
        editData.seller_address=address
        editData.save()
        return render(request,'Seller/EditProfile.html',{'update':"inserted"})
    else:
        return render(request,'Seller/EditProfile.html',{"editData":editData})      

def changepassword(request):
        changepassword=tbl_seller.objects.get(id=request.session['sid'])
        if request.method=='POST':
                Oldpassword=request.POST.get('password')  
                Newpassword=request.POST.get('newpass')
                Retypepassword=request.POST.get('re_pass')
                if Oldpassword == changepassword.seller_passsword:
                        if Retypepassword == Newpassword:
                                changepassword.seller_passsword=Newpassword
                                changepassword.save()
                                return render(request,"Seller/Changepassword.html",{"msg":"password changed"})
                        else:
                                return render(request,"Seller/Changepassword.html",{"msg":"password error"})
                else:
                        return render(request,"Seller/Changepassword.html",{"msg":"old pass erorr "})
        else:
                return render(request,'Seller/Changepassword.html')
# Create your views here.

def Addproduct(request):
        sellerdata=tbl_seller.objects.get(id=request.session['sid'])
        productdata=tbl_product.objects.all()
        Category=tbl_category.objects.all()
        if request.method=="POST":
            Name=request.POST.get("txt_name")
            Details=request.POST.get("enter_details")
            Price=request.POST.get("enter_price")
            Category=tbl_category.objects.get(id=request.POST.get('sel_Category'))      
            Photo=request.FILES.get("choosefile")
            tbl_product.objects.create(product_name=Name,product_details=Details,product_photo=Photo,product_price=Price,category_id=Category,seller_id=sellerdata)
            return render(request,"Seller/Addproduct.html",{'msg':"inserted"})
        else:
            return render(request,"Seller/Addproduct.html",{"productdata":productdata,'Category':Category,'sellerdata':sellerdata})
          

def Addstock(request,stk):
       product=tbl_product.objects.get(id=stk)
       stockdata=tbl_stock.objects.all()
       if request.method == 'POST':
              stockcount=request.POST.get('count_stock')
              tbl_stock.objects.create(stock_count=stockcount,product_id=product)
              return render(request,'Seller/Addstock.html',{"stk":stk})
       else:
             return render(request,'Seller/Addstock.html',{'product':product,'stockdata':stockdata,"stk":stk})
       
def Delstock(request,did,stk):
   tbl_stock.objects.get(id=did).delete()
   return render(request,'Seller/Addstock.html',{'msg':"stock dlt",'stk':stk})

def Addgallery(request,gall):
    product=tbl_product.objects.get(id=gall)
    gallerydata=tbl_gallery.objects.filter(product_id=gall)
    if request.method == 'POST':
        gallerycount=request.FILES.get('file_name')
        tbl_gallery.objects.create(gallery_file=gallerycount,product_id=product)
        return render(request,'Seller/Addgallery.html',{'gall':gall,'msg':"Gallery Added"})
    else:
        return render(request,'Seller/Addgallery.html',{'product':product,'gallerydata':gallerydata,'gall':gall})
    
def Delgallery(request,did,gall):
   tbl_gallery.objects.get(id=did).delete()
   return render(request,'Seller/Addgallery.html',{'msg':"Gallery dlt",'gall':gall})

       
def MyComplaint(request):
    ComplaintData=tbl_complaint.objects.filter(seller_id=request.session['sid'])
    return render(request,'Seller/MyComplaint.html',{'ComplaintData':ComplaintData})

def delmycomplaint(request,hhh):
    tbl_complaint.objects.get(id=hhh).delete()
    return render(request,'Seller/MyComplaint.html',{'msg':'deleted'})

def Complaint(request):
    userdata=tbl_seller.objects.get(id=request.session['sid'])
    if request.method=="POST":
        title=request.POST.get('txt_title')
        content=request.POST.get('txt_content')      
        tbl_complaint.objects.create(seller_id=userdata,complaint_title=title,complaint_content=content)
        return render(request,'Seller/Complaint.html', {"msg":"Complaint Registered"})
    else:
        return render(request,'Seller/Complaint.html')
    
def Deliveryboyregister(request):
    seller=tbl_seller.objects.get(id=request.session['sid'])
    dis=tbl_district.objects.all()
    if request.method =="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contacts=request.POST.get('txt_no')
        address=request.POST.get('txtaddress')
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        photo=request.FILES.get("choosefile")
        proof=request.FILES.get('choosefile')
        password=request.POST.get("enter_pass")
        repassword=request.POST.get("conform_pass")
        if password==repassword:
            tbl_deliveryboy.objects.create(deliveryboy_name=name,deliveryboy_email=email,deliveryboy_contact=contacts,deliveryboy_address=address,deliveryboy_photo=photo,deliveryboy_proof=proof,deliveryboy_password=password,place_id=place,seller_id=seller)
            return render(request,'Seller/Deliveryboyregister.html',{'msg':'inserted'})
        else:
            return render(request,'Seller/Deliveryboyregister.html',{'msg':'password not match'})
    else:
        return render(request,'Seller/Deliveryboyregister.html',{'dis':dis,})
    
def ajaxplace(request):
    districtid=tbl_district.objects.get(id=request.GET.get('did'))
    place=tbl_place.objects.filter(district=districtid)
    return render(request,"Seller/AjaxPlace.html",{'place':place})

def Viewbooking(request):
     cart=tbl_cart.objects.filter(cart_status=2)
     return render(request,'Seller/Viewbooking.html',{'cart':cart})

def AssignDeliveryboy(request,id):
     delboy = tbl_deliveryboy.objects.filter(seller_id=request.session['sid'],deliveryboy_status=1)
     if request.method == "POST":
        booking= tbl_booking.objects.get(id=id)
        booking.booking_status=3
        booking.save()
        tbl_assign.objects.create(deliveryboy_id=tbl_deliveryboy.objects.get(id=request.POST.get("sel_delivery")),booking_id=booking)
        return redirect("Seller:Viewbooking")
     else:
          return render(request,'Seller/ViewDeliveryboy.html',{'delboy':delboy})