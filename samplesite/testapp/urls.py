from django.urls import path
from .views import add, index

app_name = 'testapp'
urlpatterns = [
    #path('get/<path:filename>', get, name='get'),
    path('add/', add, name='add'),
    path('', index, name='index'),
    ]

