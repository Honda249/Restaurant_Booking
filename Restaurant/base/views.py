from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Table

# Create your views here.

def index(request):
   tables = Table.object.get()
   return render(request,'base/index.html')

class TableListView(ListView):
    model = Table
    template_name = 'base/index.html'
    context_object_name = 'tables'