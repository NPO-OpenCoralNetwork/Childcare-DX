from django import forms
from .models import Donation

class GeneralDonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount', 'is_anonymous', 'name', 'address', 'phone_number', 'reason']
    
    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount < 100:
            raise forms.ValidationError("Amount must be at least 100 yen.")
        return amount

class MembershipDonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount', 'payment_frequency', 'is_anonymous', 'name', 'address', 'phone_number', 'reason']
