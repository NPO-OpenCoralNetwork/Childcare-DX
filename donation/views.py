from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import GeneralDonationForm, MembershipDonationForm
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
def donation_overview(request):
    return render(request, 'donation/donation.html')

def general_donation(request):
    if request.method == 'POST':
        form = GeneralDonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.donation_type = 'general'
            donation.save()
            # Handle Stripe payment here
            return redirect('donation_success')
    else:
        form = GeneralDonationForm()

    return render(request, 'donation/general_donation.html', {'form': form})

def membership_donation(request):
    if request.method == 'POST':
        form = MembershipDonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.donation_type = 'member'
            donation.save()
            # Handle Stripe payment here
            return redirect('donation_success')
    else:
        form = MembershipDonationForm()

    return render(request, 'donation/membership_donation.html', {'form': form})
