from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls.base import reverse_lazy
from .models import Words, Examples
from django.views import generic
from . import forms
import urllib

class Index(generic.ListView):
    model = Words
    template_name = 'ew/index.html'


def detail(request, slug):
    word = Words.objects.get(spell=slug)
    l = word.example.split(',')
    em = []
    if l[0] != "":
        for n in l:
            em.append(Examples.objects.get(id=n))


    context = {
        'spell':word.spell,
        'ts':word.ts,
        'pt':word.pt,
        'pp':word.pp,
        'prp':word.prp,
        'em':em,
    }
    return render(request, 'ew/detail.html', context)

def add(request):
    if request.method == 'POST' and forms.AddForm(request.POST).is_valid():
        spells = request.POST.get('spell').splitlines()
        tss = request.POST.get('ts').splitlines()
        pts = request.POST.get('pt').splitlines()
        pps = request.POST.get('pp').splitlines()
        prps = request.POST.get('prp').splitlines()
        check = bool(request.POST.get('check'))
        
        while len(tss) < len(spells):
            tss.append('')
        while len(pts) < len(spells):
            pts.append('')
        while len(pps) < len(spells):
            pps.append('')
        while len(prps) < len(spells):
            prps.append('')
            
        for i in range(len(spells)):
            if spells[i] == "":
                continue
            if tss[i] == "":
                tss[i] = urllib.request.urlopen('https://script.google.com/macros/s/AKfycbwkyQRECE5BKckS2bG4j6BSKwxig9APtAw2367ssoBR4qUb7II7IwfSqzKj8ewNvh2J/exec?text=' + spells[i]).read()
            examples = Examples.objects.filter(sentence__icontains=tss[i])
            etext = ""
            for e in examples:
                etext = etext +"," + str(e.id)
            Words(spell=spells[i], ts=tss[i], pt=pts[i], pp=pps[i], prp=prps[i], example=etext, wverb=check).save()
        return redirect('ew:index')
                


    context = {
        "form":forms.AddForm,
    }
    return render(request, 'ew/add.html', context)
    
class Edit(generic.UpdateView):
    model = Words
    template_name = 'ew/edit.html'
    form_class = forms.Wuf
    slug_field = 'spell'
    def get_success_url(self):
        return reverse("ew:detail", kwargs={'slug':self.kwargs['slug']})
        
class Delete(generic.DeleteView):
    model = Words
    template_name = 'ew/delete.html'
    success_url = reverse_lazy('ew:index')
    slug_field = 'spell'

class Examplesview(generic.ListView):
    model = Examples
    template_name = 'ew/examples.html'

class Exadd(generic.CreateView):
    model = Examples
    template_name = 'ew/exadd.html'
    form_class = forms.Exaf
    success_url = reverse_lazy('ew:examples')

class Exedit(generic.UpdateView):
    model = Examples
    template_name = 'ew/exedit.html'
    form_class = forms.Exuf
    success_url = reverse_lazy('ew:examples')

class Exdelete(generic.DeleteView):
    model = Examples
    template_name = 'ew/exdelete.html'
    success_url = reverse_lazy('ew:examples')