from django.shortcuts import render, redirect, get_object_or_404
from .models import NaturePlace
from .forms import NaturePlaceForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    query = request.GET.get('q')
    if query:
        places = NaturePlace.objects.filter(title__icontains=query)
    else:
        places = NaturePlace.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'places': places, 'query': query})

@login_required
def add_place(request):
    if request.method == 'POST':
        form = NaturePlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NaturePlaceForm()
    return render(request, 'add_place.html', {'form': form})

@login_required
def edit_place(request, pk):
    place = get_object_or_404(NaturePlace, pk=pk)
    form = NaturePlaceForm(request.POST or None, instance=place)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'edit_place.html', {'form': form})

@login_required
def delete_place(request, pk):
    place = get_object_or_404(NaturePlace, pk=pk)
    if request.method == 'POST':
        place.delete()
        return redirect('home')
    return render(request, 'delete_place.html', {'place': place})
