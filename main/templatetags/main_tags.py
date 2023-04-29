from django import template
from main.models import *

register = template.Library()


@register.inclusion_tag('main/tags/home_categories.html')
def show_categories(cur_cat=0):
    return {'cats': Categories.objects.all(), 'cur_cat': cur_cat}


@register.inclusion_tag('main/tags/base_menu.html')
def show_menu(cur):
    menu = [
        {'name': 'home', 'url': 'home'},
    ]
    return {'menu': menu, 'cur': cur}


@register.inclusion_tag('main/tags/base_menu_auth.html')
def show_menu_auth(cur):
    menu = [
        {'name': 'home', 'url': 'home'},
        {'name': 'Создать публикацию', 'url': 'add_post'},
    ]
    return {'menu': menu, 'cur': cur}