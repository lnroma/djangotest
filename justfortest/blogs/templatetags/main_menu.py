from django import template
from django.http import HttpRequest


register = template.Library()

@register.inclusion_tag('chunks/navigation.html')
def navigation(path):
    from ..models.navigation import Navigation
    request = HttpRequest
    navCollection = Navigation.objects.all()
    return {'navigation':navCollection,'path':path}
