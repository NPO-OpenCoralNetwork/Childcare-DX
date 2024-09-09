from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth/signup/', views.UserSignUpAPIView.as_view(), name='api_signup'),
    path('auth/login/', views.UserLoginAPIView.as_view(), name='api_login'),
    path('auth/logout/', views.UserLogoutAPIView.as_view(), name='api_logout'),
    path('auth/verify-otp/', views.VerifyOtpAPIView.as_view(), name='api_verify_otp'),
    path('users/profile/', views.UserProfileAPIView.as_view(), name='api_profile'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('inquiries/', views.InquiryListAPIView.as_view(), name='api_inquiry_list'),
    path('inquiries/create/', views.InquiryCreateAPIView.as_view(), name='api_inquiry_create'),
    path('inquiries/<int:inquiry_id>/responses/', views.ResponseCreateAPIView.as_view(), name='api_response_create'),
    path('inquiries/save/', views.SaveInquiryAPIView.as_view(), name='api_save_inquiry'),
    path('inquiries/delete/<int:pk>/', views.DeleteInquiryAPIView.as_view(), name='api_delete_inquiry'),
    path('responses/save/', views.SaveResponseAPIView.as_view(), name='api_save_response'),
    path('response/<int:response_id>/delete/', views.DeleteResponseAPIView.as_view(), name='api_delete_response'),
    path('response/<int:response_id>/save/', views.SaveResponseAPIView.as_view(), name='api_save_response'),
    path('chat/send-message/', views.ChatMessageCreateAPIView.as_view(), name='api_send_message'),
    path('chat/history/{chat_id}/', views.ChatHistoryAPIView.as_view(), name='api_chat_history'),
    path('announcements/', views.AnnouncementListAPIView.as_view(), name='api_announcement_list'),
    path('home/', views.InquiryHomeListAPIView.as_view(), name='api_home_list'),
    path('report/', views.ReportUserAPIView.as_view(), name='api_report'),
]