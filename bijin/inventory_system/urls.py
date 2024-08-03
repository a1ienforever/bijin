from django.urls import path
from . import views

urlpatterns = [
    path('', views.BijinHome.as_view(), name=''),
    path('newcard/', views.CreateCard.as_view(), name='newcard'),
    path('addproduct/', views.AddProduct.as_view(), name='addproduct'),
    path('shipment/', views.shipment, name='shipment'),
    path('cards/', views.Cards.as_view(), name='cards'),
    path('filter/', views.date_filter, name='date'),
    path('menu/', views.menu, name='menu')

]

