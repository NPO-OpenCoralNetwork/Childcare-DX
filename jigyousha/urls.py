from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_allowed, name='search_allowed'),
    path('search_s/', views.search_disallowed, name='search_disallowed'),
    path('get-shichoson/', views.get_shichoson, name='get_shichoson'),
    path('allowed_detail/<int:pk>/', views.allowed_detail, name='allowed_detail'),
    path('disallowed_detail/<int:pk>/', views.disallowed_detail, name='disallowed_detail'),
]