from django.urls import path
from . import views

urlpatterns = [
    path('transport/type/', views.TransportTypeCreate.as_view(), name='transport_type_create'),
    path('transport/type/<int:pk>/update/', views.TransportTypeUpdate.as_view(), name='transport_type_update'),
    path('transport/type/<int:pk>/delete/', views.TransportTypeDelete.as_view(), name='transport_type_delete'),
]