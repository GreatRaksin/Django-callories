from django_filters import FilterSet

from .models import *


class fooditemFilter(FilterSet):
    class Meta:
        model = FoodItem
        fields = ['name']
