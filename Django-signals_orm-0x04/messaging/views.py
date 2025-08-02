from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from messaging.models import Message
from django.db.models import Prefetch

# Recursive helper to get all nested replies
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

    # Fetch top-level messages in the conversation
    messages = Message.objects.filter(
        sender=request.user, receiver=other_user, parent_message__isnull=True
    ).select_related('sender', 'receiver').prefetch_related(
        Prefetch('replies', queryset=Message.objects.select_related('sender'))
    )

    # Build thread trees
    threads = []
    for msg in messages:
        thread = {
            'message': msg,
            'replies': get_all_replies(msg)
        }
        threads.append(thread)

    return render(request, 'threaded_conversation.html', {'threads': threads})
