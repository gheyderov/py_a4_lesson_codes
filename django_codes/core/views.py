from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from stories.models import Category
from core.forms import ContactForm
from core.models import Contact
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Thanks for your message!")
            return redirect(reverse_lazy('contact'))
        
    context = {
        'form' : form
    }
    return render(request, 'contact.html', context)