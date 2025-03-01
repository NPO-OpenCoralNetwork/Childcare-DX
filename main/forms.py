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
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        
        # メール本文にユーザー情報を含める
        email_body = f"""
    お問い合わせがありました。
    
    【お名前】
    {name}
    
    【メールアドレス】
    {email}
    
    【メッセージ】
    {message}
        """
        
        subject = "お問い合わせ"
        from_email = settings.DEFAULT_FROM_EMAIL  # サイトのデフォルトメールアドレスを使用
        recipient_list = [settings.EMAIL_HOST_USER]
        
        
        try:
            send_mail(
                subject=subject,
                message=email_body,
                from_email=from_email,
                recipient_list=recipient_list,
                
            )
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")