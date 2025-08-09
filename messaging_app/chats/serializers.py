from rest_framework import serializers
from .models import User, Conversation, Message

# ✅ User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'phone_number', 'role', 'created_at']

# ✅ Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.CharField(source='sender.username', read_only=True)
    sender_email = serializers.CharField(source='sender.email', read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'sender_username', 'sender_email', 'conversation', 'message_body', 'sent_at']

# ✅ Conversation Serializer with nested messages + SerializerMethodField
class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at', 'messages']

    def get_messages(self, obj):
        messages = obj.messages.all()
        return MessageSerializer(messages, many=True).data

    def validate(self, data):
        # مجرد مثال لاستخدام ValidationError
        if 'participants' in data and len(data['participants']) < 2:
            raise serializers.ValidationError("Conversation must include at least two participants.")
        return data
