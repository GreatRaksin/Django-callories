from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import *


class FoodItemForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = '__all__'


class AddUserFoodItem(ModelForm):
    class Meta:
        model = UserFoodItem
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
