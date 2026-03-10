from django.urls import path
from User import views
app_name='User'
urlpatterns = [
    path('Homepage/',views.Homepage,name="Homepage"),
    path('MyProfile/',views.MyProfile,name="MyProfile"),
    path('editMyProfile/',views.editMyProfile,name="editMyProfile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('Viewproducts/',views.viewproduct,name="Viewproducts"),

    path('AddCart/<int:pid>/', views.AddCart, name='AddCart'),
    path('MyCart/', views.MyCart, name='MyCart'),
    path('DelCart/<int:did>/', views.DelCart, name='DelCart'),
    path('CartQty/', views.CartQty, name='CartQty'),


    path("payment/",views.payment,name="payment"),
    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'),

    path('MyComplaint',views.MyComplaint,name="MyComplaint"),
    path('delmycomplaint/<int:hhh>',views.delmycomplaint,name="delmycomplaint"),

    path('Complaint',views.Complaint,name="Complaint"),
    path("feedback/",views.feedback,name="feedback"),
    path('delfeedback/<int:hhh>',views.delfeedback,name="delfeedback"),

    path('rating/<int:mid>',views.rating,name="rating"), 
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),
    path('Viewgallery/<int:id>/', views.viewgallery, name='viewgallery'),

    path('ViewOrders/',views.ViewOrders,name="ViewOrders"),

]