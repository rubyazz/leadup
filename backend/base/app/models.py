from django.db import models
from ckeditor.fields import RichTextField


class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    whichLanguage = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Page(models.Model):
    whichChapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    text = RichTextField(blank=True, null=True)
    example = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name

