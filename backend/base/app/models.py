from django.db import models
from ckeditor.fields import RichTextField


# class Python(models.Model):
#     name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = "Python"
#         verbose_name_plural = "Python"


class Chapter(models.Model):
    # whichLanguage = models.ForeignKey(Python, on_delete=models.CASCADE)
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

