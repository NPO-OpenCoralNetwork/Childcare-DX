from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp'),
    path('verify-registration-otp/', views.verify_registration_otp_view, name='verify_registration_otp'),
    path('resend-registration-otp/', views.resend_registration_otp_view, name='resend_registration_otp'),
    path('profile/<int:pk>/', views.profile_view, name='profile'),
]
