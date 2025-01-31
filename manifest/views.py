from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from .models import Manifestation
from .forms import ManifestationForm  # Assuming you have a form for Manifestation
from django.http import HttpResponseForbidden

@login_required
def home(request):
    manifestations = Manifestation.objects.filter(owner=request.user).order_by('created_on')
    for manifestation in manifestations:
        if manifestation.is_charged and timezone.now() > manifestation.last_charged + timedelta(minutes=2):
            manifestation.is_charged = False
            manifestation.save()
        if manifestation.last_charged and timezone.now() > manifestation.last_charged + timedelta(minutes=1):
            manifestation.can_charge = True
            manifestation.save()

    context = {
        'manifestations': manifestations,
    }

    return render(request, 'manifest/home.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def create_manifestation(request):
    if request.method == 'POST':
        form = ManifestationForm(request.POST)
        if form.is_valid():
            manifestation = form.save(commit=False)
            manifestation.owner = request.user
            manifestation.save()
            return redirect('view_manifestation', slug=manifestation.slug)
    else:
        form = ManifestationForm()
    return render(request, 'manifest/create_manifestation.html', {'form': form})

def view_manifestation(request, slug):
    manifestation = get_object_or_404(Manifestation, slug=slug)
    
    if manifestation.owner != request.user and not (manifestation.is_public and manifestation.is_approved):
        return render(request, 'manifest/forbidden.html')
    
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
    
    return render(request, 'manifest/view_manifestation.html', {'manifestation': manifestation})

@login_required
def charge_manifestation(request, slug):
    manifestation = get_object_or_404(Manifestation, slug=slug)
    if request.method == 'POST':
        manifestation.is_charged = True
        manifestation.can_charge = False
        manifestation.last_charged = timezone.now()
        manifestation.save()
        return redirect('view_manifestation', slug=manifestation.slug)
    return render(request, 'manifest/view_manifestation.html', {'manifestation': manifestation})

@login_required
def edit_manifestation(request, slug):
    manifestation = get_object_or_404(Manifestation, slug=slug)
    if request.method == 'POST':
        form = ManifestationForm(request.POST, instance=manifestation)
        if form.is_valid():
            manifestation.is_approved = False  # Set is_approved to False
            form.save()
            return redirect('view_manifestation', slug=manifestation.slug)
    else:
        form = ManifestationForm(instance=manifestation)
    return render(request, 'manifest/edit_manifestation.html', {'form': form, 'manifestation': manifestation})

@login_required
def delete_manifestation(request, slug):
    manifestation = get_object_or_404(Manifestation, slug=slug)
    if request.method == 'POST':
        manifestation.delete()
        return redirect('home')  # Redirect to a different view after deletion
    return render(request, 'manifest/delete_manifestation.html', {'manifestation': manifestation})

def public_manifestations(request):
    manifestations = Manifestation.objects.filter(is_public=True, is_approved=True)
    return render(request, 'manifest/public_manifestations.html', {'manifestations': manifestations})

def profile(request):
    return render(request, 'manifest/profile.html')

def change_password(request):
    # Your change password logic here
    return render(request, 'manifest/change_password.html')

def success(request):
    return render(request, 'manifest/success.html')