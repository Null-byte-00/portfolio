from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.text import slugify
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title
    

@receiver(post_save, sender=Article)
def create_slug(sender, instance, created, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        instance.save()