from django.shortcuts import render,redirect
from Guest.models import *
from Seller.models import*
from User.models import*
from django.db.models import Sum
from datetime import date,datetime
from django.http import JsonResponse

# Create your views here.
def Homepage(request):
        return render(request,'User/Homepage.html')

def MyProfile(request):
        userdata=tbl_user.objects.get(id=request.session['uid'])
        return render(request,'User/MyProfile.html',{"userdata":userdata})
     
def editMyProfile(request):
    editData=tbl_user.objects.get(id=request.session['uid'])

    if request.method == 'POST':
        name=request.POST.get('txtname')
        email=request.POST.get('txtemail')
        contact=request.POST.get('enterNo')
        address=request.POST.get('txtaddress')
        editData.user_name=name
        editData.user_email=email
        editData.user_contact=contact
        editData.user_address=address
        editData.save()
        return render(request,'User/EditProfile.html',{'update':"inserted"})
    else:
        return render(request,'User/EditProfile.html',{"editData":editData})      

def changepassword(request):
        changepassword=tbl_user.objects.get(id=request.session['uid'])
        if request.method=='POST':
                Oldpassword=request.POST.get('password')  
                Newpassword=request.POST.get('newpass')
                Retypepassword=request.POST.get('re_pass')
                if Oldpassword == changepassword.user_password:
                        if Retypepassword == Newpassword:
                                changepassword.user_password=Newpassword
                                changepassword.save()
                                return render(request,"User/Changepassword.html",{"msg":"password changed"})
                        else:
                                return render(request,"User/Changepassword.html",{"msg":"password error"})
                else:
                        return render(request,"User/Changepassword.html",{"msg":"old pass erorr "})
        else:
                return render(request,'User/Changepassword.html')
        
def viewproduct(request):
        product=tbl_product.objects.all()
        return render(request,'User/Viewproducts.html',{'product':product})
        

def AddCart(request,pid):
    productdata=tbl_product.objects.get(id=pid)
    userdata=tbl_user.objects.get(id=request.session["uid"])
    bookingcount=tbl_booking.objects.filter(user_id=userdata,booking_status=0).count()
    if bookingcount>0:
        bookingdata=tbl_booking.objects.get(user_id=userdata,booking_status=0)
        cartcount=tbl_cart.objects.filter(booking_id=bookingdata,product_id=productdata).count()
        if cartcount>0:
            msg="Already added"
            return render(request,"User/Viewproducts.html",{'msg':msg})
        else:
            tbl_cart.objects.create(booking_id=bookingdata,product_id=productdata)
            msg="Added To cart"
            return render(request,"User/Viewproducts.html",{'msg':msg})
    else:
        bookingdata = tbl_booking.objects.create(user_id=userdata)
        tbl_cart.objects.create(booking_id=tbl_booking.objects.get(id=bookingdata.id),product_id=productdata)
        msg="Added To cart"
        return render(request,"User/Viewproducts.html",{'msg':msg})
    
def MyCart(request):
    if "uid" in request.session:
        if request.method=="POST":
            bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
            bookingdata.booking_amount=float(request.POST.get("carttotalamt"))
            bookingdata.booking_status=1
            bookingdata.save()
            cart = tbl_cart.objects.filter(booking_id=bookingdata)
            for i in cart:
                i.cart_status = 1
                i.save()
            return redirect("User:payment")
        else:
            bookcount = tbl_booking.objects.filter(user_id=request.session["uid"],booking_status=0).count()
            if bookcount > 0:
                book = tbl_booking.objects.get(user_id=request.session["uid"],booking_status=0)
                request.session["bookingid"] = book.id
                cart = tbl_cart.objects.filter(booking_id=book)
                for i in cart:
                    total_stock = tbl_stock.objects.filter(product_id=i.product_id.id).aggregate(total=Sum('stock_count'))['total']
                    total_cart = tbl_cart.objects.filter(product_id=i.product_id.id, cart_status=1).aggregate(total=Sum('cart_quantity'))['total']
                    # print(total_stock)
                    # print(total_cart)
                    if total_stock is None:
                        total_stock = 0
                    if total_cart is None:
                        total_cart = 0
                    total =  total_stock - total_cart
                    i.total_stock = total
                return render(request,"User/MyCart.html",{'cartdata':cart})
            else:
                return render(request,"User/MyCart.html")
    else:
        return redirect("Guest:Login")
   
def DelCart(request,did):
   tbl_cart.objects.get(id=did).delete()
   return redirect("User:MyCart")

def CartQty(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_quantity=qty
   cartdata.save()
   return redirect("User:MyCart")

def payment(request):
    bookingdata = tbl_booking.objects.get(id=request.session["bookingid"])
    amount = bookingdata.booking_amount

    if request.method == "POST":
        bookingdata.booking_status = 2
        bookingdata.save()

        cart = tbl_cart.objects.filter(booking_id=bookingdata)
        for i in cart:
            i.cart_status = 2
            i.save()

        return redirect("User:loader")
    else:
            return render(request,"User/Payment.html",{'amount':amount})

def loader(request):
    if 'uid' not in request.session:
        return redirect('Guest:login')
    return render(request,"User/Loader.html")

def paymentsuc(request):
    if 'uid' not in request.session:
        return redirect('Guest:login')
    return render(request,"User/Payment_suc.html")

def MyComplaint(request):
    ComplaintData=tbl_complaint.objects.filter(user_id=request.session['uid'])
    return render(request,'User/MyComplaint.html',{'ComplaintData':ComplaintData})

def delmycomplaint(request,hhh):
    tbl_complaint.objects.get(id=hhh).delete()
    return render(request,'User/MyComplaint.html',{'msg':'deleted'})

def Complaint(request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        title=request.POST.get('txt_title')
        content=request.POST.get('txt_content')      
        tbl_complaint.objects.create(user_id=userdata,complaint_title=title,complaint_content=content)
        return render(request,'User/Complaint.html', {"msg":"Complaint Registered"})
    else:
        return render(request,'User/Complaint.html',)


def feedback(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    
    feedbackdata=tbl_feedback.objects.all()
    if request.method == "POST":
        tbl_feedback.objects.create(feedback_content=request.POST.get("txt_content"),user_id=tbl_user.objects.get(id=request.session["uid"]))
        return render(request,"User/Feedback.html",{"msg":"Feedback Send Sucessfully.."})
    else:
        return render(request,"User/Feedback.html",{'feedbackdata':feedbackdata})
    
def delfeedback(request,hhh):
    tbl_feedback.objects.get(id=hhh).delete()
    return render(request,'User/Feedback.html',{'msg':'deleted'})
        

def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(product=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(product=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})     

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(user=tbl_user.objects.get(id=request.session['uid']),user_review=user_review,rating_data=rating_data,product=tbl_product.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(product=pid).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(product=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(product=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)

def viewgallery(request,id):
    galleryData=tbl_gallery.objects.filter(product_id=id)
    return render(request,'User/Viewgallery.html',{'data':galleryData})

def ViewOrders(request):

    cart = tbl_cart.objects.filter(
        booking_id__user_id=request.session['uid']
    )

    return render(request,"User/ViewOrders.html",{"cart":cart})