from django.utils.deprecation import MiddlewareMixin

from .models import CustomUser


class UserActivityMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            CustomUser.objects.update_activity(user_id=request.user.id)
