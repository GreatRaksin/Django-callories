from django.shortcuts import redirect


def unauthorised_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user_is_authenticated:
            return redirect('home')
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function()
