from django import template
from news.models import Category, News
from django.db.models import Count, F

register = template.Library()


@register.simple_tag()
def get_categories():
    cats = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    return cats


@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='Hello', arg2='world'):
    cats = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    return {'cats': cats, 'arg1': arg1, 'arg2': arg2}
