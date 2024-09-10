from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from .forms import CustomUserCreationForm, OTPForm,CustomAuthenticationForm,UserProfileForm
from .models import UserProfile,OTP
from carehelper.settings import SESSION_COOKIE_AGE
from django.contrib.auth.decorators import login_required
from chat.models import Chat
from inquiries.models import Inquiry,Response
from django.contrib import messages
import pyotp



def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            otp = generate_otp()
            user.otp = otp
            send_otp_via_email(request,user)
            request.session['otp'] = otp  
            request.session['user_id'] = user.id  
            if not form.cleaned_data.get('remember_me'):
                request.session.set_expiry(0)
            else:
               
                request.session.set_expiry(SESSION_COOKIE_AGE)
            return redirect('verify_otp')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            otp = generate_otp()
            user.otp = otp  # 仮にユーザーモデルにOTPを保存しておく場合
            user.is_active = False  # OTP認証後にアクティブにする
            user.save()
            send_otp_via_email(request,user)
            request.session['user_id'] = user.id  # ユーザーIDをセッションに保存
            return redirect('verify_otp')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})



def logout_view(request):
    logout(request)
    # user_id = request.user.id
    # user = UserProfile.objects.get(id=user_id)
    # user.is_active = False
    request.session.flush()
    return redirect('home') 

def generate_otp():
    totp = pyotp.TOTP(pyotp.random_base32())
    return totp.now()


def send_otp_via_email(request,user):
    # 古いOTPを削除
    OTP.objects.filter(user=user).delete()

    otp_code = generate_otp()
    OTP.objects.create(user=user, otp=otp_code)
    
    # セッションにユーザーIDを保存
    request.session['otp_user_id'] = user.id
    print(request.session['otp_user_id'])
    subject = 'ワンタイムパスワード (OTP)'
    message = f'{user.username}様,\n\nログイン用のワンタイムパスワードは {otp_code} です。このパスワードは10分間有効です。\n\nよろしくお願いします。'
    from_email = 'no-reply@forcarer.org'
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)

def verify_otp_view(request):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            input_otp = form.cleaned_data.get('otp')
            user_id = request.session.get('otp_user_id')
            print(user_id)
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
                user.is_active = True  # ユーザーをアクティブに設定
                print(user)
                login(request, user)  # ユーザーをログインさせる
                messages.success(request, 'ログインに成功しました。')
                print(request.user, 'ログインに成功しました。')
                return redirect('home')  # ログイン後のリダイレクト先
            else:
                messages.error(request, 'OTPの有効期限が切れています。再度お試しください。')
                return redirect('verify_otp')
    else:
        form = OTPForm()

    return render(request, 'accounts/verify_otp.html', {'form': form})


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
                   if profile_image != None:
                      user_profile.profile_image = profile_image
                      
                   form.save()
                return redirect('profile', pk=user_profile.pk)

            # if 'save_profile' in request.POST:
            #     form = UserProfileForm(request.POST, instance=user_profile)
            #     if form.is_valid():
            #         form.save()
            #         return redirect('profile', pk=user_profile.pk)
            
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



