from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import OTP
from accounts.views import generate_otp

User = get_user_model()

class UserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        fields = ['username', 'password']


class VerifyOtpSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=6)

    class Meta:
        fields = ['otp']

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'user_type']

class OtpSerializer(serializers.ModelSerializer):

    class meta:
        model = OTP
        fields = ['user','otp']

    def create(self, validated_data):
        user = User(
            password=validated_data['password'],
            username=validated_data['username']
        )
        otp_code = generate_otp()
        OTP.objects.create(user=user, otp=otp_code)
        return user
    
from inquiries.models import Inquiry, Response, SavedResponse

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ['id', 'title', 'content', 'user', 'created_at']

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ['id', 'inquiry', 'content', 'user', 'created_at']

class SavedResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedResponse
        fields = '__all__'

from jigyousha.models import disallowed, allowed

class disallowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = disallowed
        fields = '__all__'

class allowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = allowed
        fields = '__all__'

from chat.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

from main.models import Announcement

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

from inquiries.models import Report

class ReportSerializer(serializers.Serializer):
    class Meta:
        model = Report
        fields = '__all__'