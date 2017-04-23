from django.template import Library
from urllib.parse import quote_plus


register = template.Library()


@register.filter
def urify(value):
    return quote_plus(value)
