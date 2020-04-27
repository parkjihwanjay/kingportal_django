from django.db import models

# Create your models here.


class Chats(models.Model):
    content = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.content
