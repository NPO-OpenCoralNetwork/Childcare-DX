from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
class ContactForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _("お名前"),
        }),
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': _("メールアドレス"),
        }),
    )
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': _("メッセージ"),
        }),
    )
    def send_email(self):
        """フォームの内容をメールで送信"""
        subject = f"問い合わせ: {self.cleaned_data['name']}様より"
        message = f"""
       問い合わせがありました。
       
       送信者: {self.cleaned_data['name']}
       メールアドレス: {self.cleaned_data['email']}
       
       メッセージ:
       {self.cleaned_data['message']}
        """
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')