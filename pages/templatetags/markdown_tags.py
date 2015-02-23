import markdown2

from django import template

register = template.Library()


@register.filter
def markdown_to_html(markdown_c):
    return markdown2.markdown(markdown_c)
