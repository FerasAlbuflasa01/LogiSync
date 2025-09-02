    
from django.urls import path, include
from . import views

urlpatterns = [

# -------------------------------------------------------------- home / about --------------------------------------------------------------
    path('',views.home,name='home'),
    path('about/', views.about, name='about'),
    
# -------------------------------------------------------------- containers --------------------------------------------------------------
    path('containers/', views.ContainerList, name='container_list'),
    path('containers/create/', views.ContainerCreate.as_view(), name='container_create' ),
    path('containers/<int:container_id>/', views.ContainerDetail, name='container_detail' ),
    path('transports/<int:transport_id>/getlocation', views.ContainerLocation, name='trasnport_location' ),
    path('containers/<int:pk>/update/', views.ContainerUpdate.as_view(), name='container_update' ),
    path('containers/<int:pk>/delete/', views.ContainerDelete.as_view(), name='container_delete' ),

    path('containers/<int:container_id>/assoc_package/<int:package_id>',views.assoc_package,name='assoc_package'),
    path('containers/<int:container_id>/unassoc_package/<int:package_id>',views.unassoc_package,name='unassoc_package'),
    
# -------------------------------------------------------------- Transport --------------------------------------------------------------
    path('transports/',views.TransportList, name='transport_list' ),
    path('transports/create/', views.TransportCreate.as_view(), name='transport_create'),
    path('transports/<int:transport_id>/', views.TransportDetails, name='transport_detail'),
    path('transports/<int:pk>/update/', views.TransportUpdate.as_view(), name='transports_update'),
    path('transports/<int:pk>/delete/', views.TransportDelete.as_view(), name='transports_delete'),

    path('transports/<int:transport_id>/assoc_container/<int:container_id>',views.assoc_container,name='assoc_container'),
    path('transports/<int:transport_id>/unassoc_container/<int:container_id>',views.unassoc_container,name='unassoc_container'),

# -------------------------------------------------------------- packages --------------------------------------------------------------
    path('packages/',views.PackageList.as_view(),name='packages_index'),
    path('packages/create',views.package_create,name='packages_create'),
    path('packages/<int:pk>',views.PackageDetails.as_view(),name='packages_detail'),
    path('packages/<int:pk>/delete',views.PackageDelete.as_view(),name='packages_delete'),
    path('packages/<int:pk>/update',views.PackageUpdate.as_view(),name='packages_update'),


# -------------------------------------------------------------- TransportType --------------------------------------------------------------
    path('transporttype/list/', views.TransportTypeList.as_view(), name='transport_type_list'),
    path('transporttype/create/', views.TransportTypeCreate.as_view(), name='transport_type_create'),
    path('transporttype/<int:pk>/update/', views.TransportTypeUpdate.as_view(), name='transport_type_update'),
    path('transporttype/<int:pk>/delete/', views.TransportTypeDelete.as_view(), name='transport_type_delete'),
    
# -------------------------------------------------------------- auth --------------------------------------------------------------
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.profile_detail, name='profile_detail'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),


# -------------------------------------------------------------- features --------------------------------------------------------------
    path('source/create/', views.SourceCreate.as_view(), name='source_create'),
    path('destination/create/', views.DestinationCreate.as_view(), name='destination_create'),
    
    # path('containers/active/', views.containers_active, name='containers_active'),
    path('qr_code/<int:pk>/', views.qr_code, name='qr_code'),

    path('transports/<int:transport_id>/checklist/', views.containers_checklist, name='containers_checklist'),
    path('transports/recieved', views.containers_recieved, name='containers_recieved'),



# -------------------------------------------------------------- locations(testing) --------------------------------------------------------------
    path('trasnports/<int:transport_id>/location', views.map, name='map'),

    path('location/save',views.location_save,name='location_save'),
    path('location/load',views.location_load,name='location_load'),
    # path('location/load',views.location_load,name='location_load'),

]