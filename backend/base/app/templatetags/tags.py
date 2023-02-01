from django import template
from ..models import *

register = template.Library()

@register.simple_tag(name='get_list_chapters')
def get_chapters():
    return Chapter.objects.all().prefetch_related('page_set')