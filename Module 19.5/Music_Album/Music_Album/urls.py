from django.contrib import admin
from django.urls import path, include
from Music_Album.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Album.urls')),
    path('', include('Musicians.urls')),
    path('', home, name='home'),
]