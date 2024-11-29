from django.shortcuts import render, redirect
from Album.forms import *
from Album.models import AlbumModel
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def album(request):
    if request.method == 'POST':
        form = ALbumForm(request.POST)
        if form.is_valid():
            form.save()
            form = ALbumForm()
    else:
        form = ALbumForm()
    return render(request, 'album.html', {'form' : form})

@login_required
def edit(request, id):
    album = AlbumModel.objects.get(pk=id)
    album_form = ALbumForm(instance=album)
    if request.method == 'POST':
        post_form = ALbumForm(request.POST, instance=album)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')
        
    return render(request, 'album.html', {'form' : album_form})


class login(LoginView):
    model = AuthenticationForm
    template_name = 'auth.html'
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login'
        return context

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'auth.html', {'form' : form, 'type' : 'Signup'})

def user_logout(request):
    logout(request)
    return redirect('home')

# 123456SI