from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class AdvUser(AbstractUser):
    is_activate = models.BooleanField(default=True, db_index=True,
                                verbose_name="Прошел активацию?")
    send_message = models.BooleanField(default=True,
                                verbose_name='Слать оповещение о новых комментариях?')

    class Meta(AbstractUser.Meta):
        pass