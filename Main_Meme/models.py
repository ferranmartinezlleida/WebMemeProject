from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Meme(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return 'Meme: ' + self.title


class Comentari(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=380)


class MemeComment(Comentari):
    commented_meme = models.ForeignKey('Meme', on_delete=models.CASCADE,null=True)


class CommentComment(Comentari):
    related_comment = models.ForeignKey('Comentari', related_name='thread', on_delete=models.CASCADE, null=True)



VALUES = (
        (1, 'Positive'),
        (2, 'Negative'),
    )


class Vot(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    voted_meme = models.ForeignKey('Meme', on_delete=models.CASCADE, null=True)
    value = models.PositiveIntegerField(null=True, blank=True, choices=VALUES)

    def __str__(self):
        return 'Vot: ' + self.voted_meme

class Tag(models.Model):
    name = models.CharField(max_length=30)
    tagged_memes = models.ManyToManyField(Meme)

    def __str__(self):
        return 'Tag: ' + self.name