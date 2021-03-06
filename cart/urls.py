from django.urls import path
from . import views

urlpatterns = [
    path('',views.view_cart, name="view-cart"),
    path('add/<str:pk>/',views.add_to_cart, name="add-to-cart"),
    path('adjust/<str:pk>/',views.adjust_cart, name="adjust-cart"),
]