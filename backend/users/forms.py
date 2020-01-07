from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    fullname = forms.CharField(label = "Full name")

    class Meta:
        model= User
        fields=['username','fullname','email','password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.fullname = self.cleaned_data["fullname"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user