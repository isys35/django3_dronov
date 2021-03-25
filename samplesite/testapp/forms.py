"""
Листинг 20.2 Форма с полем для выгрузки файла
"""

from django import forms
from django.core import validators

from .models import Img


class ImgForm(forms.ModelForm):
    img = forms.ImageField(label='Изображение',
                           validators=[validators.FileExtensionValidator(allowed_extensions=('gif', 'jpg', 'png'))],
                           error_messages={
                               'invalid_extension': 'Этот формат не поддерживается'
                           })
    desc = forms.CharField(label='Описание', widget=forms.widgets.Textarea())

    class Meta:
        model = Img
        fields = '__all__'
