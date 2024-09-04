from django import template

register = template.Library()

@register.filter(name='reverse_string')
def reverse_string(value):
    return value[::-1]


@register.filter(name='reverse_string2')
def reverse_string(value):
    return value[::-1]
