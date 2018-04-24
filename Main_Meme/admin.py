from django.contrib import admin
from Main_Meme.models import Meme, Comentari,Vot,Tag,MemeComment,CommentComment

# Register your models here.
admin.site.register(Meme)
admin.site.register(Comentari)
admin.site.register(Vot)
admin.site.register(Tag)
admin.site.register(MemeComment)
admin.site.register(CommentComment)
