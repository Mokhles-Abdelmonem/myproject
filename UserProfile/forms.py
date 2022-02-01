from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class Register(UserCreationForm):
    username = forms.CharField(label='الاسم :')
    first_name = forms.CharField(label='الاسم الاول :')
    last_name = forms.CharField(label='الاسم الاخير :')
    email = forms.EmailField(label='البريد الإلكترونى :')
    password1 = forms.CharField(label='كلمة المرور :', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(label='تأكيد كلمة المرور :', widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class Login(forms.ModelForm):
    username = forms.CharField(label='الاسم :')
    password = forms.CharField(label='كلمة المرور :', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')

class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(label='الاسم الاول :')
    last_name = forms.CharField(label='الاسم الاخير :')
    email = forms.EmailField(label='البريد الإلكترونى :')
    password = forms.CharField(label='كلمة المرور :', widget=forms.PasswordInput(), min_length=8)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
    
class SendingMail(forms.ModelForm):
    email = forms.EmailField(label='البريد الإلكترونى :')
    class Meta:
        model = User
        fields = ('email',)
    