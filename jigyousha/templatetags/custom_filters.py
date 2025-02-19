from django import template

register = template.Library()

@register.filter
def display_none(value):
    if value is None or value == '':
        return '情報なし'
    return value