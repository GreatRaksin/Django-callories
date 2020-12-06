from django.http import HttpResponse
from django.shortcuts import redirect


def unauthorised_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function


def allowed_users(allowed_roles=[]):
    def decorator(view_function):
        def wrapper_function(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_function(request, *args, **kwargs)
            else:
                return HttpResponse('<h1>Ur not allowed to access this page</h1>')

        return wrapper_function

    return decorator


def admin_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'user':
            return redirect('userPage')
        if group == 'admin':
            return view_function(request, *args, **kwargs)

    return wrapper_function
