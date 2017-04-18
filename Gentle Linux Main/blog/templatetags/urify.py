from django import template
from urllib.parse import quote_plus


register = template.Library()


@register.filter
def urify(value):
    return quote_plus(value)
