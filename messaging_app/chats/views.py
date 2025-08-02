from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from messaging.models import Message

@login_required
@cache_page(60)
def conversation_view(request):
    threads = Message.objects.filter(receiver=request.user, parent_message__isnull=True)\
        .select_related('sender', 'receiver')\
        .prefetch_related('replies__sender')  # fetch replies for threading

    return render(request, 'chat/conversation_list.html', {
        'threads': threads,
    })

@login_required
def delete_user(request):
    request.user.delete()
    return redirect('home')
