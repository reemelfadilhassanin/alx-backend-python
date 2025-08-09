from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification, MessageHistory

class MessagingSignalTests(TestCase):
    def setUp(self):
        self.u1 = User.objects.create_user(username='u1', password='pass')
        self.u2 = User.objects.create_user(username='u2', password='pass')

    def test_notification_on_message_create(self):
        msg = Message.objects.create(sender=self.u1, receiver=self.u2, content='Hello')
        self.assertTrue(Notification.objects.filter(user=self.u2, message=msg).exists())

    def test_message_edit_logging(self):
        msg = Message.objects.create(sender=self.u1, receiver=self.u2, content='Old')
        msg.content = 'New'
        msg.save()
        hist = MessageHistory.objects.filter(message=msg).first()
        self.assertIsNotNone(hist)
        self.assertEqual(hist.old_content, 'Old')
        self.assertTrue(Message.objects.get(pk=msg.pk).edited)

    def test_cascade_on_user_delete(self):
        msg = Message.objects.create(sender=self.u1, receiver=self.u2, content='Hi')
        Notification.objects.create(user=self.u2, message=msg)
        self.u2.delete()
        self.assertFalse(Message.objects.filter(receiver=self.u2).exists())
        self.assertFalse(Notification.objects.filter(user=self.u2).exists())
