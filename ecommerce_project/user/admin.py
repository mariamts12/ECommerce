from django.contrib import admin

from .models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "last_active_datetime")
    list_filter = ("is_staff", "is_active")
    search_fields = ("username", "email", "first_name", "last_name")
