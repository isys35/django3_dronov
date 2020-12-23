from django.urls import path

from .views import index, by_rubric, BbCreateView

# app_name = 'bboard'
urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index')
]


"""
    Указание шаблонных путей в виде регулярных выражений
    Листинг 8.4
"""

# from django.urls import re_path

# urlpatterns = [
#     re_path(r'^add/$', BbCreateView.as_view(), name='add'),
#     path(r'^(?P<rubric_id>[0-9]*)/$', by_rubric, name='by_rubric'),
#     path(r'^$', index, name='index')
# ]