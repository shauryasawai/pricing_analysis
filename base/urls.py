# restaurant/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('update-prices/', views.update_prices, name='update_prices'),
    path('compare_prices/', views.compare_prices, name='compare_prices'),

  
]
