from django.db import models

from django.urls import reverse


class Storie(models.Model):
    title=models.CharField(max_length=45)
    story=models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ("story", kwargs={"id":self.id})

