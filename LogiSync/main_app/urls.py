    
from django.urls import path, include
from . import views

urlpatterns = [

# -------------------------------------------------------------- home / about --------------------------------------------------------------
    path('',views.home,name='home'),
    path('about/', views.about, name='about'),
    
# -------------------------------------------------------------- containers --------------------------------------------------------------
    path('containers/', views.ContainerList.as_view(), name='container_list'),
    path('containers/create/', views.ContainerCreate.as_view(), name='container_create' ),
    path('containers/<int:pk>/', views.ContainerDetail.as_view(), name='container_detail' ),
    path('containers/<int:pk>/update/', views.ContainerUpdate.as_view(), name='container_update' ),
    path('containers/<int:pk>/delete/', views.ContainerDelete.as_view(), name='container_delete' ),
    
# -------------------------------------------------------------- Transport --------------------------------------------------------------
    path('transports/',views.TransportList.as_view(), name='transport_list' ),
    path('transports/create/', views.TransportCreate.as_view(), name='transport_create'),
    path('transports/<int:pk>/', views.TransportDetails.as_view(), name='transport_detail'),
    path('transports/<int:pk>/update/', views.TransportUpdate.as_view(), name='transports_update'),
    path('transports/<int:pk>/delete/', views.TransportDelete.as_view(), name='transports_delete'),

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
    path('profile/edit/', views.edit_profile, name='edit_profile')
]