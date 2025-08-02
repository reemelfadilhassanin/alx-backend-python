from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Message, Notification, MessageHistory

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:
        try:
            previous = Message.objects.get(pk=instance.pk)
        except Message.DoesNotExist:
            return
        if previous.content != instance.content:
            MessageHistory.objects.create(message=instance, old_content=previous.content)
            instance.edited = True

@receiver(post_delete, sender=User)
def delete_related_data(sender, instance, **kwargs):
    # Deletes messages where user sent or received
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()
    # Deletes notifications
    Notification.objects.filter(user=instance).delete()
    # Deletes history entries for messages of deleted user
    MessageHistory.objects.filter(message__sender=instance).delete()
