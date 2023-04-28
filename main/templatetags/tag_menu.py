from django import template
from main.models import Menu, Items

register = template.Library()

@register.inclusion_tag('main/draw_menu.html')
def draw_menu(menu_name, select=''):
    menu = Menu.objects.get(name=menu_name)
    items = Items.objects.all()
    return {'menu': menu, 'items': items, 'select': select}