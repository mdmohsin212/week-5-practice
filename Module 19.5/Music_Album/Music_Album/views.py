from django.shortcuts import render, redirect
from Album.models import AlbumModel

def home(request):
    data = AlbumModel.objects.all()
    return render(request, 'index.html', {'data' : data})

