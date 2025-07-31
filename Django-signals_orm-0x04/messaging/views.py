from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from .models import Message

def delete_user(request):
    if request.user.is_authenticated:
        user = request.user
        logout(request)
        user.delete()
    return redirect('home')

@method_decorator(cache_page(60), name='dispatch')
class ConversationListView(ListView):
    model = Message
    template_name = 'messaging/conversation_list.html'

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user)
