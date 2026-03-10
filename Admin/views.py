from urllib import request

from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import*
# Create your views here.
def District(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_name')
        tbl_district.objects.create(district_name=name)
        return render(request,'Admin/District.html',{'update':"inserted"})
    else:
        return render(request,'Admin/District.html',{'District':dis})
    
def editDistrict(request,eid):
    editData=tbl_district.objects.get(id=eid)
    if request.method == 'POST':
        district=request.POST.get('txt_name')
        editData.district_name=district
        editData.save()
        return render(request,'Admin/District.html',{'update':"inserted"})
    else:
        return render(request,'Admin/District.html',{'editData':editData}) 

def delDistrict(request,dlt):
    tbl_district.objects.get(id=dlt).delete()   
    return render(request,'Admin/District.html',{'update':"Deleted"}) 

def Category(request):
    cat=tbl_category.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_nme')
        tbl_category.objects.create(category_name=name)
        return render(request,'Admin/Category.html',{'update':"inserted"})
    else:
        return render(request,'Admin/Category.html',{'Category':cat})
    
def editCategory(request,eid):
    editData=tbl_category.objects.get(id=eid)
    if request.method=='POST':
        Category=request.POST.get("txt_nme")
        editData.category_name=Category
        editData.save()
        return render(request,'Admin/Category.html',{'update':"inserted"})
    else:
        return render(request,'Admin/Category.html',{'editData':editData})



def delcategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return render(request,'Admin/Category.html',{'update':"Deleted"})

def Registration(request):
    reg=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_pass')
        tbl_admin.objects.create(admin_name=name,admin_email=email,admin_password=password)
        return render(request,'Admin/Registration.html',{'msg':"inserted"})
    else:
        return render(request,'Admin/Registration.html',{'Registration':reg})
    
def editRegistration(request,eid):
    editData=tbl_admin.objects.get(id=eid)    
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_pass')
        editData.admin_name=name
        editData.admin_email=email
        editData.admin_password=password
        editData.save()
        return render(request,'Admin/Registration.html',{'msg':"inserted"})
    else:
        return render(request,'Admin/Registration.html',{'editData':editData})
        



def delRegistration(request,hll):
    tbl_admin.objects.get(id=hll).delete()
    return render(request,'Admin/Registration.html',{'msg':'deleted'})

def Place(request):
    placeData=tbl_place.objects.all()
    districtData=tbl_district.objects.all()
    if request.method == 'POST':
        place=request.POST.get('txt_name')
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(district=district,place_name=place)
        return render(request,'Admin/Place.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/Place.html',{'districtData':districtData,'placeData':placeData})
    
def delPlace(request,edd):
    tbl_place.objects.get(id=edd).delete()
    return render(request,'Admin/Place.html',{'msg':'deleted'})

def editPlace(request,idd):
    editData=tbl_place.objects.get(id=idd)
    district=tbl_district.objects.all()
    if request.method=='POST':
        place=request.POST.get('txt_name')
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        editData.district=district
        editData.place_name=place
        editData.save()
        return render(request,'Admin/Place.html',{'update':"insert"})
    else:
        return render(request,'Admin/Place.html',{'editData':editData,'districtData':district})
    

def Subcategory(request):
    CategoryData=tbl_category.objects.all()
    subCategoryData=tbl_subcategory.objects.all()
    if request.method == 'POST':
        Subcategory=request.POST.get('txt_name')
        Category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        tbl_subcategory.objects.create(category=Category,subcategory_name=Subcategory)
        return render(request,'Admin/Subcategory.html',{'msg':"inserted"})
    else:
        return render(request,'Admin/Subcategory.html',{'CategoryData':CategoryData,"subCategoryData":subCategoryData})
    
def delSubcategory(request,hhh):
    tbl_subcategory.objects.get(id=hhh).delete()
    return render(request,'Admin/Subcategory.html',{'msg':'deleted'})

def editSubcategory(request,edt):
    editData=tbl_subcategory.objects.get(id=edt)
    categoryData=tbl_category.objects.all()
    if request.method=='POST':
        Subcategory=request.POST.get("txt_name")
        Category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        editData.category=Category
        editData.subcategory_name=Subcategory
        editData.save()
        return render(request,'Admin/Subcategory.html',{'update':"inserted"})
    else:
        return render(request,'Admin/Subcategory.html',{'editData':editData,'CategoryData':categoryData})
    

def Homepage(request):

    total_users = tbl_user.objects.count()
    total_sellers = tbl_seller.objects.count()
    total_products = tbl_product.objects.count()
    total_deliveryboys = tbl_deliveryboy.objects.count()
    total_bookings = tbl_booking.objects.count()
    pending_deliveryboys = tbl_deliveryboy.objects.filter(deliveryboy_status=0).count()

    recent_booking = tbl_booking.objects.all().order_by('-booking_date')[:5]

    return render(request,'Admin/Homepage.html',{
        "total_users":total_users,
        "total_sellers":total_sellers,
        "total_products":total_products,
        "total_deliveryboys":total_deliveryboys,
        "total_bookings":total_bookings,
        "pending_deliveryboys":pending_deliveryboys,
        "recent_booking":recent_booking
    })
def Userlist(request):
    pending = tbl_user.objects.filter(user_status=0)
    accepted = tbl_user.objects.filter(user_status=1)
    rejected = tbl_user.objects.filter(user_status=2)

    return render(request,"Admin/Userlist.html",{
    "pending":pending,
    "accepted":accepted,
    "rejected":rejected
     })

def Viewcomplaint(request):
    complaint=tbl_complaint.objects.all()
    return render(request,'Admin/Viewcomplaint.html',{'complaint':complaint})

def Reply(request,id):
    complaint=tbl_complaint.objects.get(id=id)
    if request.method == "POST":
        reply=request.POST.get("txt_reply")
        complaint.complaint_reply=reply
        complaint.complaint_status = 1
        complaint.save()
        return  redirect("Admin:Viewcomplaint")
    return render(request,'Admin/Reply.html')


def Accept(request,act):
    accuser=tbl_user.objects.get(id=act)
    accuser.user_status =1
    accuser.save()
    return render(request,'Admin/Userlist.html',{'msg':"Accepted"})

def reject(request,rjt):
    rejuser=tbl_user.objects.get(id=rjt)
    rejuser.user_status =2
    rejuser.save()
    return render(request,'Admin/Userlist.html',{'msg':"Rejected"})


def Deliveryboylist(request):
    pending = tbl_deliveryboy.objects.filter(deliveryboy_status=0)
    accepted = tbl_deliveryboy.objects.filter(deliveryboy_status=1)
    rejected = tbl_deliveryboy.objects.filter(deliveryboy_status=2)

    return render(request,"Admin/Deliveryboylist.html",{
    "pending":pending,
    "accepted":accepted,
    "rejected":rejected
    })

def Acceptboy(request,act):
    accboy=tbl_deliveryboy.objects.get(id=act)
    accboy.deliveryboy_status =1
    accboy.save()
    return render(request,'Admin/Deliveryboylist.html',{'msg':"Accepted"})

def rejectboy(request,rjt):
    rejboy=tbl_deliveryboy.objects.get(id=rjt)
    rejboy.deliveryboy_status =2
    rejboy.save()
    return render(request,'Admin/Deliveryboylist.html',{'msg':"Rejected"})

def Sellerlist(request):

    pending = tbl_seller.objects.filter(seller_status=0)
    accepted = tbl_seller.objects.filter(seller_status=1)
    rejected = tbl_seller.objects.filter(seller_status=2)

    return render(request,'Admin/Sellerlist.html',{
        "pending":pending,
        "accepted":accepted,
        "rejected":rejected
    })


def Acceptseller(request,id):
    seller = tbl_seller.objects.get(id=id)
    seller.seller_status = 1
    seller.save()
    return render(request,'Admin/Sellerlist.html',{'msg':"Accepted"})


def Rejectseller(request,id):
    seller = tbl_seller.objects.get(id=id)
    seller.seller_status = 2
    seller.save()
    return render(request,'Admin/Sellerlist.html',{'msg':"Rejected"})


def logout(request):
    del request.session['aid']
    return redirect('Guest:Login')