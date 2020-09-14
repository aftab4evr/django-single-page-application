from django import forms
from django.contrib import admin

from .models import UserManagement


class AddUserForm(forms.ModelForm):

    class Meta:
        model = UserManagement
        fields = "__all__"
