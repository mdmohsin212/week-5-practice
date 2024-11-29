from django.shortcuts import render

def Home(requets):
    return render(requets, 'home.html')