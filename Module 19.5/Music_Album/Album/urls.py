from django.urls import path, include
from Album.views import *

urlpatterns = [
    path('album/', album, name='album'),
    path('edit/<int:id>', edit, name='edit_album'),
    path('login/', login.as_view(), name='login'),
    path('signup/', sign_up, name='signup'),
    path('logout/', user_logout, name='logout'),
]
