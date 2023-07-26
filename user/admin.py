from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_name',
        'user_email',
        'user_pw',
        'user_register_dttm'
    )