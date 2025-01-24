from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from .models import Manifestation
from .forms import ManifestationForm  # Assuming you have a form for Manifestation
from django.http import HttpResponseForbidden

@login_required
def home(request):
    manifestations = Manifestation.objects.filter(owner=request.user)
    return render(request, 'manifest/home.html', {'manifestations': manifestations})

@login_required
def create_manifestation(request):
    if request.method == 'POST':
        form = ManifestationForm(request.POST)
        if form.is_valid():
            manifestation = form.save(commit=False)
            manifestation.owner = request.user
            manifestation.save()
            return redirect('view_manifestation', manifestation_id=manifestation.id)
    else:
        form = ManifestationForm()
    return render(request, 'manifest/create_manifestation.html', {'form': form})

@login_required
def view_manifestation(request, manifestation_id):
    manifestation = get_object_or_404(Manifestation, id=manifestation_id)
    
    if manifestation.owner != request.user and not (manifestation.is_public and manifestation.is_approved):
        return HttpResponseForbidden("You do not have permission to view this manifestation.")
    
    if manifestation.is_charged and timezone.now() > manifestation.last_charged + timedelta(minutes=2):
        manifestation.is_charged = False
        manifestation.save()
    if manifestation.last_charged and timezone.now() > manifestation.last_charged + timedelta(minutes=1):
        manifestation.can_charge = True
        manifestation.save()
    context = {
        'manifestation': manifestation,
        'next_charge_time': manifestation.next_charge_time()
    }
    return render(request, 'manifest/view_manifestation.html', context)

@login_required
def charge_manifestation(request, id):
    manifestation = get_object_or_404(Manifestation, id=id)
    if request.method == 'POST':
        manifestation.is_charged = True
        manifestation.can_charge = False
        manifestation.last_charged = timezone.now()
        manifestation.save()
        return redirect('view_manifestation', manifestation_id=id)
    return render(request, 'manifest/view_manifestation.html', {'manifestation': manifestation})

@login_required
def edit_manifestation(request, id):
    manifestation = get_object_or_404(Manifestation, id=id)
    if request.method == 'POST':
        form = ManifestationForm(request.POST, instance=manifestation)
        if form.is_valid():
            form.save()
            return redirect('view_manifestation', manifestation_id=manifestation.id)
    else:
        form = ManifestationForm(instance=manifestation)
    return render(request, 'manifest/edit_manifestation.html', {'form': form, 'manifestation': manifestation})

@login_required
def delete_manifestation(request, id):
    manifestation = get_object_or_404(Manifestation, id=id)
    if request.method == 'POST':
        manifestation.delete()
    return redirect('home')