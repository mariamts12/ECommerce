from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def update_activity(self, user_id: int):
        self.filter(id=user_id).update(last_active_datetime=timezone.now())
