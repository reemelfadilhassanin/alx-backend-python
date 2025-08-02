from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification, MessageHistory

class SignalTests(TestCase):
    def setUp(self):
        self.u1 = User.objects.create_user(username='u1', password='pass')
        self.u2 = User.objects.create_user(username='u2', password='pass')

    def test_notification_on_message_create(self):
        msg = Message.objects.create(sender=self.u1, receiver=self.u2, content="Hello")
        notif = Notification.objects.filter(user=self.u2, message=msg).first()
        self.assertIsNotNone(notif)

    def test_message_edit_logs_history(self):
        msg = Message.objects.create(sender=self.u1, receiver=self.u2, content="First")
        msg.content = "Second"
        msg.save()
        history = MessageHistory.objects.filter(message=msg).first()
        self.assertEqual(history.old_content, "First")
        self.assertTrue(Message.objects.get(pk=msg.pk).edited)

    def test_user_delete_cleans_data(self):
        msg = Message.objects.create(sender=self.u1, receiver=self.u2, content="Hi")
        Notification.objects.create(user=self.u2, message=msg)
        self.u2.delete()
        self.assertFalse(Message.objects.filter(pk=msg.pk).exists())
        self.assertFalse(Notification.objects.filter(message=msg).exists())
