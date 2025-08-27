from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),

    #package
    path('packages/',views.PackageList.as_view(),name='packages_index'),

    path('packages/<int:pk>',views.PackageDetails.as_view(),name='packages_detail'),

    path('packages/create',views.package_create,name='packages_create'),

    path('packages/<int:pk>/delete',views.PackageDelete.as_view(),name='packages_delete'),

    path('packages/<int:pk>/update',views.PackageUpdate.as_view(),name='packages_update'),
    
]