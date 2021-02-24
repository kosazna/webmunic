from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(response):
    if response.method == 'POST':
        form = UserRegisterForm(response.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                response, f"Your account has been created. You are able to login!")
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(response, 'users/register.html', {'form': form})


@login_required
def profile(response):
    return render(response, 'users/profile.html')
