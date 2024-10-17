from django import forms
from .models import Donation
class GeneralDonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount', 'is_anonymous', 'name', 'address', 'phone_number']
        labels = {
            'amount': '金額',
            'is_anonymous': '匿名希望',
            'name': '名前',
            'address': '住所',
            'phone_number': '電話番号',
            'reason': '',
        }
    
    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount < 100:
            raise forms.ValidationError("金額は100円以上でなければなりません。")
        return amount

class MembershipDonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount', 'payment_frequency', 'is_anonymous', 'name', 'address', 'phone_number']
        labels = {
            'amount': '金額',
            'payment_frequency': '',
            'is_anonymous': '匿名希望',
            'name': '名前',
            'address': '住所',
            'phone_number': '電話番号',
            'reason': ''
        }
