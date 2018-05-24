from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from Main_Meme.models import *


# Create your views here.

def home(request):

    memes = Meme.objects.all()
    context = {}
    context['memes'] = memes
    template = 'home.html'
    return render(request, template, context)

def search_memes(request):
    context = {}
    if request.method == 'GET':  # If the form is submitted
        search_query = request.GET.get('search_box', None)
        context['memes'] = Meme.objects.filter(title_contains=search_query)
    template = 'search.html'
    return render(request, template, context)

def memedetails(request, meme_id):

    context = {}
    try:
        meme = Meme.objects.get(pk=meme_id)
        context['meme'] = meme
    except Meme.DoesNotExist:
        raise Http404


    if request.method == "POST":
        dictionaryRequest = request.POST.dict()
        comment = MemeComment()
        comment.author = User.objects.get(username=dictionaryRequest['author'])
        comment.title = dictionaryRequest['title']
        comment.text = dictionaryRequest['body']
        comment.commented_meme=meme
        comment.save()
    try:
        comments = MemeComment.objects.filter(commented_meme=meme)
        context['comments'] = comments
    except MemeComment.DoesNotExist:
        comments = None

    return render(request, 'meme.html', context)

def uploadMeme(request):
    dictionari = request.POST.dict()
    tag = dictionari["tag"]
    meme = Meme()
    meme.title = dictionari['title']
    meme.image = request.FILES['image']
    meme.author = User.objects.get(username=dictionari['author'])
    meme.tag = Tag.objects.get(tags=tag)
    meme.save()
    return render(request,'upload_succesful.html')