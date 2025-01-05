from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationFormCustom, UserChangeFormCustom
from .models import CustomUser, Profile

# Register your models here.

class UserAdminCustom(UserAdmin):
    add_form = UserCreationFormCustom
    form = UserChangeFormCustom
    model = CustomUser
    list_display = ['username', 'email', 'is_staff']


admin.site.register(CustomUser, UserAdminCustom)
admin.site.register(Profile)