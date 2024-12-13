from django import forms
from .models import *

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['user_name', 'email', 'password']

    def clean_user_name(self):
        user_name = self.cleaned_data['user_name']
        if User.objects.filter(user_name=user_name).exists():
            raise forms.ValidationError("This username is already taken.")
        return user_name

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'email', 'password', 'role']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'cost', 'category', 'image'] 

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'date_order', 'status', 'address_order', 'finish_cost', 'payment']


class SupportMessageForm(forms.ModelForm):
    class Meta:
        model = SupportMessage
        fields = ['subject', 'message']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}),
        }



class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = '__all__'

class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class ProductsOnWarehouseForm(forms.ModelForm):
    class Meta:
        model = ProductsOnWarehouse
        fields = '__all__'

class SupportMessageForm(forms.ModelForm):
    class Meta:
        model = SupportMessage
        fields = '__all__'

class WhatInOrderForm(forms.ModelForm):
    class Meta:
        model = WhatInOrder
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if not (1 <= rating <= 5):
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating