from django.urls import path, include
from first_app.views import *

urlpatterns = [
    path('signup/', user_signup, name='signup'),
    path('login/', user_login, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', user_logout, name='logout'),
    path('pass_change/', change_pass, name='pass_change'),
    path('pass_reset/', reset_pass, name='pass_reset'),
]