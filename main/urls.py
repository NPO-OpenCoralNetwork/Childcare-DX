from . import views
from django.urls import path
urlpatterns = [
    path('', views.home_view, name='home'),  
    path('chats/', views.chat_list_view, name='chat_list'),
    path('announcement/<int:pk>/', views.announcement_detail_view, name='announcement_detail'),
    path('child-support/', views.child_support_list, name='child_support_list'),
    path('child-support/<int:pk>/', views.child_support_detail, name='child_support_detail'),
        path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('contact/result/', views.ContactResultView.as_view(), name='contact_result'),
]