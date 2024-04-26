from typing import Iterable
from django.db import models

# Create your models here.


class SiteDescription(models.Model):
    about = models.TextField()

    def __str__(self):
        return self.about
    
    def save(self):
        if SiteDescription.objects.exists():
            self.pk = SiteDescription.objects.first().pk
        super().save()


class Media(models.Model):
    name = models.CharField(max_length=1000)
    url = models.URLField()
    image = models.ImageField(upload_to="media", null=True, blank=True)

    def __str__(self):
        return self.name