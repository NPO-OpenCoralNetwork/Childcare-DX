from .views import (InquiryListView, InquiryDetailView, 
                    InquiryCreateView,ResponseDetailView,SavedResponseListView, 
                    SavedInquiryListView, report_user)
from django.urls import path

urlpatterns = [
    path('', InquiryListView.as_view(), name='inquiry_list'),
    path('inquiry/<int:pk>/', InquiryDetailView.as_view(), name='inquiry_detail'),
    path('inquiry/new/', InquiryCreateView.as_view(), name='inquiry_create'),
    path('inquiry/<int:pk>/response/<int:profile_user_id>/', ResponseDetailView.as_view(),name='response_detail'),
    path('saved_responses/', SavedResponseListView.as_view(), name='saved_responses'),
    path('saved-inquiries/', SavedInquiryListView.as_view(), name='saved_inquiries'),
    path('report/', report_user, name='report_user'),
]