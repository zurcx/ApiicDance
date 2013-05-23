# encoding: utf-8

from .models import Rhythm

def categories(request):
    return {
        'categories': Rhythm.objects.all(),
    }

def sorted(request):
    pass