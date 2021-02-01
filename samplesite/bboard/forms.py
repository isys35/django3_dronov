from django.forms import ModelForm
from django.forms.widgets import Select
from django.forms import modelform_factory, DecimalField

from .models import Bb

"""
    Быстрое объявление формы, связанной с моделью
    Листинг 13.2
"""


class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')
        labels = {'title': 'Название товара'}
        help_texts = {'rubric': 'Не забудьте задать рубрику'}
        field_classes = {'price': DecimalField}
        widgets = {'rubric': Select(attrs={'size': 8})}


"""
    Использование фабрики классов modelform_factory()
    Листинг 13.1
"""

#
# BbForm = modelform_factory(Bb,
#                            fields=('title', 'content', 'price', 'rubric'),
#                            labels={'title': 'Название товара'},
#                            help_texts={'rubric': 'Не забудьте выбрать рубрику!'},
#                            field_classes={'price': DecimalField},
#                            widgets={'rubric': Select(attrs={'size':8})})


"""
    Полное объявление формы
    Листинг 13.3
"""
# from django import forms
# from .models import Bb, Rubric
#
#
# class BbForm(forms.ModelForm):
#     title = forms.CharField(label='Название товара')
#     content = forms.CharField(label='Описание', widget=forms.widgets.Textarea())
#     price = forms.DecimalField(label='Цена', decimal_places=2)
#     rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),
#                                     label='Рубрика',
#                                     help_text='Не забудьте задать рубрику!',
#                                     widget=forms.widgets.Select(attrs={'size': 8}))
#
#     class Meta:
#         model = Bb
#         fields = ('title', 'content', 'price', 'rubric')

"""
    Полное объявление отдельных полей формы
    Листинг 13.4
"""
# from django import forms
# from .models import Bb, Rubric
#
#
# class BbForm(forms.ModelForm):
#     price = forms.DecimalField(label='Цена', decimal_places=2)
#     rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),
#                                     label='Рубрика', help_text='Не забудьте задать рубрику!',
#                                     widget=forms.widgets.Select(attrs={'size': 8}))
#
#     class Meta:
#         model = Bb
#         fields = ('title', 'content', 'price', 'rubric')
#         labels = {'title': 'Название товара'}


"""
    Объявление в форме полей, не существующих в связанной модели
    Листинг 13.5
"""

from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Пароль (повторнорно)')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
