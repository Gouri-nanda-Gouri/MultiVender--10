from django.urls import path
from Admin import views
app_name='Admin'
urlpatterns = [
    path('District',views.District,name="District"),
    path('delDistrict/<int:dlt>',views.delDistrict,name="delDistrict"),
    path('editDistrict/<int:eid>',views.editDistrict,name="editDistrict"),
    path('Category',views.Category,name="Category"),
    path('delcategory/<int:did>',views.delcategory,name="delcategory"),
    path('editcategory/<int:eid>',views.editCategory,name="editcategory"),

    path('Registration',views.Registration,name="Registration"),
    path('delRegistration/<int:hll>',views.delRegistration,name="delRegistration"),
    path('editRegistration/<int:eid>',views.editRegistration,name="editRegistration"),
    path('Place',views.Place,name="Place"),
    path('delPlace/<int:edd>',views.delPlace,name="delPlace"),
    path('editPlace/<int:idd>',views.editPlace,name="editPlace"),
    path('Subcategory',views.Subcategory,name="Subcategory"),
    path('delSubcategory/<int:hhh>',views.delSubcategory,name="delSubcategory"),
    path('editSubcategory/<int:edt>',views.editSubcategory,name="editSubcategory"),
    
    path('Homepage/',views.Homepage,name="Homepage"),
    path('Userlist/',views.Userlist,name="Userlist"),
    path('Viewcomplaint/',views.Viewcomplaint,name="Viewcomplaint"),
    path('Reply/<int:id>',views.Reply,name="Reply"),
    path('Accept/<int:act>',views.Accept,name="Accept"),
    path('reject/<int:rjt>',views.reject,name="reject"),
    path('Deliveryboylist',views.Deliveryboylist,name="Deliveryboylist"),
    path('Acceptboy/<int:act>',views.Acceptboy,name="Acceptboy"),
    path('rejectboy/<int:rjt>',views.rejectboy,name="rejectboy"),

    path('logout',views.logout,name="logout"),

    path('Sellerlist/',views.Sellerlist,name="Sellerlist"),
    path('Acceptseller/<int:id>',views.Acceptseller,name="Acceptseller"),
    path('Rejectseller/<int:id>',views.Rejectseller,name="Rejectseller"),

]
