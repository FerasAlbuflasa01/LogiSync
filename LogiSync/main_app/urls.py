from django.urls import path, include
from . import views

urlpatterns = [
    path('transports/',views.TransportList.as_view(), name='index' ),
    path('transports/show/<int:cat_id>/', views.TransportDetails.as_view, name='detail'),
    path('transports/create/', views.TransportCreate.as_view(), name='cat_create'),
    path('transports/<int:pk>/update/', views.TransportUpdate.as_view(), name='cats_update'),
    path('transports/<int:pk>/delete/', views.TransportDelete.as_view(), name='cats_delete'),
]