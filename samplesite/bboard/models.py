from django.db import models
from django.core.exceptions import ValidationError


def validate_even(val):
    if val % 2 != 0:
        raise ValidationError("Число %(value)s нечётное",
                              code='odd', params={'value': val})


class MinMaxValueValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, val):
        if val < self.min_value or val > self.max_value:
            raise ValidationError("Введённое число должно находится в диапозоне от %(min)s до %(max)s",
                                  code='out_of_range', params={'min': self.min_value, 'max': self.max_value})


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    # price = models.FloatField(null=True, blank=True, verbose_name='Цена', validators=[validate_even])
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика',
                               related_name='entries', related_query_name='entry')

    def clean(self):
        errors = {}
        if not self.content:
            errors['content'] = ValidationError('Укажите описание продаваемого товара')

        if self.price and self.price < 0:
            errors['price'] = ValidationError("Укажите неотрицательное значение цены")

        if errors:
            raise ValidationError(errors)

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
