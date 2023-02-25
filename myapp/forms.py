from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name','last_name', 'email','mobile','address')
class EditUser(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name','last_name', 'email','mobile','address')