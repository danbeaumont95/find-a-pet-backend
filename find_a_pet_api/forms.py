from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'phone_number', 'email')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
