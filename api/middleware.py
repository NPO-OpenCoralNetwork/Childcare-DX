from django.conf import settings
from django.contrib.auth import get_user_model

# class DisableAuthForLocalMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if settings.DEBUG and request.META['REMOTE_ADDR'] in ('127.0.0.1', 'localhost'):
#             User = get_user_model()
#             request.user = User.objects.get(username='bacon')
#         return self.get_response(request)