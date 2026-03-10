from django.urls import path
from Seller import views
app_name='Seller'
urlpatterns = [
     path('Homepage',views.Homepage,name="Homepage"),
    path('MyProfile',views.MyProfile,name="MyProfile"),
    path('editMyProfile',views.editMyProfile,name="editMyProfile"),
    path('changepassword',views.changepassword,name="changepassword"),
    path('Addproduct',views.Addproduct,name="Addproduct"),
    path('Addstock/<int:stk>',views.Addstock,name="Addstock"),
    path('Delstock/<int:did>/<int:stk>/', views.Delstock,name='Delstock'),

    path('Addgallery/<int:gall>',views.Addgallery,name="Addgallery"),
    path('Delgallery/<int:did>/<int:gall>', views.Delgallery, name='Delgallery'),

    path('MyComplaint',views.MyComplaint,name="MyComplaint"),
    path('delmycomplaint/<int:hhh>',views.delmycomplaint,name="delmycomplaint"),

    path('Complaint',views.Complaint,name="Complaint"),
    path('Deliveryboyregister',views.Deliveryboyregister,name="Deliveryboyregister"),
    path('Viewbooking',views.Viewbooking,name="Viewbooking"),
    path('AssignDeliveryboy/<int:id>',views.AssignDeliveryboy,name="AssignDeliveryboy"),
]