from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.urls import reverse
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
        context['memes'] = Meme.objects.filter(title__contains=search_query)
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

        if dictionaryRequest['Object'] == "AlterComment":

            if dictionaryRequest['type'] == "MMC":

                try:
                    comentari = MemeComment.objects.get(pk=dictionaryRequest['key'])
                except:
                    """"""
            else:

                try:
                    comentari = CommentComment.objects.get(pk=dictionaryRequest['key'])
                except:
                    """"""
            if dictionaryRequest['Action'] == "Delete":

                comentari.delete()

            else:
                comentari.text = dictionaryRequest['body']
                comentari.title = dictionaryRequest['title']
                comentari.save()


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

        elif dictionaryRequest['Object'] == "Vote":

            try:
                vote = Vot.objects.get(author=request.user,voted_meme=meme)
                if dictionaryRequest['value']=='positive':
                    vote.value = 1
                else:
                    vote.value = 2
                vote.save()
            except:
                vote = Vot()
                vote.author = request.user
                if dictionaryRequest['value'] == 'positive':
                    vote.value = 1
                else:
                    vote.value = 2
                vote.voted_meme = meme
                vote.save()

        return HttpResponseRedirect("/meme/"+str(meme.pk))

    try:
        votes = Vot.objects.filter(voted_meme=meme)

        context['positive'] = 0
        context['negative'] = 0

        for vot in votes:
            if vot.value is 1:
                context['positive']+=1
            else:
                context['negative']+=1

        context['totalpuntuation'] = context['positive'] - context['negative']

    except:

        context['totalpuntuation'] = 0
        context['positive'] = 0
        context['negative'] = 0



    try:
        comments = MemeComment.objects.filter(commented_meme=meme)
        context['comments']=comments

        dict = {}
        for comment in comments:
            related_comment = comment
            context['ComComment'] = dict
            try:
                dict[related_comment.pk] = CommentComment.objects.filter(related_comment=related_comment)
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



def deleteMeme(request):

    dictionari = request.POST.dict()
    try:
        meme = Meme.objects.get(id=dictionari['Delete'])
    except:
        return HttpResponseRedirect("/profile/")
    title = meme.title
    meme.delete()
    return render(request,"meme_delete.html",{"meme_title":title})


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