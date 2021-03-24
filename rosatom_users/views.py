from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

from .decorators import unauthenticated_user
from .forms import LoginForm


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('rosatom_app:home')
        else:
            messages.info(request, 'Неверное имя пользователя ИЛИ пароль')

    form = LoginForm()
    context = {'form': form}

    return render(request, 'registration/login.html', context)