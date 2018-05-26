from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Meme(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'Meme: ' + self.title


class MemeComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=380)
    commented_meme = models.ForeignKey('Meme', on_delete=models.CASCADE,null=True)


class CommentComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=380)
    related_comment = models.ForeignKey('MemeComment', on_delete=models.CASCADE, null=True)



VALUES = (
        (1, 'Positive'),
        (2, 'Negative'),
    )


class Vot(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    voted_meme = models.ForeignKey('Meme', on_delete=models.CASCADE, null=True)
    value = models.PositiveIntegerField(null=True, blank=True, choices=VALUES)

    def __str__(self):
        return 'Vot: ' + self.voted_meme.title

class Tag(models.Model):
    TAG_CHOICES = (
        (1, 'NSFW'), (2, 'Animals'), (3, 'Edgy'), (4, 'Movies'),
        (5, 'Dead Meme'), (6, 'Cringe'), (7, 'Sports'),
        (8, 'Politics'), (9, 'Work'), (10, 'Country')
    )
    tags = models.PositiveIntegerField(null=True, blank=True, choices=TAG_CHOICES)

    def __str__(self):
        return "%s" % (self.TAG_CHOICES[self.tags-1][1])
