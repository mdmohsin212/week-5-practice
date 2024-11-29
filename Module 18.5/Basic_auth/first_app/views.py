from django.shortcuts import render, redirect
from first_app.forms import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'auth.html', {'form' : form, 'type' : 'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            passwd = form.cleaned_data['password']
            user = authenticate(username = name, password = passwd)
            if user is not None:
                login(request, user)
                messages.success(request, "Login Successful")
                return redirect('profile')
            else:
                redirect('signup')
                messages.warning(request, "You have no account")
    else:
        form = AuthenticationForm()
    return render(request, 'auth.html', {'form' : form, 'type' : 'Login'})

@login_required
def profile(requets):
    return render(requets, 'profile.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect('home')


@login_required
def change_pass(requets):
    if requets.method == 'POST':
        form = PasswordChangeForm(user=requets.user, data=requets.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(requets, form.cleaned_data['user'])
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=requets.user)
    return render(requets, 'pass_change.html', {'form' : form, 'type' : 'Change'})

@login_required
def reset_pass(requets):
    if requets.method == 'POST':
        form = SetPasswordForm(user=requets.user, data=requets.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(requets, form.cleaned_data['user'])
            return redirect('profile')
    else:
        form = SetPasswordForm(user=requets.user)
    return render(requets, 'pass_change.html', {'form' : form, 'type' : 'Reset'})

# 123456SI