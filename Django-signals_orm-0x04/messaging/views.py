from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from messaging.models import Message
from django.db.models import Prefetch

@login_required
def delete_user(request):
    user = request.user
    user.delete()
    messages.success(request, "Your account has been deleted.")
    return redirect('account_deleted')

def get_all_replies(message):
    replies = []
    children = message.replies.all()
    for reply in children:
        replies.append(reply)
        replies += get_all_replies(reply)
    return replies

@login_required
def threaded_conversation_view(request, conversation_user_id):
    from django.contrib.auth.models import User
    other_user = get_object_or_404(User, id=conversation_user_id)
    messages_qs = Message.objects.filter(
        sender=request.user, receiver=other_user, parent_message__isnull=True
    ).select_related('sender', 'receiver').prefetch_related(
        Prefetch('replies', queryset=Message.objects.select_related('sender'))
    )
    threads = []
    for msg in messages_qs:
        threads.append({'message': msg, 'replies': get_all_replies(msg)})
    return render(request, 'threaded_conversation.html', {'threads': threads})

@login_required
def unread_messages_view(request):
    unread_messages = Message.unread.unread_for_user(request.user)
    return render(request, 'unread_messages.html', {'messages': unread_messages})
