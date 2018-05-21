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

        if dictionaryRequest['Object']=="Meme":

            comment = MemeComment()
            comment.author = User.objects.get(username=dictionaryRequest['author'])
            comment.title = dictionaryRequest['title']
            comment.text = dictionaryRequest['body']
            comment.commented_meme=meme
            comment.save()
        elif dictionaryRequest['Object']=="Comment":

            comment_pk = dictionaryRequest['Comment_pk'].split("/")
            try:
                related_comment = MemeComment.objects.get(pk=comment_pk[0])
                comment = CommentComment()
                comment.author = User.objects.get(username=dictionaryRequest['author'])
                comment.title = dictionaryRequest['title']
                comment.text = dictionaryRequest['body']
                comment.related_comment = related_comment
                comment.save()
            except:
                raise Http404



    try:
        comments = MemeComment.objects.filter(commented_meme=meme)
        context['comments']=comments

        iter = 1
        for comment in comments:
            related_comment = comment
            try:
                context['ComCommentari'] = {related_comment.pk: CommentComment.objects.filter(related_comment=related_comment)}

            except CommentComment.DoesNotExist:
                """"""

    except MemeComment.DoesNotExist:
        comments = None

    return render(request, 'meme.html', context)


def profile(request):

    username = None
    if request.user.is_authenticated:
        Memes = Meme.objects.filter(author=request.user)
        context = {'Memes': Memes}
        return render(request,'Profile.html',context)

    return render(request,'Profile.html')

def uploadMeme(request):
    dictionari = request.POST.dict()
    meme = Meme()
    meme.title = dictionari['title']
    meme.image = request.FILES['image']
    meme.author = User.objects.get(username=dictionari['author'])
    meme.save()
    return render(request,'upload_succesful.html')