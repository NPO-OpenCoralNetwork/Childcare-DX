from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_jigyousha, name='search_jigyousha'),
    path('search_s/', views.search_sjigyousha, name='search_sjigyousha'),
    path('get-shichoson/', views.get_shichoson, name='get_shichoson'),
]