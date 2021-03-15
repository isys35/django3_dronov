from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import *

app_name = 'bboard'
urlpatterns = [
    path('delete/<int:pk>/', BbDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', BbEditView.as_view(), name='edit'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    # path('', BbIndexView.as_view(), name='index')
    path('', index, name='index'),
    path('rubrics', rubrics, name='rubrics'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='bboard:index'), name='logout'),
    path('accounts/password_change/', PasswordChangeView.as_view(template_name='registration/change_password.html'),
         name='password_change'),
    path('accounts/password_change/done/',
         PasswordChangeDoneView.as_view(template_name='registration/password_changed.html'),
         name='password_change_done'),
    path('accounts/password_reset/',
         PasswordResetView.as_view(template_name='registration/reset_password.html',
                                   subject_template_name='registration/reset_subjects.txt',
                                   email_template_name='registration/reset_email.txt'
                                   ),
         name='password_reset'),
    path('accounts/password_reset/done/',
         PasswordResetDoneView.as_view(template_name='registration/email_sent.html'),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='registration/confirm_password.html'),
         name='password_reset_confirm'),
    path('accounts/reset/done',
         PasswordResetCompleteView.as_view(template_name='registration/password_confirmed.html'),
         name='password_reset_complete'),
    # path('detail/<int:year>/<int:month>/<int:day>/<int:pk>/', BbDetailView.as_view(), name='delete'),
    path('search', search, name='search')
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
