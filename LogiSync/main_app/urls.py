from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),

    #package
    path('packages/',views.ListView.as_view(),name='packages_index'),

    path('packages/<int:pk>',views.DetailView.as_view(),name='packages_detail'),

    path('packages/create',views.package_create,name='packages_create'),

    path('packages/<int:pk>/delete',views.PackageDelete.as_view(),name='packages_delete'),

    path('packages/<int:pk>/update',views.PackageUpdate.as_view(),name='packages_update'),
  
    path('transport/type/', views.TransportTypeCreate.as_view(), name='transport_type_create'),
    path('transport/type/<int:pk>/update/', views.TransportTypeUpdate.as_view(), name='transport_type_update'),
    path('transport/type/<int:pk>/delete/', views.TransportTypeDelete.as_view(), name='transport_type_delete'),
]