from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Message, MessageHistory
from messaging.models import Message, MessageHistory
from django.conf import settings

User = get_user_model()

@receiver(post_save, sender=Message)
def notify_receiver(sender, instance, created, **kwargs):
    if created:
        # أنشئ Notification هنا (إذا أردت)
        pass

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.id:
        old = Message.objects.get(pk=instance.id)
        if old.content != instance.content:
            instance.edited = True
            instance.edited_by = instance.sender  # أو من يقوم بالتعديل
            instance.edited_at = timezone.now()
            MessageHistory.objects.create(
                message=instance, old_content=old.content,
                edited_by=instance.edited_by, edited_at=instance.edited_at
            )

@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(recipient=instance).delete()
    MessageHistory.objects.filter(message__sender=instance).delete()
