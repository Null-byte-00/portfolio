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


class Resume(models.Model):
    resume = models.TextField()

    def __str__(self):
        return self.resume
    
    def save(self):
        if Resume.objects.exists():
            self.pk = Resume.objects.first().pk
        super().save()


class Biography(models.Model):
    bio = models.TextField()

    def __str__(self):
        return self.bio
    
    def save(self):
        if Biography.objects.exists():
            self.pk = Biography.objects.first().pk
        super().save()


class Experience(models.Model):
    experience = models.TextField()

    def __str__(self):
        return self.experience
    
    def save(self):
        if Experience.objects.exists():
            self.pk = Biography.objects.first().pk
        super().save()


class Media(models.Model):
    name = models.CharField(max_length=1000)
    url = models.URLField()
    image = models.ImageField(upload_to="media", null=True, blank=True)

    def __str__(self):
        return self.name