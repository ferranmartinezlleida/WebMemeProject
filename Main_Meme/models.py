from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Meme(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(default=None)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return 'Meme: ' + self.title


class Comentari(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=380)
    commented_comment = models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    commented_Meme = models.ForeignKey('Meme', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return 'Comentari: ' + self.title

class Vot(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    voted_meme = models.ForeignKey('Meme', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'Vot: ' + self.voted_meme

class Tag(models.Model):
    name = models.CharField(max_length=30)
    tagged_memes = models.ManyToManyField(Meme)

    def __str__(self):
        return 'Tag: ' + self.voted_meme