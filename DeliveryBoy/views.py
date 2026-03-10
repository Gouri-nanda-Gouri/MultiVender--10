from django.shortcuts import redirect, render
from Seller.models import *
from User.models import *
# Create your views here.
def Homepage(request):
        return render(request,'DeliveryBoy/Homepage.html')

def MyProfile(request):
        deliverydata=tbl_deliveryboy.objects.get(id=request.session['did'])
        return render(request,'DeliveryBoy/MyProfile.html',{"deliverydata":deliverydata})
     
def editMyProfile(request):
    editData=tbl_deliveryboy.objects.get(id=request.session['did'])

    if request.method == 'POST':
        name=request.POST.get('txtname')
        email=request.POST.get('txtemail')
        contact=request.POST.get('enterNo')
        address=request.POST.get('txtaddress')
        editData.deliveryboy_name=name
        editData.deliveryboy_email=email
        editData.deliveryboy_contact=contact
        editData.deliveryboy_address=address
        editData.save()
        return render(request,'DeliveryBoy/EditProfile.html',{'update':"inserted"})
    else:
        return render(request,'DeliveryBoy/EditProfile.html',{"editData":editData})      

def changepassword(request):
        changepassword=tbl_deliveryboy.objects.get(id=request.session['did'])
        if request.method=='POST':
                Oldpassword=request.POST.get('password')  
                Newpassword=request.POST.get('newpass')
                Retypepassword=request.POST.get('re_pass')
                if Oldpassword == changepassword.deliveryboy_password:
                        if Retypepassword == Newpassword:
                                changepassword.deliveryboy_password=Newpassword
                                changepassword.save()
                                return render(request,"DeliveryBoy/Changepassword.html",{"msg":"password changed"})
                        else:
                                return render(request,"DeliveryBoy/Changepassword.html",{"msg":"password error"})
                else:
                        return render(request,"DeliveryBoy/Changepassword.html",{"msg":"old pass erorr "})
        else:
                return render(request,'DeliveryBoy/Changepassword.html')


def AssignedTask(request):

    if 'did' not in request.session:
        return redirect("Guest:Login")

    deliveryboy = tbl_deliveryboy.objects.get(id=request.session['did'])

    task = tbl_assign.objects.filter(deliveryboy_id=deliveryboy)

    return render(request,"Deliveryboy/AssignedTask.html",{"task":task})


def AcceptDelivery(request,id):
    booking = tbl_booking.objects.get(id=id)
    booking.booking_status = 4
    booking.save()
    return redirect("Deliveryboy:AssignedTask")


def RejectDelivery(request,id):

    booking = tbl_booking.objects.get(id=id)

    # delete assign entry
    tbl_assign.objects.filter(booking_id=booking).delete()

    # change booking status
    booking.booking_status = 2
    booking.save()

    return redirect("Deliveryboy:AssignedTask")


def OutDelivery(request,id):
    booking = tbl_booking.objects.get(id=id)
    booking.booking_status = 5
    booking.save()
    return redirect("Deliveryboy:AssignedTask")


def CompleteDelivery(request,id):
    booking = tbl_booking.objects.get(id=id)
    booking.booking_status = 6
    booking.save()
    return redirect("Deliveryboy:AssignedTask")