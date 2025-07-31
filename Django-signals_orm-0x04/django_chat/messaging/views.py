from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Prefetch
from django.views.decorators.cache import cache_page
from .models import Message

@login_required
@cache_page(60)
def inbox(request):
    threads = (
        Message.objects.filter(recipient=request.user, parent_message__isnull=True)
        .select_related('sender', 'recipient')
        .prefetch_related(Prefetch('replies', queryset=Message.objects.select_related('sender')))
        .order_by('-timestamp')
    )

    def build_thread(msg):
        return {
            'msg': msg,
            'replies': [build_thread(r) for r in msg.replies.all()]
        }

    return render(request, 'messaging/inbox.html', {
        'threads': [build_thread(msg) for msg in threads]
    })

@login_required
def delete_user(request):
    user = request.user
    logout(request)
    user.delete()
    return redirect('home')
