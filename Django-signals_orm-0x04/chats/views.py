from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from messaging.models import Message

@login_required
@cache_page(60)
def conversation_view(request):
    threads = Message.objects.filter(receiver=request.user, parent_message__isnull=True) \
        .select_related('sender') \
        .prefetch_related('replies__sender')
    return render(request, 'conversation_list.html', {'threads': threads})
