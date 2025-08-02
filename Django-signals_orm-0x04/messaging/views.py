# messaging/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

@login_required
def delete_user(request):
    """Deletes the currently logged-in user account"""
    user = request.user
    user.delete()
    messages.success(request, "Your account has been deleted.")
    return redirect('account_deleted')  # This URL name should exist or be created
