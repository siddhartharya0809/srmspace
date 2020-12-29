from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, logout, login
# from datetime import date
from .forms import NotesForm
from .models import *


# Create your views here.


def srm_space(request):
    return render(request, 'Homepage.html')


def navbar(request):
    return render(request, 'navigation.html')


def go(request):
    context = {}
    if request.method == 'POST':
        upload_file = request.FILES['document']
        # print(upload_file.name)
        # print(upload_file.size)
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        context['url'] = fs.url(name)
    return render(request, 'view_notes.html', context)


def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        description = request.POST['desc']
        print(request)
        # print(name, email, description)
        contact = Contact(name=name, email=email, desc=description)
        contact.save()
    return render(request, 'contact.html')


def view_notes(request):
    notes = Notes.objects.all()
    return render(request, 'view_notes.html', {'notes': notes})


def upload_notes(request):
    if request.method == 'POST':
        uploadfile = request.FILES()
        form = NotesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'File Uploaded Successfully')
            return redirect('/upload_notes')
    else:
        form = NotesForm()
    form = NotesForm
    return render(request, 'upload_notes.html', {'form': form})

# def upload_notes(request):
# if request.method == 'POST':
#     form = NotesForm(request.POST, request.FILES)
#     if form.is_valid():
#         NotesForm(request.FILES['file'])
#         return HttpResponseRedirect('/upload_notes')
# else:
#     form = NotesForm()
# return render(request, 'upload_notes.html', {'form': form})

