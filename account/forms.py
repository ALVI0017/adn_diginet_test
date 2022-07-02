# form for user registration login
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
# from .models import UserProfile


class SignUpForm(UserCreationForm):

    username = forms.CharField(max_length=100, label="User Name", error_messages={'required': 'This field is required'}, widget=forms.TextInput(
        attrs={'placeholder': 'Write Your username', }))
    email = forms.EmailField(max_length=200, label='Email', widget=forms.EmailInput(
        attrs={'placeholder': 'Write Your email', }))
    first_name = forms.CharField(max_length=100, label="First name", widget=forms.TextInput(
        attrs={'placeholder': 'Write Your first name', }))
    last_name = forms.CharField(max_length=100, label="Last Name", widget=forms.TextInput(
        attrs={'placeholder': 'Write Your last name', }))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter New Password',
                                                    }),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Enter Repeat password',
                                                    }),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))

    class Meta:
        model = User
        fields = ['username', 'password']
