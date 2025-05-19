from django import template
from ..models import Menu
from ..utils import build_menu_tree

register = template.Library()

@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path_info

    menu_items = Menu.objects.filter(menu_name=menu_name).select_related('parent')
    menu_tree = build_menu_tree(menu_items, current_path)

    return {
        'menu_tree': menu_tree,
        'current_path': current_path,
    }