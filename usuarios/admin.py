from django.contrib import admin
from django.contrib.auth import admin as admin_auth_django

from .models import Users
from .forms import UserChangeForm, UserCreationForm


@admin.register(Users)
class UserAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    