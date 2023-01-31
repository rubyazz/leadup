from django.http import HttpResponse
from django.shortcuts import render

from .models import Chapter, Page


def base(request):
    a = Chapter.objects.all().prefetch_related('page_set')
    context = {'a':a}
    return render(request, "python.html", context)


