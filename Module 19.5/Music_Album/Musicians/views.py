from django.shortcuts import render, redirect
from Musicians.forms import MusicianForm
from Musicians.models import MusicianModel
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def musicians(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            form = MusicianForm()
    else:
        form = MusicianForm()
    return render(request, 'musician.html', {'form':form})

@login_required
def delete(request, id):
    MusicianModel.objects.get(pk=id).delete()
    return redirect('home')

@login_required
def edit_musician(request, id):
    musician = MusicianModel.objects.get(pk=id)
    musician_form = MusicianForm(instance=musician)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'musician.html', {'form':musician_form})
    