from rest_framework.views import APIView
from rest_framework.response import Response

class MessageView(APIView):
    def get(self, request):
        return Response({"message": "Hello from Messaging API"})
