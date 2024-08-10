from django import forms
from .models import Category, Product,un

#register
from django.contrib.auth.forms import UserCreationForm
import django.contrib.auth
User=django.contrib.auth.get_user_model()
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'