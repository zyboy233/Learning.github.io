from django.template import Library

register = Library()

@register.filter
def my_filter(value):
    pass

