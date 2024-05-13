from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vendor/',views.VendorView.vendor_view,name='vendors-view'),
    path('vendor/create/',views.VendorView.vendor_create,name='vendor-create'),
    path('vendor/detail/<pk>',views.VendorView.vendor_detail,name='vendor-detail'),
    path('fruit/',views.FruitsView.view_fruits,name='fruits'),
    path('fruit/create/',views.FruitsView.create_fruits,name='add-fruits'),
    path('fruit/update/<pk>',views.FruitsView.update_fruits,name='update-fruits'),
    path('fruit/delete/<pk>',views.FruitsView.delete_fruits,name='delete-fruits'),
    path('fruit/bin/',views.FruitsView.bin_fruits,name='bin-fruits'),
    path('fruit/restore/<pk>',views.FruitsView.restore_fruits,name='restore-fruits'),
    path('vegitable/',views.VegitablesView.view_vegitables,name='vegitables'),
    path('vegitable/create/',views.VegitablesView.create_vegitables,name='add-vegitables'),
    path('vegitable/update/<pk>',views.VegitablesView.update_vegitables,name='update-vegitables'),
    path('vegitable/delete/<pk>',views.VegitablesView.delete_vegitables,name='delete-vegitables'),
    path('vegitable/bin/',views.VegitablesView.bin_vegitables,name='bin-vegitables'),
    path('vegitable/restore/<pk>',views.VegitablesView.restore_vegitables,name='restore-vegitables'),
    path('store/',views.store,name='store'),
    path('store/create/',views.store_create,name='create_store'),
    path('store/detail/<pk>',views.store_detail,name='store_detail'),
]

