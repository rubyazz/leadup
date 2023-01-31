from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Chapter, Page


def main(request):
    return render(request, "main.html")


def python(request):
    a = Chapter.objects.all().prefetch_related('page_set')
    context = {'a':a}
    return render(request, "python.html", context)

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    gg = Page.objects.all()
    context2 = {'page': page, 'gg': gg}
    return render(request, 'page_detail.html', context2)
