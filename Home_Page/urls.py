from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('industries/', views.IndustriesView.as_view(), name='industries'),
    path('products/<int:pk>/', views.brand_detail, name='brand_detail'), 

  
]