# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    pasword = forms.CharField()

    class Meta():
        model = User
        fields = ('username','email','password')


# class UserCreateForm(UserCreationForm):
#
#     class Meta():
#         fields = ('username','email','password1','password2')
#         model = get_user_model()
#
#         widgets = {
#             'username': forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Username'}),
#             'email': forms.EmailInput(attrs = {'class':'form-control', 'placeholder': 'Email address'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}),
#         }
#
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self.fields['username'].label = 'Display Name'
#         self.fields['email'].label = 'Email Address'
