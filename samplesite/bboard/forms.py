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
