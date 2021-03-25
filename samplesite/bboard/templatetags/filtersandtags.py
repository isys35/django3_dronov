"""
    Листинг 19.1 Пример создания фильтра
"""

# from django import template
#
# register = template.Library()
#
#
# def currency(value, name='руб. '):
#     return '%1.2f %s' % (value, name)
#
#
# register.filter('currency', currency)

"""
    Листинг 19.2 Пример объявления тега, выводящего элементарное значение
"""

# from django import template
#
# register = template.Library()
#
#
# @register.simple_tag
# def lst(sep, *args):
#     return '%s (итого %s)' % (sep.join(args), len(args))

"""
    Листинг 19.3 Пример шаблонного тега
"""

# from django import template
#
# register = template.Library()
#
#
# @register.inclusion_tag('tags/ulist.html')
# def ulist(*args):
#     return {'items': args}
