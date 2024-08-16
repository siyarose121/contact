from django import forms
from django.contrib.auth.models import User
from ContactApp.models import ContactModel


class RegisterForm(forms.ModelForm):
        class Meta:
            model=User
            fields=["first_name","last_name","username","email","password"]
            widgets={
                "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"firstName"}),
                "last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"LastName"}),
                "username":forms.TextInput(attrs={"class":"form-control","placeholder":"UserName"}),
                "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"}),
                "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}),
        }

class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}),

        }

class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactModel
        fields=["name","phone"]
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control","placeholder":"Name"}),
            "phone":forms.NumberInput(attrs={"class":"form-control","placeholder":"Phone Number"}),
        }