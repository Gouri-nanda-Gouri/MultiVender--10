from django.urls import path
from DeliveryBoy import views
app_name='Deliveryboy'
urlpatterns = [
     path('Homepage',views.Homepage,name="Homepage"),
    path('MyProfile',views.MyProfile,name="MyProfile"),
    path('editMyProfile',views.editMyProfile,name="editMyProfile"),
    path('changepassword',views.changepassword,name="changepassword"),
    path('AssignedTask/',views.AssignedTask,name="AssignedTask"),

    path('AcceptDelivery/<int:id>',views.AcceptDelivery,name="AcceptDelivery"),
path('RejectDelivery/<int:id>',views.RejectDelivery,name="RejectDelivery"),
path('OutDelivery/<int:id>',views.OutDelivery,name="OutDelivery"),
path('CompleteDelivery/<int:id>',views.CompleteDelivery,name="CompleteDelivery"),
   
]