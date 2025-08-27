    
from django.urls import path, include
from . import views

urlpatterns = [

    # home / about 

    path('',views.home,name='home'),
    path('about/', views.about, name='about'),
    
    #Containers
    path('containers/', views.ContainerList.as_view(), name='container_list'),
    path('containers/create/', views.ContainerCreate.as_view(), name='container_create' ),
    path('containers/<int:container_id>/', views.ContainerDetail, name='container_detail' ),

    path('containers/<int:pk>/update/', views.ContainerUpdate.as_view(), name='container_update' ),
    path('containers/<int:pk>/delete/', views.ContainerDelete.as_view(), name='container_delete' ),

    path('containers/<int:container_id>/assoc_package/<int:package_id>',views.assoc_package,name='assoc_package'),
    path('containers/<int:container_id>/unassoc_package/<int:package_id>',views.unassoc_package,name='unassoc_package'),
    

    # transport
    path('transports/',views.TransportList.as_view(), name='index' ),
    path('transports/<int:pk>/', views.TransportDetails.as_view, name='detail'),
    path('transports/create/', views.TransportCreate.as_view(), name='transport_create'),
    path('transports/<int:pk>/update/', views.TransportUpdate.as_view(), name='transports_update'),
    path('transports/<int:pk>/delete/', views.TransportDelete.as_view(), name='transports_delete'),


    #package
    path('packages/',views.PackageList.as_view(),name='packages_index'),

    path('packages/<int:pk>',views.PackageDetails.as_view(),name='packages_detail'),

    path('packages/create',views.package_create,name='packages_create'),

    path('packages/<int:pk>/delete',views.PackageDelete.as_view(),name='packages_delete'),

    path('packages/<int:pk>/update',views.PackageUpdate.as_view(),name='packages_update'),
  
    # transportType
    path('transport/type/', views.TransportTypeCreate.as_view(), name='transport_type_create'),
    path('transport/type/<int:pk>/update/', views.TransportTypeUpdate.as_view(), name='transport_type_update'),
    path('transport/type/<int:pk>/delete/', views.TransportTypeDelete.as_view(), name='transport_type_delete'),
    
    #auth
    path('accounts/signup/', views.signup, name='signup'),


]