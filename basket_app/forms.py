from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from basket_app.models import Receiver

class CustomerForm(forms.ModelForm):
    password= forms.CharField(widget=PasswordInput)

    class Meta():
        model= User
        fields= ('username','password','email')

class OrderForm(forms.ModelForm):
    class Meta():
        model= Receiver
        fields= ('recname','phone','address')

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['recname'].required = True
        self.fields['phone'].required = True
        self.fields['address'].required = True