from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm 
from .models import Order, Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    mobile = forms.IntegerField()
    profile_pic = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'email', 'mobile', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email','mobile',  'shipping_address', 'city', 'district', 'zip', 'payment_method']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields =('first_name' ,'last_name', 'email', 'username' )

        def __str__(self):
            return f'{self.user.username} Profile'

class ProfileimageUpdate(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        
    

# class MyPasswordChangeForm(forms.Form):
#     def __init__(self, user, *args, **kwargs):
#         self.user = user
#         super().__init__(user, *args, **kwargs)
#         self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': "Old Password"})
#         self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': "New Password"})
#         self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': "New Password"})

#     def save(self, commit=True):, '
#         password = self.cleaned_data["new_password1"]
#         self.user.set_password(password)
#         if commit:
#             self.user.save()
#         return self.user