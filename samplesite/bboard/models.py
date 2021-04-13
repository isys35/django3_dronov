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
    order = models.SmallIntegerField(default=0, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['order', 'name']


"""
Листинг 16.5. Пример прокси-модели
"""


class RevRubric(Rubric):
    class Meta:
        proxy = True
        ordering = ['-name']


"""
Листинг 16.6. Пример объявления собственного диспетчера записей
"""


class RubricManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('order', 'name')

    def order_by_bb_count(self):
        return super().get_queryset().annotate(cnt=models.Count('bb')).order_by('-cnt')


"""
Листинг 16.7. Пример диспетчера обратной связи
"""


class BbManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('price')


"""
Листинг 16.7. Пример собственного набора записей
"""


class RubricQuerySet(models.QuerySet):
    def order_by_bb_count(self):
        return self.annotate(cnt=models.Count('bb')).order_by('-cnt')


"""
Листинг 16.9. Пример диспетчера записей, обслуживающего набор записей из листинга 16.8 
"""

# class RubricManager(models.Manager):
#     def get_queryset(self):
#         return RubricQuerySet(self.model, using=self._db)
#
#     def order_by_bb_count(self):
#         return self.get_queryset().order_by_bb_count()

from django.db.models.signals import post_save


def post_save_dispatcher(sender, **kwargs):
    if kwargs['created']:
        print('Объявление в рубрике "%s" создано' % kwargs['instance'].rubric.name)


post_save.connect(post_save_dispatcher, sender=Bb)

from django.dispatch import Signal

add_bb = Signal(providing_args=['instance', 'rubric'])


def add_bb_dispatcher(sender, **kwargs):
    print('Объявление в рубрике "%s" с ценой %.2f создано' % (kwargs['rubric'].name, kwargs['instance'].price))


add_bb.connect(add_bb_dispatcher)
