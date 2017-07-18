from django.db import models
from django.contrib.auth.models import User


CISTERN_TYPES = (('box', 'куб'),
                 ('hc', 'горизонтальный цилиндр'),
                 ('vc', 'вертикальный цилиндр'))


# БД Ключей
class KeyOwner(models.Model):
    name = models.CharField(max_length=40, default="")
    car = models.CharField(max_length=40, default="")
    keys = models.CharField(max_length=16, unique=True)
    comment = models.TextField(null=True, blank=True)


# Резервуар
class Cistern(models.Model):
    start_volume = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    max_volume = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    cistern_type = models.CharField(max_length=3, choices=CISTERN_TYPES)

    def save(self, *args, **kwargs):
        if self.start_volume > self.max_volume:
            raise ValueError('Начальное значение не может превышать максимальное')
        else:
            super(Cistern, self).save(*args, **kwargs)


# БД Отгрузок
class Database(models.Model):
    user = models.ForeignKey(KeyOwner)
    op_id = models.CharField(max_length=20)
    dosed = models.DecimalField(decimal_places=2, max_digits=15)
    date_time = models.DateTimeField()
    add = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    cistern = models.ForeignKey(Cistern, default=0, null=True)
    cistern_volume = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    delete = models.BooleanField(default=False)

    class Meta:
        ordering = ["date_time"]


class UpDosed(models.Model):
    user = models.ForeignKey(User)
    cistern = models.ForeignKey(Cistern)
    date_time = models.DateTimeField()
    volume = models.DecimalField(decimal_places=2, max_digits=15)
    comment = models.TextField(null=True, blank=True)


# Параметры соединения
class Connect(models.Model):
    port = models.CharField(max_length=20, default='0')
    speed = models.PositiveIntegerField(default=115200)
