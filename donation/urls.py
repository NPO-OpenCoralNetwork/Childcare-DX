from django.urls import path
from . import views

urlpatterns = [
    path('donation/', views.donation_overview, name='donation_overview'),
    path('general/', views.general_donation, name='general_donation'),
    path('membership/', views.membership_donation, name='membership_donation'),
]
