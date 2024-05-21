from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from base.models import Table

# Create your views here.
class IndexView(ListView):
    model = Table
    template_name = 'base/index.html'
    context_object_name = 'tables'