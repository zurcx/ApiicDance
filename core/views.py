# encoding: utf-8

from django.views.generic import TemplateView, ListView

from dance.models import Rhythm

class HomeView(ListView):

    template_name = 'home.html'

    def get_queryset(self):
        return Rhythm.objects.filter(features=True)

