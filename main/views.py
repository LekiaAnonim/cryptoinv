from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
class Home(TemplateView):
    template_name = 'main/index.html'