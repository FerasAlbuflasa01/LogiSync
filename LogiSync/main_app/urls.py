    
from django.urls import path, include
from . import views



    
    
    

urlpatterns = [
    path('',views.home,name='home'),
    path('about/', views.about, name='about'),
    
    path('containers/', views.ContainerList.as_view(), name='container_list'),
    path('containers/<str:pk>/', views.ContainerDetail.as_view(), name='container_detail' ),
    path('containers/create/', views.ContainerCreate.as_view(), name='container_create' ),
    path('containers/<str:pk>/update/', views.ContainerUpdate.as_view(), name='container_update' ),
    path('containers/<str:pk>/delete/', views.ContainerDelete.as_view(), name='container_delete' ),
    
    # transport
    path('transports/',views.TransportList.as_view(), name='index' ),
    path('transports/show/<int:cat_id>/', views.TransportDetails.as_view, name='detail'),
    path('transports/create/', views.TransportCreate.as_view(), name='cat_create'),
    path('transports/<int:pk>/update/', views.TransportUpdate.as_view(), name='cats_update'),
    path('transports/<int:pk>/delete/', views.TransportDelete.as_view(), name='cats_delete'),


    #package
    path('packages/',views.ListView.as_view(),name='packages_index'),

    path('packages/<int:pk>',views.DetailView.as_view(),name='packages_detail'),

    path('packages/create',views.package_create,name='packages_create'),

    path('packages/<int:pk>/delete',views.PackageDelete.as_view(),name='packages_delete'),

    path('packages/<int:pk>/update',views.PackageUpdate.as_view(),name='packages_update'),
  
    # transportType
    path('transport/type/', views.TransportTypeCreate.as_view(), name='transport_type_create'),
    path('transport/type/<int:pk>/update/', views.TransportTypeUpdate.as_view(), name='transport_type_update'),
    path('transport/type/<int:pk>/delete/', views.TransportTypeDelete.as_view(), name='transport_type_delete'),

]