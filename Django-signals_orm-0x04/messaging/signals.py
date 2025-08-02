from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory
from django.contrib.auth.models import User

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)

@receiver(pre_save, sender=Message)
def save_message_history(sender, instance, **kwargs):
    if instance.pk:
        old = Message.objects.get(pk=instance.pk)
        if old.content != instance.content:
            MessageHistory.objects.create(message=old, old_content=old.content)

@receiver(post_delete, sender=User)
def delete_user_data(sender, instance, **kwargs):
    from .models import Message, Notification, MessageHistory
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()
    Notification.objects.filter(user=instance).delete()
    MessageHistory.objects.filter(message__sender=instance).delete()

@receiver(pre_save, sender=Message)
def save_message_history(sender, instance, **kwargs):
    if instance.pk:
        old = Message.objects.get(pk=instance.pk)
        if old.content != instance.content:
            # edited_by can’t be accessed directly here; set it manually in the view
            MessageHistory.objects.create(
                message=old,
                old_content=old.content,
                edited_by=instance.sender  # this assumes sender is editing
            )
