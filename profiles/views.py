from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.views import PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        messages.success(request, 'You are not logged in... Please login..')
        return redirect('profiles:login_user')


def signup_user(request):
    if request.user.is_authenticated:
        return redirect('profiles:dashboard')

    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(
                    request, 'You have been successfully registered...')
                return redirect('profiles:dashboard')

        else:
            form = SignUpForm()

        context = {'form': form}
        return render(request, 'register.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('blogs:blog')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully logged In')
                return redirect('blogs:blog')

            else:
                messages.success(
                    request, 'Login failed - Please Try again....')
                return redirect('profiles:login_user')

        else:
            return render(request, 'login.html')


def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(
                    request, 'Profile successfully updated...')
                return redirect('profiles:dashboard')

        else:
            form = EditProfileForm(instance=request.user)

        context = {'form': form}
        return render(request, 'edit_profile.html', context)


def password_update(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(
                    request, 'Password successfully updated...')
                return redirect('profiles:dashboard')

        else:
            form = PasswordChangeForm(user=request.user)

        context = {'form': form}
        return render(request, 'password_update.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out!!!..')
    return redirect('blogs:blog')
