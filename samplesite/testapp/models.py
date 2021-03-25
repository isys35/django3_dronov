from django.db import models
from django.contrib.auth.models import User


class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Spare(models.Model):
    name = models.CharField(max_length=30)


class Machine(models.Model):
    name = models.CharField(max_length=30)
    spares = models.ManyToManyField(Spare)


""""
Листинг 16.1. Создание связи "многие со многими" с дополнительными данными
"""

# class Machine(models.Model):
#     name = models.CharField(max_length=30)
#     spares = models.ManyToManyField(Spare, through='Kit', through_fields=('machine', 'spare'))
#
#
# class Kit(models.Model):
#     machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
#     spare = models.ForeignKey(Spare, on_delete=models.CASCADE)
#     count = models.IntegerField()

""""
Листинг 16.2. Пример использования полиморфной связи
"""

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Note(models.Model):
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_objects = GenericForeignKey(ct_field='content_type', fk_field='object_id')


""""
Листинг 16.3. Пример прямого(многотабличного) наследования моделей
"""

# class Message(models.Model):
#     content = models.TextField()
#
#
# class PrivateMessage(Message):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


""""
Листинг 16.4. Переопределение и удаление полей, объявленных в базовой
абстрактной модели
"""


class Message(models.Model):
    content = models.TextField()
    name = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        abstract = True


class PrivateMessage(Message):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Переопределяем поле name
    name = models.CharField(max_length=40)
    # Удаляем поле email
    email = None

""""
Листинг 20.1. Модель с полем для хранения выгруженного файла
"""

from datetime import datetime
from os.path import splitext


def get_timestamp_path(instance, filename):
    return "%s%s" % (datetime.now().timestamp(), splitext(filename)[1])


class Img(models.Model):
    img = models.ImageField(verbose_name='Изображения', upload_to=get_timestamp_path)
    desc = models.TextField(verbose_name='Описание')

    # def delete(self, *args, **kwargs):
    #     self.img.delete(save=False)
    #     super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
