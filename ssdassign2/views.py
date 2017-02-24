from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from ssdassign2.forms import ProfileAvatarForm
from ssdassign2.models import ProfileAvatar

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile.html')

def profile-edit(request):
    return render(request, 'profile-edit.html')

def avatar(request):
    return render(request, 'avatar.html')

def avatar-edit(request):
    return render(request, 'avatar-edit.html')