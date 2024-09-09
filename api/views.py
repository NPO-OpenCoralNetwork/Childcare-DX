from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response as DRFResponse
from .serializers import UserProfileSerializer,UserSignUpSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.models import OTP
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import login, authenticate,logout
from accounts.models import UserProfile, OTP
from accounts.views import generate_otp, send_otp_via_email
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

class UserSignUpAPIView(APIView):

    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            otp_code = generate_otp()
            OTP.objects.create(user=user, otp=otp_code)
            send_otp_via_email(user, otp_code)
            request.session['otp_user_id'] = user.id

            # JWTトークンの生成
            refresh = RefreshToken.for_user(user)

            return DRFResponse({
                'message': 'OTP sent. Please verify OTP.',
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'next_url': reverse('verify_otp')  
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            try:
                user_profile = UserProfile.objects.get(username=user)
            except UserProfile.DoesNotExist:
                return Response({'error': 'UserProfile does not exist'}, status=status.HTTP_400_BAD_REQUEST)
           
            # JWTトークンの生成
            refresh = RefreshToken.for_user(user)
            
            send_otp_via_email(request, user_profile)
            request.session['otp_user_id'] = user.id
            
            return DRFResponse({
                'message': 'OTP sent. Please verify OTP.',
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'next_url': reverse('api_verify_otp')  
            }, status=status.HTTP_200_OK)
        
        return DRFResponse({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class VerifyOtpAPIView(APIView):

    permission_classes = [AllowAny]
    def post(self, request):
        otp_input = request.data.get('otp')
        username = request.data.get('username')
        user = get_object_or_404(UserProfile, username=username)
        otp_record = OTP.objects.filter(user=user).last()

        if otp_record and otp_record.otp == otp_input:
            login(request, user)
            otp_record.delete()  
            return DRFResponse({'message': 'Logged in successfully!'}, status=status.HTTP_200_OK)
        return DRFResponse({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # username = request.data.get('username')
        # user = get_object_or_404(UserProfile, username=username)
        # request.data.username = user
        logout(request)
        return DRFResponse({"detail": "ログアウトしました。"}, status=200)

class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


from inquiries.models import Inquiry, Response,SavedResponse
from .serializers import InquirySerializer, ResponseSerializer,SavedResponseSerializer
from rest_framework.permissions import IsAuthenticated

class InquiryCreateAPIView(generics.CreateAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ResponseCreateAPIView(generics.CreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        inquiry = Inquiry.objects.get(pk=self.kwargs['inquiry_id'])
        serializer.save(user=self.request.user, inquiry=inquiry)

class DeleteResponseAPIView(APIView):
    def delete(self, request, response_id):
        response = get_object_or_404(Response, id=response_id)
        if response.user == request.user:
            response.delete()
            return DRFResponse({"message": "Response deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        return DRFResponse({"error": "You are not authorized to delete this response."}, status=status.HTTP_403_FORBIDDEN)

class SaveResponseAPIView(APIView):
    def post(self, request, response_id):
        response = get_object_or_404(Response, id=response_id)
        if request.user.user_type == 'inquirer':  # 相談者のみ保存可能
            if not SavedResponse.objects.filter(user=request.user, response=response).exists():
                saved_response = SavedResponse.objects.create(user=request.user, response=response)
                serializer = SavedResponseSerializer(saved_response)
                return DRFResponse(serializer.data, status=status.HTTP_201_CREATED)
        return DRFResponse({"error": "You are not authorized to save this response."}, status=status.HTTP_403_FORBIDDEN)

class InquiryListAPIView(generics.ListAPIView):
    serializer_class = InquirySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Inquiry.objects.all()
        keyword = self.request.query_params.get('keyword', None)
        
        if keyword:
            queryset = Inquiry.objects.filter(title__icontains=keyword)
        return queryset

class SaveInquiryAPIView(generics.CreateAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            inquiry = serializer.save(user=request.user)
            return Response({"detail": "Inquiry saved successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 投稿削除用のAPIビュー
class DeleteInquiryAPIView(generics.DestroyAPIView):
    queryset = Inquiry.objects.all()
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        inquiry = self.get_object()
        if inquiry.user == request.user:
            inquiry.delete()
            return Response({"detail": "Inquiry deleted successfully."}, status=status.HTTP_200_OK)
        return Response({"detail": "You are not allowed to delete this inquiry."}, status=status.HTTP_403_FORBIDDEN)

# 返答保存API
class SaveResponseAPIView(generics.CreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        inquiry_id = request.data.get('inquiry_id')
        inquiry = Inquiry.objects.get(id=inquiry_id)
        if request.user.user_type == 'inquirer':
            response = Inquiry.objects.create(inquiry=inquiry, user=request.user, content=request.data['content'])
            Response.objects.create(user=request.user, response=response)
            return Response({"detail": "Response saved successfully."}, status=status.HTTP_201_CREATED)
        return Response({"detail": "Only inquirers can save responses."}, status=status.HTTP_403_FORBIDDEN)

# 保存した返答リスト表示用のAPI
class SavedResponseListAPIView(generics.ListAPIView):
    serializer_class = SavedResponseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Response.objects.filter(user=self.request.user)

from .serializers import SJigyoushaSerializer, JigyoushaSerializer
from jigyousha.models import SJigyousha,Jigyousha
from django.db.models import Q

class SJigyoushaListAPIView(generics.ListAPIView):
    serializer_class = SJigyoushaSerializer
    permission_classes = [IsAuthenticated]  # 認証が必要であれば追加
    
    def get_queryset(self):
        queryset = SJigyousha.objects.all()
        todofuken = self.request.query_params.get('todofuken', None)
        shichoson = self.request.query_params.get('shichoson', None)
        service_types = self.request.query_params.getlist('service_types', None)
        keyword = self.request.query_params.get('keyword', None)

        if todofuken:
            queryset = queryset.filter(Q(jigyousho_address_city__icontains=todofuken))

        if shichoson:
            queryset = queryset.filter(Q(jigyousho_address_city__icontains=shichoson))

        if service_types:
            service_filters = Q()
            service_mapping = {
        '訪問系サービス': [
            '居宅介護', '重度訪問介護', '同行援護', '行動援護', '重度障害者等包括支援'
        ],
        '日中活動系サービス': [
            '療養介護', '生活介護', '短期入所'
        ],
        '施設系サービス': [
            '施設入所支援'
        ],
        '居住系サービス': [
            '共同生活援助', '自立生活援助'
        ],
        '訓練系・就労系サービス': [
            '自立訓練(機能訓練)', '自立訓練(生活訓練)', '宿泊型自立訓練',
            '就労移行支援', '就労継続支援Ａ型', '就労継続支援Ｂ型', '就労定着支援'
        ],
        '障害児通所系サービス': [
            '児童発達支援', '医療型児童発達支援', '放課後等デイサービス',
            '居宅訪問型児童発達支援', '保育所等訪問支援'
        ],
        '障害児入所系サービス': [
            '福祉型障害児入所施設', '医療型障害児入所施設'
        ],
        '相談系サービス': [
            '地域相談支援(地域移行)', '地域相談支援(地域定着)', '計画相談支援', '障害児相談支援'
        ]
    }

            for service_type in service_types:
                mapped_services = service_mapping.get(service_type, [])
                service_filters |= Q(service_type__in=mapped_services)
            queryset = queryset.filter(service_filters)

        if keyword:
            queryset = queryset.filter(Q(service_type__icontains=keyword))

        return queryset


class JigyoushaListAPIView(generics.ListAPIView):
    serializer_class = JigyoushaSerializer
    permission_classes = [IsAuthenticated]  # 認証が必要であれば追加
    
    def get_queryset(self):
        queryset = Jigyousha.objects.all()
        todofuken = self.request.query_params.get('todofuken', None)
        shichoson = self.request.query_params.get('shichoson', None)
        service_types = self.request.query_params.getlist('service_types', None)
        keyword = self.request.query_params.get('keyword', None)

        if todofuken:
            queryset = queryset.filter(Q(jigyousho_address_city__icontains=todofuken))

        if shichoson:
            queryset = queryset.filter(Q(jigyousho_address_city__icontains=shichoson))

        if service_types:
            service_filters = Q()
            service_mapping = {
                '相談': ['居宅介護支援'],
                '訪問介護': [
                    '訪問介護', '訪問看護', '訪問リハビリテーション', '訪問入浴介護', '定期巡回・随時対応型訪問介護看護'
                ],
                '福祉用品利用': ['福祉用具貸与'],
                'デイサービス': [
                    '通所介護', '地域密着型通所介護', '認知症対応型通所介護'
                ],
                'ショートステイ': [
                    '短期入所生活介護', '看護小規模多機能型居宅介護', '小規模多機能型居宅介護',
                    '短期入所療養介護（介護老人保健施設）', '短期入所療養介護（介護医療院）', 
                    '短期入所療養介護', '療養通所介護'
                ],
                '施設入所': [
                    '認知症対応型共同生活介護',
                    '特定施設入居者生活介護（有料老人ホーム（サービス付き高齢者向け住宅））',
                    '特定施設入居者生活介護（有料老人ホーム（サービス付き高齢者向け住宅（外部サービス利用型））',
                    '地域密着型特定施設入居者生活介護（有料老人ホーム（サービス付き高齢者向け住宅））',
                    '特定施設入居者生活介護（軽費老人ホーム）',
                    '特定施設入居者生活介護（軽費老人ホーム（外部サービス利用型）',
                    '地域密着型特定施設入居者生活介護（軽費老人ホーム）',
                    '特定施設入居者生活介護（有料老人ホーム）',
                    '特定施設入居者生活介護（有料老人ホーム（外部サービス利用型））',
                    '地域密着型特定施設入居者生活介護（有料老人ホーム）',
                    '介護医療院', '介護療養型医療施設'
                ],
                '施設入所（費用減免制度あり）': [
                    '介護老人福祉施設', '介護老人保健施設'
                ]
            }

            for service_type in service_types:
                mapped_services = service_mapping.get(service_type, [])
                service_filters |= Q(service_type__in=mapped_services)
            queryset = queryset.filter(service_filters)

        if keyword:
            queryset = queryset.filter(Q(service_type__icontains=keyword))

        return queryset
    

from chat.models import Chat,Message
from .serializers import MessageSerializer
class ChatMessageCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        chat = get_object_or_404(Chat, id=data.get('chat_id'))
        message = Message.objects.create(chat=chat, sender=request.user, content=data.get('content'))
        return Response({'message': 'Message sent successfully', 'message_id': message.id})

class ChatHistoryAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        return Message.objects.filter(chat_id=chat_id)


from main.models import Announcement
from .serializers import InquirySerializer, AnnouncementSerializer

class InquiryHomeListAPIView(generics.ListAPIView):
    latest = Inquiry.objects.order_by('-created_at')[:5]
    popular = Inquiry.objects.order_by('views')[:5]
    serializer_class = InquirySerializer
    
    def get_queryset(self):
        return self.latest,self.popular
    
class AnnouncementListAPIView(generics.ListAPIView):
    queryset = Announcement.objects.order_by('-date')[:8]
    serializer_class = AnnouncementSerializer
    
    def get_queryset(self):
        return self.queryset
    

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
from accounts.models import UserProfile
from inquiries.models import Report
from .serializers import ReportSerializer

class ReportUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            reported_user_id = serializer.validated_data['reported_user_id']
            reason = serializer.validated_data['reason']

            reported_user = get_object_or_404(UserProfile, id=reported_user_id)
            report = Report.objects.create(reporter=request.user, reported_user=reported_user, reason=reason)
            
            # メール通知
            send_mail(
                '新しい通報がありました',
                f'通報者: {request.user.username}\n通報されたユーザー: {reported_user.username}\n理由: {reason}',
                'no-reply@yourdomain.com',
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            return Response({'message': '通報が正常に送信されました。'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# "access_token":eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1NDMyNDM2LCJpYXQiOjE3MjU0MjkwOTcsImp0aSI6IjQ0NWVmZGY0ZDQwMDQyMzhhZTUyOTM5NDJjY2YyMTY5IiwidXNlcl9pZCI6MX0.DCXXLzwE58dVF2a9nmFl8gh8P9-HKznG0fmWIBgOUWo
# "refresh_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTUxNTQ5NywiaWF0IjoxNzI1NDI5MDk3LCJqdGkiOiI1YTIxOTUxODY2ODU0OGZlOTZkYWU2MDQ4ZTVmNmEzMyIsInVzZXJfaWQiOjF9.ej56rrTqCwwLyoMgplJMBYs-ZzTqoHUH8xdi-lbEVzo"