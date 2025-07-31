from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Message, MessageHistory

User = get_user_model()

class MessageHistoryTest(TestCase):
    def test_edit_history_created(self):
        u = User.objects.create(username='test')
        msg = Message.objects.create(sender=u, recipient=u, content='hi')
        msg.content = 'hello'
        msg.save()
        self.assertTrue(MessageHistory.objects.filter(message=msg).exists())
        mh = MessageHistory.objects.get(message=msg)
        self.assertEqual(mh.old_content, 'hi')
