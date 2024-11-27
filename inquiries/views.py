from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Inquiry, Response,Tag, SavedResponse, SavedInquiry, Report
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import InquiryForm, ResponseForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import UserProfile
from django.core.mail import send_mail
from django.contrib import messages
from childhelper import settings

class InquiryListView(ListView):
    model = Inquiry
    template_name = 'inquiry_list.html'
    context_object_name = 'inquiries'
    paginate_by = 8  

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        query = self.request.GET.get('q')
        tag_ids = self.request.GET.getlist('tags')
    
        if query:
            queryset = queryset.filter( Q(title__icontains=query) | Q(content__icontains=query))
    
        if tag_ids:
            tag_ids = [tag_id for tag_id in tag_ids if tag_id]  # 空のIDを除去
            if tag_ids:
                for tag_id in tag_ids:
                    queryset = queryset.filter(tags__in=[tag_id])
    
        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['selected_tags'] = self.request.GET.getlist('tags')
        context['query'] = self.request.GET.get('q', '')
        return context


class InquiryDetailView(DetailView):
    model = Inquiry
    template_name = 'inquiries/inquiry_detail.html'
    context_object_name = 'inquiry'
    
    def get_object(self):
        inquiry = super().get_object()
        # 閲覧数を増加させる
        inquiry.views += 1
        inquiry.save()
        return inquiry
    
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        user = self.request.user
        context['is_owner'] = self.request.user == self.get_object().user
       
        if user.is_authenticated and user.user_type == 'responder':
            context['form'] = ResponseForm()
        else:
            context['form'] = None

        response_id = self.request.GET.get('response_id')
        
        if response_id:
            responses = Response.objects.filter(id=response_id, inquiry=self.get_object())
            
            context['responses'] = responses
        else:
            context['responses'] = Response.objects.filter(inquiry=self.get_object())
        return context
        

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # self.objectを設定
    
        if "delete_inquiry" in request.POST:
            if self.object.user == self.request.user:
                self.object.delete()
                return redirect('profile', pk=self.request.user.pk)
    
        if "delete_response" in request.POST:
            response_id = request.POST.get('delete_response_id')
            response = get_object_or_404(Response, id=response_id)
            if response.user == self.request.user:
                response.delete()
    
        if 'save_response' in request.POST:
            response_id = request.POST.get('response_id')
            response = get_object_or_404(Response, id=response_id)
            if request.user.user_type == 'inquirer':  # 相談者のみ保存可能
                # 同じユーザーが同じレスポンスを既に保存していないか確認
                if not SavedResponse.objects.filter(user=request.user, response=response).exists():
                    SavedResponse.objects.create(user=request.user, response=response)
        
        if 'save_inquiry' in request.POST:
            inquiry_id = request.POST.get('inquiry_id')
            inquiry = get_object_or_404(Inquiry, id=inquiry_id)
            if request.user.user_type == 'responder': 
                if not SavedInquiry.objects.filter(responder=request.user, inquiry=inquiry).exists():
                    SavedInquiry.objects.create(responder=request.user, inquiry=inquiry)
    
    
        if request.user.is_authenticated and request.user.user_type == 'responder':
            form = ResponseForm(request.POST)
            if form.is_valid():
                response = form.save(commit=False)
                response.inquiry = self.object
                response.user = request.user
                response.save()
                return redirect('inquiry_detail', pk=self.object.pk)
    
        context = self.get_context_data()
        context['form'] = ResponseForm()  # 必要に応じてリセット
        return self.render_to_response(context)

class InquiryCreateView(CreateView):
    model = Inquiry
    form_class = InquiryForm
    template_name = 'inquiries/inquiry_form.html'
    success_url = reverse_lazy('inquiry_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        tag_ids = self.request.POST.getlist('tags')
        if tag_ids and any(tag_ids): 
            tags = Tag.objects.filter(id__in=tag_ids)
            self.object.tags.set(tags)

        return response

    def form_invalid(self, form):
        print(form.errors)  # エラーメッセージをログに出力
        return super().form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.user_type == 'inquirer':
            return redirect('inquiry_list')  # 相談者以外はアクセス不可
        return super().dispatch(request, *args, **kwargs)


class ResponseDetailView(LoginRequiredMixin, DetailView):
    model = Inquiry
    template_name = 'inquiries/response_detail.html'
    context_object_name = 'inquiry'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_user_id = self.kwargs.get('profile_user_id')
        profile_user = get_object_or_404(UserProfile, id=profile_user_id)
        responses = Response.objects.filter(inquiry=self.get_object(), user=profile_user)
        if responses.exists():
            context['response'] = responses.first()  # 最初の一件を取得
        else:
            context['response'] = None
        context['profile_user'] = profile_user
        return context
    
    def post(self, request, *args, **kwargs):

        if "delete_response" in request.POST:
            response_id = request.POST.get('delete_response_id')
            response = get_object_or_404(Response, id=response_id)
            if response.user == self.request.user:
                response.delete()
            return redirect('profile', pk=self.request.user.pk)
        return self.get(request, *args, **kwargs)
    
class SavedResponseListView(LoginRequiredMixin, ListView):
    model = SavedResponse
    template_name = 'inquiries/saved_response.html'
    context_object_name = 'saved_responses'

    def get_queryset(self):
        return SavedResponse.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        response_id = request.POST.get('response_id')
        saved_response = get_object_or_404(SavedResponse, user=request.user, response_id=response_id)
        saved_response.delete()
        return redirect('saved_responses')
    

class SavedInquiryListView(LoginRequiredMixin, ListView):
    model = SavedInquiry
    template_name = 'inquiries/saved_inquiries.html'
    context_object_name = 'saved_inquiries'

    def get_queryset(self):
        return SavedInquiry.objects.filter(responder=self.request.user)
    
    def post(self, request, *args, **kwargs):
        inquiry_id = request.POST.get('inquiry_id')
        saved_inquiry = get_object_or_404(SavedInquiry, responder=request.user, inquiry_id=inquiry_id)
        saved_inquiry.delete()
        return redirect('saved_inquiries')
    
@login_required
def report_user(request):
    if request.method == "POST":
        reported_user_id = request.POST.get('reported_user_id')
        reason = request.POST.get('reason')

        if reported_user_id and reason:
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
            messages.success(request, '通報が正常に送信されました。')
        else:
            messages.error(request, '通報内容に不備があります。')
    return redirect('inquiry_detail',pk=request.user.id)