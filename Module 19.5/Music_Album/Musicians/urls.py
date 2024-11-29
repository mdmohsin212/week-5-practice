from django.urls import path, include
from Musicians.views import *

urlpatterns = [
    path('musicians/', musicians, name='musicians'),
    path('edit_musicians/<int:id>', edit_musician, name='edit_musicians'),
    path('delete/<int:id>', delete, name='delete_album'),
]
