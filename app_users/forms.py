from django import forms
# from django.contrib.auth.models import User
# from .models import user_profile
from .models import User, user_profile
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

        labels = {
            'password1':'Password',
            'password2':'Confirm Password'
        }

class UserProfileInfoForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    user_types = [
        ('student','student'),
        ('parent','parent')
    ]

    user_type = forms.ChoiceField(required=True,choices=user_types)

    class Meta():
        model = user_profile
        fields = ('bio', 'profile_pic', 'user_type')