from django import forms
from .models import JournalEntry, MembershipEntry
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

class JournalEntryForm(forms.ModelForm):
    """Form definition for JournalEntry."""

    class Meta:
        """Meta definition for JournalEntryform."""

        model = JournalEntry
        fields = ('name','renewal_date', 'sub_cost')

class MembershipEntryForm(forms.ModelForm):
    """Form definition for MembershipEntry."""

    class Meta:
        """Meta definition for MembershipEntryform."""

        model = MembershipEntry
        fields = ('name', 'renewal_date', 'sub_cost')

class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input100', 
            'placeholder': 'Username',
       }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={ 
            'class': 'input100',
            'placeholder': 'Password',
        }
    ))

class UserSignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input100',
            'placeholder': 'Username',
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input100',
            'placeholder': 'Password',
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input100',
            'placeholder': 'Confirm Password',
        }
    ))

