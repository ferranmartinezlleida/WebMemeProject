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
        tagged_meme = Tag.objects.filter(tagged_meme=meme)
        context['comments'] = comments
        context['tagged_meme'] = tagged_meme
    except MemeComment.DoesNotExist:
        comments = None

    return render(request, 'meme.html', context)

def uploadMeme(request):
    dictionari = request.POST.dict()
    meme = Meme()
    meme.title = dictionari['title']
    meme.image = request.FILES['image']
    meme.author = User.objects.get(username=dictionari['author'])
    meme.save()
    tag = Tag()
    tag.tags = dictionari['tag']
    try:
        tag.tagged_meme = Meme.objects.get(title=dictionari['title'])
    except Meme.DoesNotExist:
        raise Http404
    tag.save()
    return render(request,'upload_succesful.html')