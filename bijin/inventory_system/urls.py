from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('newcard/', views.create_card, name='newcard'),
    path('addproduct/', views.add_product, name='addproduct'),
    path('shipment/', views.shipment, name='shipment'),
    path('cards/', views.cards, name='cards'),
    path('filter/', views.date_filter, name='date')
]