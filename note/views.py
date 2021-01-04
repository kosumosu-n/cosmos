from django.shortcuts import render, redirect
from . import forms
from .models import Notes
from django.http import HttpResponse


def index(request):
    formed = forms.Note(request.POST)
    form = forms.Note()
    texted = request.POST.get('text')

    if texted == '':
        return redirect('note:add')
    elif request.method == 'POST' and formed.is_valid():
        Notes(text=texted).save()

    context = {
        'form':form,
        'notes':Notes.objects.all().order_by('-created'),
    }
    return render(request, 'note/index.html', context)

def add(request):
    form = forms.Note()
    context = {
        'form':form,
    }
    return render(request, 'note/add.html', context)

def delete(request, noteid):
    Notes.objects.get(id=noteid).delete()
    return redirect('note:index')