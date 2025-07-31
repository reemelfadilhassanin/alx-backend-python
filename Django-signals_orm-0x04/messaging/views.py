from django.shortcuts import render
from .models import Message
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch

@login_required
def inbox(request):
    # Top-level messages only (not replies), with their replies prefetched
    messages = (
        Message.objects
        .filter(recipient=request.user, parent_message__isnull=True)
        .select_related('sender', 'recipient')
        .prefetch_related(
            Prefetch('replies', queryset=Message.objects.select_related('sender'))
        )
        .order_by('-timestamp')
    )

    return render(request, 'messaging/inbox.html', {
        'messages': messages
    })
