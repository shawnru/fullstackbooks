from __future__ import unicode_literals
from django.db import models

class Bookmanager(models.Manager):
    def addbooks(self, postdata):
        if postdata:
            book = self.create(name=postdata['name'],author=postdata['author'],category=postdata['category'])

class Book(models.Model):
    name = models.CharField(max_length=38)
    author = models.CharField(max_length= 38)
    category = models.CharField(max_length= 38)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = Bookmanager()
