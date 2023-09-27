from typing import Any
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Username'
    }))
    password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Confirm Password'
    }))


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Confirm Password'
    }))
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'image',
            'password',
        )
        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'First name'
            }),
            'last_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Last name'
            }),
            'username' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Username'
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Email'
            }),
            'password' : forms.PasswordInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Password'
            }),
        }

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Passwords must be same!')

    def save(self, commit: bool = ...) -> Any:
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()