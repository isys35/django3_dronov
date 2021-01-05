from django.urls import path

from .views import *

# app_name = 'bboard'
urlpatterns = [
    path('delete/<int:pk>/', BbDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', BbEditView.as_view(), name='edit'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    #path('', BbIndexView.as_view(), name='index')
    path('', index, name='index')
    # path('detail/<int:year>/<int:month>/<int:day>/<int:pk>/', BbDetailView.as_view(), name='delete'),
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