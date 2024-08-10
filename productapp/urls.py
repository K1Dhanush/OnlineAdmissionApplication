#from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('listcategory',views.listCategory,name='listcategory' ),
    path('insertcategory/',views.insertCategory,name='insertcategory'),
    path('insertcategory/<int:id>',views.insertCategory,name='editcategory'),#edit C
    path('deletecategory/<int:id>',views.deleteCategory,name='deletecategory'),#delete C
    path('listproduct',views.listProduct,name='listproduct' ),
    path('insertproduct/',views.insertProduct,name='insertproduct'),
    path('insertproduct/<int:id>',views.insertProduct,name='editproduct'), #edit P
    path('deleteproduct/<int:id>',views.deleteProduct,name='deleteproduct'), #delete P
]