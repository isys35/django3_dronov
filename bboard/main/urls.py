
from django.urls import path

from .views import index, other_page, BBLoginView, profile, LogoutView, ChangeUserInfoView

app_name = 'main'

urlpatterns = [
    path('accounts/profile/change', ChangeUserInfoView.as_view(),
         name='profile_change'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]