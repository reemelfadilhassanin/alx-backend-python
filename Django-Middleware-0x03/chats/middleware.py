import logging
from datetime import datetime

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('requests.log')
formatter = logging.Formatter('%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logger.info(log_message)

        response = self.get_response(request)
        return response
from django.http import HttpResponseForbidden
from datetime import datetime

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour
        # Allow only between 6AM (06) and 9PM (21)
        if not (6 <= current_hour < 21):
            return HttpResponseForbidden("Access to chat is restricted during these hours.")
        return self.get_response(request)
from django.http import HttpResponseForbidden

class RolePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/chats/'):
            user = request.user
            if not user.is_authenticated or not user.is_staff:
                return HttpResponseForbidden("You do not have permission to perform this action.")
        return self.get_response(request)
from django.http import JsonResponse
import time

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_tracker = {}  # {ip: [timestamps]}

    def __call__(self, request):
        if request.method == "POST" and request.path.startswith("/chats/"):
            ip = self.get_client_ip(request)
            now = time.time()
            timestamps = self.requests_tracker.get(ip, [])
            # Keep only timestamps in the last 60 seconds
            timestamps = [t for t in timestamps if now - t < 60]
            if len(timestamps) >= 5:
                return JsonResponse({"error": "Too many messages. Try again later."}, status=429)
            timestamps.append(now)
            self.requests_tracker[ip] = timestamps

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
