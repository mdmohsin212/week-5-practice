from django import forms
from Album.models import AlbumModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ALbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = '__all__'