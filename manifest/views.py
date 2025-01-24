from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Manifestation
from .forms import ManifestationForm  # Assuming you have a form for Manifestation

@login_required
def home(request):
    user = request.user
    manifestations = user.manifestations.all()
    print(f"User: {user.username}, Manifestations: {manifestations}")  # Debug statement
    return render(request, 'manifest/home.html', {'user': user, 'manifestations': manifestations})

@login_required
def create_manifestation(request):
    if request.method == 'POST':
        form = ManifestationForm(request.POST)
        if form.is_valid():
            manifestation = form.save()
            request.user.manifestations.add(manifestation)
            return redirect('home')
    else:
        form = ManifestationForm()
    return render(request, 'manifest/create_manifestation.html', {'form': form})

@login_required
def view_manifestation(request, id):
    manifestation = Manifestation.objects.get(id=id)
    return render(request, 'manifest/view_manifestation.html', {'manifestation': manifestation})