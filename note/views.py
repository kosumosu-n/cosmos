from django.shortcuts import render, redirect
from . import forms
from .models import Notes
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy, reverse


class Index(generic.ListView):
    model = Notes
    template_name = 'note/index.html'
    
class Add(generic.CreateView):
    model = Notes
    template_name = 'note/add.html'
    form_class = forms.Notes
    success_url = reverse_lazy('note:index')

class Delete(generic.DeleteView):
    model = Notes
    template_name = 'note/delete.html'
    success_url = reverse_lazy('note:index')

class Detail(generic.DetailView):
    model = Notes
    template_name = 'note/detail.html'

class Edit(generic.UpdateView):
    model = Notes
    template_name = 'note/edit.html'
    form_class = forms.Notes
    def get_success_url(self):
        return reverse("note:detail", kwargs={'pk':self.kwargs['pk']})
