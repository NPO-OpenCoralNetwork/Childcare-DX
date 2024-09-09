from . import views
from django.urls import path
urlpatterns = [
    path('', views.home_view, name='home'),  
    path('chats/', views.chat_list_view, name='chat_list'),
     path('announcement/<int:pk>/', views.announcement_detail_view, name='announcement_detail'),
]