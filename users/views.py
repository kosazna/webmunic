from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(response):
    if response.method == 'POST':
        form = UserRegisterForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(
                response, f"Your account has been created. You are able to login!")
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(response, 'users/register.html', {'form': form})


@login_required
def profile(response):
    if response.method == 'POST':
        u_form = UserUpdateForm(response.POST, instance=response.user)
        p_form = ProfileUpdateForm(response.POST,
                                   response.FILES,
                                   instance=response.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(response, "Your account has been updated!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=response.user)
        p_form = ProfileUpdateForm(instance=response.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(response, 'users/profile.html', context)
