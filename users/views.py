from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(response):
    if response.method == 'POST':
        form = UserRegisterForm(response.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(response, f"Account created for {username}")
            return redirect('blog-home')
    else:
        form = UserRegisterForm()

    return render(response, 'users/register.html', {'form': form})
