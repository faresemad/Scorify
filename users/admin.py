from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "email", "is_active", "is_superuser"]
    list_editable = ["is_active"]
    list_display_links = ["first_name", "email"]
