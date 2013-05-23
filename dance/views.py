# encoding: utf-8

import random

from django.shortcuts import get_object_or_404

from django.views.generic import DetailView, ListView

from .models import DanceStep, Rhythm

class DanceStepView(DetailView):
    template_name = 'dance/dancestep.html'
    model = DanceStep
    context_object_name = 'dancestep'

class DanceStepListView(ListView):

    template_name = 'dance/dancesteps.html'
    paginate_by = 12


    # # Original
    # def get_queryset(self):
    #     rhythm_slug = self.kwargs.get('slug')
    #     rhythm = get_object_or_404(Rhythm, slug=rhythm_slug)
    #     return rhythm.dancesteps.all()

     # Original
    def get_queryset(self):
        rhythm_slug = self.kwargs.get('slug')
        rhythm = get_object_or_404(Rhythm, slug=rhythm_slug)
        # items = list(rhythm.dancesteps.all().order_by('pk')[:10])
        return rhythm.dancesteps.all().order_by('?')[:15]
        # count = rhythm.dancesteps.all().count()
        # slice = random.random() * (count - 10)
        # rhythm.objects.all()[slice: slice+10]


    #opcao 1

    # def get_queryset(self):
    #     rhythm_slug = self.kwargs.get('slug')
    #     rhythm = get_object_or_404(Rhythm, slug=rhythm_slug)
         # sorteado = list(rhythm.dancesteps.all()[:5])
    #     return random.shuffle(sorteado)

    # #     return sorteado[0]

    # opcao 2

    # def get_queryset(self):
    #     rhythm_slug = self.kwargs.get('slug')
    #     rhythm = get_object_or_404(Rhythm, slug=rhythm_slug)
    #     items = list(rhythm.dancesteps.all()[:25])
    #     try:
    #         items = items.remove('')
    #     except:
    #         return random.shuffle(items)

    # opcao 3


    # def get_queryset(self):
    #     cont = 0
    #     rhythm_slug = self.kwargs.get('slug')
    #     rhythm = get_object_or_404(Rhythm, slug=rhythm_slug)
    #     cont = rhythm.dancesteps.all().count()
    #     rand_ids = range(0, cont)
    #     random.shuffle(rand_ids)

    #     # gerar range e sortear

    #     return rhythm.dancesteps.filter(pk=2)

    # opcao 4

    # def get_queryset(self):
    #     rhythm_slug = self.kwargs.get('slug')
    #     rhythm = get_object_or_404(Rhythm, slug=rhythm_slug)
    #     num_steps = rhythm.dancesteps.all().count()
    #     ger = range(0, num_steps)

    #     nr_step = random.shuffle(ger)


    #     return rhythm.dancesteps.filter(id=2)


        # items = list(rhythm.dancesteps.all()[:25])
        # return random.shuffle(items)
