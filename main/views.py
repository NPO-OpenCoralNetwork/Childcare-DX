from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from chat.models import Chat
from inquiries.models import Inquiry
from accounts.models import UserProfile
from .models import Announcement
from django.core.paginator import Paginator
from django.db.models import Q

def home_view(request):

    new_inquiries = Inquiry.objects.all().order_by('-created_at')
    paginator_new = Paginator(new_inquiries, 5)
    page_number_new = request.GET.get('page_new')
    new_inquiries_page = paginator_new.get_page(page_number_new)
    
    # 閲覧数の多い相談
    popular_inquiries = Inquiry.objects.all().order_by('-views')
    paginator_popular = Paginator(popular_inquiries, 5)
    page_number_popular = request.GET.get('page_popular')
    popular_inquiries_page = paginator_popular.get_page(page_number_popular)

    # お知らせ
    announcements = Announcement.objects.all().order_by('-date')
    paginator_announcements = Paginator(announcements, 8)
    page_number_announcement = request.GET.get('page_announcement')
    announcements_page = paginator_announcements.get_page(page_number_announcement)

    context = {
        'new_inquiries': new_inquiries_page,
        'popular_inquiries': popular_inquiries_page,
        'announcements': announcements_page,
    }
    return render(request, 'main/home.html', context)

@login_required
def chat_list_view(request):
    chats = Chat.objects.filter(participants=request.user)
    
    # チャットと相手のユーザー名をセットでリスト化
    chat_data = []
    if request.user.user_type == 'inquirer':
        query = request.GET.get('q')
        if query:
            responders = UserProfile.objects.filter(
                Q(username__icontains=query) | Q(bio__icontains=query),
                user_type='responder'
            )
        else:
            responders = UserProfile.objects.filter(user_type='responder')
    else:
        responders = None
    for chat in chats:
        other_participant = chat.participants.exclude(id=request.user.id).first()
        chat_data.append({
            'chat': chat,
            'other_participant_username': other_participant.username if other_participant else 'Unknown'
        })
    
    return render(request, 'main/chat_list.html', {'chat_data': chat_data,'responders': responders})

def announcement_detail_view(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    return render(request, 'main/announcement_detail.html', {'announcement': announcement})