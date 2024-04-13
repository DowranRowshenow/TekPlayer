from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, View


class MainView(TemplateView):
    template_name='main/main.html'
