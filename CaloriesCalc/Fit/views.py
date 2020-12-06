from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import *
from .filter import *


@login_required(login_url='login')
def home(requet):
    breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()[:5]
    lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()[:5]
    dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()[:5]
    snack = Category.objects.filter(name='snack')[0].fooditem_set.all()[:5]
    customers = Customer.objects.all()
    context = {
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner,
        'snack': snack,
        'customers': customers
    }
    return render(requet, 'main.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def fooditem(requet):
    breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()
    b_count = breakfast.count()
    lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()
    l_count = lunch.count()
    dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()
    d_count = dinner.count()
    snack = Category.objects.filter(name='snack')[0].fooditem_set.all()
    s_count = snack.count()

    context = {
        'breakfast': breakfast,
        'b_count': b_count,
        'lunch': lunch,
        'l_count': l_count,
        'dinner': dinner,
        'd_count': d_count,
        'snack': snack,
        's_count': s_count,
    }
    return render(requet, 'fooditem.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createFoodItem(request):
    form = FoodItemForm()
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'createfooditem.html', context)


