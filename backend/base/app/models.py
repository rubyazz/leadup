from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse



class Chapter(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Page(models.Model):
    whichChapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug=models.SlugField(max_length=250, null=True, blank=True)
    text = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})
