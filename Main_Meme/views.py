from django.shortcuts import render
from Main_Meme.models import *

# Create your views here.

def home(request):

    memes = Meme.objects.all()
    context = {}
    context['memes'] = memes
    template = 'home.html'
    return render(request, template, context)