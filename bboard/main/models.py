from django.contrib.auth.models import AbstractUser
from django.db import models


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True,
                                       db_index=True,
                                       verbose_name='ПРошёл активацию?')
    send_messages = models.BooleanField(default=True,
                                        verbose_name='Слать сообщения о новых комментариях?')


    class Meta(AbstractUser.Meta):
        pass
