from django.shortcuts import render
from django.views import generic
from .models import Browser
    
class master(generic.ListView):
    template_name='Lab8App/master.html'
    context_object_name='Browsers'
    allow_empty=True
    def get_queryset(self):
        return Browser.objects.all()

class detail(generic.DetailView):
    model=Browser
    template_name='Lab8App/detail.html'
    
# Create your views here.
