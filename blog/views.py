from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Computers, Categary, Man_clothes, Womans_clothes
from .forms import ContactForm
from django.views.generic import UpdateView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
class ComputersUpdateView(UpdateView):
    model = Computers
    fields = ('name', 'bio', 'img', 'price', 'old_price')
    template_name = 'ComputersEdit.html'

class ComputersDeleteView(DeleteView):
    model = Computers
    template_name = 'ComputersDelete.html'
    success_url = reverse_lazy('index')

class ComputersCreateView(CreateView):
    model = Computers
    template_name = 'ComputersCreate.html'
    fields = ('name', 'bio', 'img', 'price', 'old_price')

def index(request):
    computers = Computers.objects.all()
    man = Man_clothes.objects.all()
    womans = Womans_clothes.objects.all()
    categary = Categary.objects.all()
    contact = ContactForm(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!!!<h2>")
    context = {
        "computers": computers,
        "man": man,
        "womans": womans,
        "contact": contact,
        "categary": categary,
    }
    return render(request, 'index.html', context=context)

def computers(request):
    computers = Computers.object.all()
    context = {
        'computers': computers
    }
    return render(request, 'computers.html', context=context)

def contact(request):
    contact = ContactForm(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!!!</h2>")
    context = {
        "contact": contact
    }
    return render(request, 'contact.html', context=context)

def man_clothes(request):
    man = Man_clothes.objects.all()
    context = {
        "man": man
    }
    return render(request, 'mans_clothes.html', context=context)

def womans_clothes(request):
    woman = Womans_clothes.objects.all()
    context = {
        "woman": woman
    }
    return render(request, 'womans_clothes.html', context=context)

def womansDetailView(request):
    return render(request, 'womansDetailView', context={})

def computersDetailView(request, computers):
    computers = get_object_or_404(Computers, slug=computers)
    context = {
        'computers': computers
    }
    return render(request, 'computersDetailView', context=context)

def manDetailView(request):
    return render(request, 'manDetailView', context={})



