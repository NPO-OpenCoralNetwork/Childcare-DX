from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile,OTP
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


ALLOWED_DOMAINS = [
    "yahoo.co.jp", "gmail.com", "ezweb.ne.jp", "au.com", "docomo.ne.jp", 
    "i.softbank.jp", "softbank.ne.jp", "excite.co.jp", "googlemail.com", 
    "hotmail.co.jp", "hotmail.com", "icloud.com", "live.jp", "me.com", 
    "mineo.jp", "nifty.com", "outlook.com", "outlook.jp", "yahoo.ne.jp", 
    "ybb.ne.jp", "ymobile.ne.jp"
]

class CustomAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, label="ログイン状態を保持する")

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = ('username', 'email', 'user_type', 'bio')
        labels = {
            'username': 'ユーザー名',
            'email': 'メールアドレス',
            'user_type': 'ユーザータイプ',
            'bio': '自己紹介',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # パスワードフィールドのhelp_textを空にする
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields.pop('usable_password', True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        domain = email.split('@')[-1]
        if domain not in ALLOWED_DOMAINS:
            raise ValidationError(f"このメールドメイン '{domain}' は登録できません。\n 使用できるメールドメインは{ALLOWED_DOMAINS}です。")
        return email

class OTPForm(forms.ModelForm):
    class Meta:
        model = OTP
        fields = ['otp'] 
        labels = {'otp':'パスワード'}

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio'] 
        labels = {'bio':'自己紹介'}
    profile_image = forms.ImageField(
        label='プロフィール画像',
        widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input', 'style': 'display:none;'}),
        required=False
    )