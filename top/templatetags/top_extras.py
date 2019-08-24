from django import template

register = template.Library()


@register.filter(name='remove_br')
def remove_br(raw_html):
    return raw_html.replace('<br>', ' ')
