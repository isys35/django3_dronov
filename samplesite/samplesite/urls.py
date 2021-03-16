"""samplesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('bboard.urls')),
    # path('bboard/', include('bboard.urls')),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls'))
]

"""
    Список маршрктов уровня проекто, включающий список маршрутов уровня приложения
    Листинг 8.3
"""
# from samplesite.bboard.views import index,by_rubric, BbCreateView
# urlpatterns = [
#     path('bboard/', include([
#         path('add/', BbCreateView.as_view(), name='add'),
#         path('<int:rubric_id>/', by_rubric, name='by_rubric'),
#         path('', index, name='index')
#     ])),
#     path('admin/', admin.site.urls),
# ]
