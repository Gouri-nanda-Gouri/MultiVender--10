from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import*
from Seller.models import*
# Create your views here.
def Userregistration(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        name=request.POST.get("txtname")
        email=request.POST.get("txtemail")
        contacts=request.POST.get("txtphone")
        address=request.POST.get("txtaddress")
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        photo=request.FILES.get("choosefile")
        password=request.POST.get("enter_pass")
        repassword=request.POST.get("conform_pass")
        if password==repassword:
            tbl_user.objects.create(user_name=name,user_email=email,user_contact=contacts,user_address=address,user_photo=photo,user_password=password,place=place)
            return render(request,'Guest/Userregistration.html',{'msg':'inserted'})
        else:
            return render(request,'Guest/Userregistration.html',{'msg':'password not match'})
    else:
        return render(request,'Guest/Userregistration.html',{'dis':dis})
    
def ajaxplace(request):
    districtid=tbl_district.objects.get(id=request.GET.get('did'))
    place=tbl_place.objects.filter(district=districtid)
    return render(request,"Guest/AjaxPlace.html",{'place':place})

def Login(request):
    if request.method=="POST":
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_pass")
        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        sellercount=tbl_seller.objects.filter(seller_email=email,seller_passsword=password).count()
        deliveryboycount=tbl_deliveryboy.objects.filter(deliveryboy_email=email,deliveryboy_password=password).count()
        if admincount>0:
            admindata=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admindata.id
            return redirect('Admin:Homepage')
        elif usercount>0:
            userData=tbl_user.objects.get(user_email=email,user_password=password)
            if userData.user_status == 1:
                request.session['uid'] = userData.id
                return redirect('User:Homepage')
            elif userData.user_status == 0:
                return render(request,"Guest/Login.html",{"msg":"Account Pending Approval"})
            elif userData.user_status == 2:
                return render(request,"Guest/Login.html",{"msg":"Account Rejected"})
        elif sellercount>0:
            SellerData=tbl_seller.objects.get(seller_email=email,seller_passsword=password)
            if SellerData.seller_status == 1:
                request.session['sid'] = SellerData.id
                return redirect('Seller:Homepage')
            elif SellerData.seller_status == 0:
                return render(request,"Guest/Login.html",{"msg":"Account Pending Approval"})
            elif SellerData.seller_status == 2:
                return render(request,"Guest/Login.html",{"msg":"Account Rejected"})
            
        elif deliveryboycount>0:
            DeliveryBoyData=tbl_deliveryboy.objects.get(deliveryboy_email=email,deliveryboy_password=password)
            if DeliveryBoyData.deliveryboy_status == 1:
                request.session['did'] = DeliveryBoyData.id
                return redirect('DeliveryBoy:Homepage')
            elif DeliveryBoyData.delivery_boy_status == 0:
                return render(request,"Guest/Login.html",{"msg":"Account Pending Approval"})
            elif DeliveryBoyData.delivery_boy_status == 2:
                return render(request,"Guest/Login.html",{"msg":"Account Rejected"})

        else:
            return render(request,"Guest/Login.html")

    else:
            return render(request,"Guest/Login.html")
    
def Sellerregistration(request):
        dis=tbl_district.objects.all()
        if request.method=="POST":
            name=request.POST.get("txt_name")
            email=request.POST.get("txt_email")
            contacts=request.POST.get("txt_no")
            address=request.POST.get("txtaddress")
            place=tbl_place.objects.get(id=request.POST.get("sel_place"))
            photo=request.FILES.get("choosefile")
            password=request.POST.get("password")
            proof=request.FILES.get("enter_proof")
        
            tbl_seller.objects.create(seller_name=name,seller_email=email,seller_contact=contacts,seller_address=address,seller_photo=photo,seller_passsword=password,place=place,seller_proof=proof)
            return render(request,"Guest/Sellerregistration.html",{'msg':'inserted'})
        else:
            return render(request,"Guest/Sellerregistration.html",{'dis':dis})
             
             


def index(request):
     return render(request,"Guest/index.html")