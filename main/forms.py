from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import userpost


class signupForm(UserCreationForm):

    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }))

    password2 = forms.CharField(
        label='Password (Again)', widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'email': "Email"
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control'
            }),
            'first_name': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'required': True,
                'class': 'form-control'
            })
        }


class signinForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'class': 'form-control'
    }))
    password = forms.CharField(
        label='Password', strip=False, widget=forms.PasswordInput(attrs={
            'autofocus': True,
            'class': 'form-control'
        }))


class postForm(forms.ModelForm):
    class Meta:
        model = userpost
        exclude = ['username']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }


class updateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'email': 'Email'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'required': True,
                'class': 'form-control'
            })
        }

    def __init__(self, *args, **kwargs):
        super(updateUserForm, self).__init__(*args, **kwargs)
        self.fields.pop('password', None)
        # self.fields['username'].required = False


class updatePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old password', strip=False, widget=forms.PasswordInput(attrs={
            'autofocus': True,
            'class': 'form-control'
        }))
    new_password1 = forms.CharField(
        label='New password', strip=False, widget=forms.PasswordInput(attrs={
            'autofocus': True,
            'class': 'form-control'
        }))
    new_password2 = forms.CharField(
        label='Confirm New password', strip=False, widget=forms.PasswordInput(attrs={
            'autofocus': True,
            'class': 'form-control'
        }))
