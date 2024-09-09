from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Chat, Message
from .forms import MessageForm
from accounts.models import UserProfile

@login_required
def start_chat_view(request, pk):
    responder = get_object_or_404(UserProfile, pk=pk)
    user = request.user

    # 既存のチャットを探すか、新しいチャットを作成
    chat = Chat.objects.filter(participants=user).filter(participants=responder).first()
    if not chat:
        chat = Chat.objects.create()
        chat.participants.add(user, responder)

    return redirect('chat', chat_id=chat.id)


@login_required
def chat_view(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    if request.user not in chat.participants.all():
        return redirect('home')

    # 過去のメッセージを取得
    messages = Message.objects.filter(chat=chat).order_by('timestamp')

    return render(request, 'chat/chat.html', {
        'chat': chat,
        'messages': messages,
        'other_participant': chat.participants.exclude(id=request.user.id).first()
    })