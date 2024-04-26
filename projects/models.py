from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    link = models.URLField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    technologies = models.ManyToManyField(Technology)

    def __str__(self):
        return f"{self.title[:100]} - {self.category}"