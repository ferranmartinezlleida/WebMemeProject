from django.http import Http404
from django.shortcuts import render
from Main_Meme.models import *


# Create your views here.

def home(request):

    memes = Meme.objects.all()
    context = {}
    context['memes'] = memes
    template = 'home.html'
    return render(request, template, context)



def memedetails(request, meme_id):

    context = {}
    try:
        meme = Meme.objects.get(pk=meme_id)
        context['meme'] = meme
    except Meme.DoesNotExist:
        raise Http404
    try:
        comments = MemeComment.objects.filter(commented_meme=meme)
        context['comments']=comments
    except MemeComment.DoesNotExist:
        comments = None

    return render(request, 'meme.html', context)
