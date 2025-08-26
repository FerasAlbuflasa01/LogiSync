from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    
    path('containers/', views.ContainerList.as_view(), name='container_list'),
    path('containers/<str:pk>/', views.ContainerDetail.as_view(), name='container_detail' ),
    
    path('containers/create/', views.ContainerCreate.as_view(), name='container_create' ),
    path('containers/<str:pk>/update/', views.ContainerUpdate.as_view(), name='container_update' ),
    path('containers/<str:pk>/delete/', views.ContainerDelete.as_view(), name='container_delete' ),
    
]