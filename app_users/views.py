from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form =  UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('store-home')
    else:
        form =  UserRegisterForm()
    return render(request, "app_users/register.html", {'form': form})

def login(request):
    return render(request, "app_users/login.html")