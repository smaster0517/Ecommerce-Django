from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UpdateProfileForm
from django.contrib import messages
from app_store.models import Wishlist
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form =  UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form =  UserRegisterForm()
    return render(request, "app_users/register.html", {'form': form})

@login_required
def profile(request):
    wishlist = Wishlist.objects.get(user=request.user)
    products_in_wishlist = wishlist.wishlistproduct_set.order_by('-date_added')[:10]

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            user = request.user
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
    else:
        user = request.user
        form = UpdateProfileForm(instance=user)

    context = {
        'products_in_wishlist': products_in_wishlist,
        'form': form
    }
    return render(request, "app_users/profile.html", context=context)