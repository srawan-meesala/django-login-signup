from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class AccountUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_picture', 'address_line1', 'city', 'state', 'pincode', 'user_type')

    def clean(self):
        data = super().clean()
        password = data.get("password1")
        confirm_password = data.get("password2")

        if password != confirm_password:
            self.add_error('password2', "Passwords do not match")