from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField
from django.forms import EmailField


class CustomUserCreationForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        field_classes = {"username": UsernameField}
