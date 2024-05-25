from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsView.as_view(), name='news'),
    path('details/<int:n_id>', views.NewsDetailView.as_view(), name='news-details')
  
]