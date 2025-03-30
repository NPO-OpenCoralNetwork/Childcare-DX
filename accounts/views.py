from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, get_user_model
from django.core.mail import send_mail
from .forms import CustomUserCreationForm, OTPForm, CustomAuthenticationForm, UserProfileForm
from .models import UserProfile, OTP
from childhelper.settings import SESSION_COOKIE_AGE
from django.contrib.auth.decorators import login_required
from chat.models import Chat
from inquiries.models import Inquiry, Response
from django.contrib import messages
import pyotp

User = get_user_model()

def generate_otp():
    totp = pyotp.TOTP(pyotp.random_base32())
    return totp.now()

def send_otp_via_email(request, user):
    # 既存のログイン用OTP送信処理（ユーザーがDBに存在している場合）
    OTP.objects.filter(user=user).delete()
    otp_code = generate_otp()
    OTP.objects.create(user=user, otp=otp_code)
    request.session['otp_user_id'] = user.id
    subject = 'ワンタイムパスワード (OTP)'
    message = f'{user.username}様,\n\nログイン用のワンタイムパスワードは {otp_code} です。このパスワードは10分間有効です。\n\nよろしくお願いします。'
    from_email = 'no-reply@forcarer.org'
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)

def send_registration_otp_email(request, email, otp, username):
    # ユーザー登録用のOTPメール送信用（ユーザー未登録時）
    subject = '新規登録用ワンタイムパスワード (OTP)'
    message = f'{username}様,\n\n新規登録用のワンタイムパスワードは {otp} です。このパスワードは10分間有効です。\n\nよろしくお願いします。'
    from_email = 'no-reply@forcarer.org'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # 登録データはセッションに一時保存（※セキュリティ上、適切な対策を検討してください）
            registration_data = form.cleaned_data
            otp = generate_otp()
            request.session['registration_data'] = registration_data
            request.session['registration_otp'] = otp
            # 登録用OTPメールを送信
            send_registration_otp_email(request, registration_data.get('email'), otp, registration_data.get('username'))
            return redirect('verify_registration_otp')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def verify_registration_otp_view(request):
    """
    ユーザー登録時のOTP検証用ビュー  
    セッションに保存していたOTPとユーザー入力を照合し、一致すればユーザーを作成・認証します。
    """
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            input_otp = form.cleaned_data.get('otp')
            session_otp = request.session.get('registration_otp')
            if input_otp == session_otp:
                registration_data = request.session.get('registration_data')
                if registration_data:
                    # ユーザー作成（CustomUserCreationFormのフィールド名に合わせて調整してください）
                    user = User.objects.create_user(
                        username=registration_data.get('username'),
                        email=registration_data.get('email'),
                        password=registration_data.get('password1')
                    )
                    user.is_active = True
                    user.save()
                    # セッションの一時情報を削除
                    del request.session['registration_data']
                    del request.session['registration_otp']
                    login(request, user)
                    messages.success(request, '登録と認証が完了しました。')
                    return redirect('home')
                else:
                    messages.error(request, '登録データが見つかりません。再度最初からお試しください。')
                    return redirect('register')
            else:
                messages.error(request, 'OTPが正しくありません。再度お試しください。')
                return redirect('verify_registration_otp')
    else:
        form = OTPForm()
    # テンプレート側で再送信リンクを表示するために is_registration=True を渡す
    return render(request, 'accounts/verify_otp.html', {'form': form, 'is_registration': True})

def resend_registration_otp_view(request):
    """
    登録用OTPの再送信ビュー  
    セッションの登録情報から新たなOTPを生成し、メールを再送します。
    """
    registration_data = request.session.get('registration_data')
    if registration_data:
        otp = generate_otp()
        request.session['registration_otp'] = otp
        send_registration_otp_email(request, registration_data.get('email'), otp, registration_data.get('username'))
        messages.success(request, 'OTPを再送信しました。メールをご確認ください。')
        return redirect('verify_registration_otp')
    else:
        messages.error(request, '再送信可能な登録情報がありません。最初からやり直してください。')
        return redirect('register')

# 以下は既存のログイン用ビュー等（変更がない部分）です。

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            otp = generate_otp()
            user.otp = otp
            send_otp_via_email(request, user)
            request.session['otp_user_id'] = user.id
            if not form.cleaned_data.get('remember_me'):
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(SESSION_COOKIE_AGE)
            return redirect('verify_otp')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def verify_otp_view(request):
    """
    ログイン用OTP検証ビュー（既存の実装）
    """
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            input_otp = form.cleaned_data.get('otp')
            user_id = request.session.get('otp_user_id')
            if not user_id:
                messages.error(request, 'セッションが無効です。もう一度最初からやり直してください。')
                return redirect('login')
            user = UserProfile.objects.get(id=user_id)
            try:
                otp_entry = OTP.objects.filter(user=user, otp=input_otp).latest('created_at')
            except OTP.DoesNotExist:
                messages.error(request, '無効なOTPです。再度お試しください。')
                return redirect('verify_otp')
            if otp_entry.is_valid():
                otp_entry.delete()
                user.is_active = True
                user.save()
                login(request, user)
                messages.success(request, 'ログインに成功しました。')
                return redirect('home')
            else:
                messages.error(request, 'OTPの有効期限が切れています。再度お試しください。')
                return redirect('verify_otp')
    else:
        form = OTPForm()
    return render(request, 'accounts/verify_otp.html', {'form': form})

def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('home')

@login_required
def profile_view(request, pk):
    user_profile = get_object_or_404(UserProfile, pk=pk)
    is_owner = request.user == user_profile 
    inquiry_his = Inquiry.objects.filter(user=user_profile)
    responses = Response.objects.filter(user=user_profile)
    
    if request.method == 'POST':
        if not is_owner:
            chat, created = Chat.objects.get_or_create(participants__in=[request.user, user_profile], defaults={'participants': [request.user, user_profile]})
            return redirect('chat', chat_id=chat.id)
        if is_owner:
            if 'save_profile' in request.POST:
                form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
                if form.is_valid():
                    profile_image = form.cleaned_data.get('profile_image')
                    if profile_image is not None:
                        user_profile.profile_image = profile_image
                    form.save()
                return redirect('profile', pk=user_profile.pk)
            elif 'delete_account' in request.POST:
                user_profile.delete()
                logout(request)
                return redirect('home')
            elif 'delete_inquiry' in request.POST:
                inquiry_id = request.POST.get('delete_inquiry_id')
                inquiry = get_object_or_404(Inquiry, id=inquiry_id, user=request.user)
                inquiry.delete()
                return redirect('profile', pk=request.user.pk)
            elif 'change_user_type' in request.POST:
                new_user_type = request.POST.get('user_type')
                if new_user_type in ['responder', 'inquirer']:
                    user_profile.user_type = new_user_type
                    user_profile.save()
                    return redirect('profile', pk=user_profile.pk)
            else:
                form = UserProfileForm(instance=user_profile)
    else:
        form = UserProfileForm(instance=user_profile) if is_owner else None
    
    return render(request, 'accounts/profile.html', {
        'form': form,
        'user_profile': user_profile,
        'is_owner': is_owner,
        'inquiries': inquiry_his,
        'responses': responses
    })
