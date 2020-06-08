# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth import authenticate, get_user_model, login, logout 
# from .forms import UserLogin, UserRegister
# from django.contrib.auth.decorators import login_required

# @login_required
# def home(request):
#     return render(request, 'accounts/home.html', {})

# def login_view(request):
#     next = request.GET.get('next')
#     form = UserLogin(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data('username')
#         password = form.cleaned_data('password') 
#         user = authenticate(username=username, user=password)
#         login(request, user)
#         if next:
#             return redirect(next)   
#         return redirect('/')
    
#     context = {
#         'form': form,
#     }

#     return render(request, 'accounts/login.html', context )

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLogin, UserRegister

@login_required
def home(request):
    return render(request, 'accounts/home.html', {})


def login_view(request):
    next = request.GET.get('next')
    form = UserLogin(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "accounts/login.html", context)

        
