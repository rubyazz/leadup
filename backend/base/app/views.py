from django.http import HttpResponse
from django.shortcuts import render

from .models import Chapter, Page


def base(request):
    a = Chapter.objects.all()
    b = Page.objects.filter()
    context = {'a':a, 'b': b}
    return render(request, "base.html", context)

# жеке жеке жасау керек джава бир апп дегендей и каждый теплейтты
