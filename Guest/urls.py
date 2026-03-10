from django.urls import path
from Guest import views
app_name='Guest'
urlpatterns = [
    path('Userregistration',views.Userregistration,name="Userregistration"),
    path("ajaxplace/",views.ajaxplace,name='ajaxplace'),
    path('Login/',views.Login,name='Login'),
    path('index/',views.index,name='index') ,
    path('Sellerregistration/',views.Sellerregistration,name='Sellerregistration') ,
]