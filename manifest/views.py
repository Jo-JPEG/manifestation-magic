from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
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
            return redirect('view_manifestation', id=manifestation.id)
    else:
        form = ManifestationForm()
    return render(request, 'manifest/create_manifestation.html', {'form': form})

@login_required
def view_manifestation(request, id):
    manifestation = Manifestation.objects.get(id=id)
    if manifestation.is_charged and timezone.now() > manifestation.last_charged + timedelta(minutes=1):
        manifestation.is_charged = False
        manifestation.save()
    return render(request, 'manifest/view_manifestation.html', {'manifestation': manifestation})

@login_required
def charge_manifestation(request, id):
    manifestation = get_object_or_404(Manifestation, id=id)
    if request.method == 'POST':
        manifestation.is_charged = True
        manifestation.last_charged = timezone.now()
        manifestation.save()
        return redirect('view_manifestation', id=id)
    return render(request, 'manifest/view_manifestation.html', {'manifestation': manifestation})

@login_required
def edit_manifestation(request, id):
    manifestation = get_object_or_404(Manifestation, id=id)
    if request.method == 'POST':
        form = ManifestationForm(request.POST, instance=manifestation)
        if form.is_valid():
            form.save()
            return redirect('view_manifestation', id=manifestation.id)
    else:
        form = ManifestationForm(instance=manifestation)
    return render(request, 'manifest/edit_manifestation.html', {'form': form, 'manifestation': manifestation})

@login_required
def delete_manifestation(request, id):
    manifestation = get_object_or_404(Manifestation, id=id)
    if request.method == 'POST':
        manifestation.delete()
        return redirect('home')
    return render(request, 'manifest/delete_manifestation.html', {'manifestation': manifestation})