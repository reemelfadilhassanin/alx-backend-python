from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_messages'
    )
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_messages'
    )
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    
    # Edit tracking
    edited = models.BooleanField(default=False)
    edited_by = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='edited_messages'
    )
    edit_timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.sender.username} to {self.recipient.username}: {self.content[:30]}"

class MessageEditHistory(models.Model):
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name='edit_history'
    )
    old_content = models.TextField()
    edited_by = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL
    )
    edit_timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Edit on {self.edit_timestamp} by {self.edited_by.username if self.edited_by else 'Unknown'}"
