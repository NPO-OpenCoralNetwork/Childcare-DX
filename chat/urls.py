from django.urls import path
from .views import chat_view, start_chat_view

urlpatterns = [
    path('chat/<int:chat_id>/', chat_view, name='chat'),
    path('start-chat/<int:pk>/', start_chat_view, name='start_chat')
]