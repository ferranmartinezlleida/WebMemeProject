from django.contrib import admin
from Main_Meme.models import *

# Register your models here.
admin.site.register(Meme)
admin.site.register(Vot)
admin.site.register(Tag)
admin.site.register(MemeComment)
admin.site.register(CommentComment)
