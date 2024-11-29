from django.contrib import admin
from django.urls import path, include
from Basic_auth.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first_app.urls')),
    path('', Home, name='home'),
]
