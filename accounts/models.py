from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import datetime


class UserProfile(AbstractUser):
    USER_TYPE_CHOICES = (
        ('inquirer', '相談者'),
        ('responder', '回答者'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    inquiry_history = models.TextField(blank=True, null=True) 
    response_history = models.TextField(blank=True, null=True)
    chat_history = models.TextField(blank=True, null=True) 
    profile_image = models.ImageField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        # 以前のインスタンスを取得して、ユーザータイプが変更されたか確認
        if self.pk:
            previous = UserProfile.objects.get(pk=self.pk)
            print(self.profile_image)
            # ユーザータイプが変更され、かつオリジナルの画像が設定されていない場合のみデフォルト画像を更新
            if previous.user_type != self.user_type and (not self.profile_image or 'sheep' in str(self.profile_image) or 'kap' in str(self.profile_image)):
                if self.user_type == 'inquirer':
                    self.profile_image = 'icon_sheep_g1dsw0.png'
                elif self.user_type == 'responder':
                    self.profile_image = 'v1725934048/icon_kap_aptfdl.png'
        
        super().save(*args, **kwargs)
    

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='userprofile_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='userprofile_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )


    def __str__(self):
        return self.username

class OTP(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        # OTPの有効期間を10分間に設定
        return timezone.now() < self.created_at + datetime.timedelta(minutes=10)

    def __str__(self):
        return f"OTP for {self.user.username}"

