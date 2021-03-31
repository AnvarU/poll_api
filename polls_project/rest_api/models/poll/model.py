from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    start_datetime = models.DateTimeField(db_index=True, verbose_name='Дата начала')
    end_datetime = models.DateTimeField(db_index=True, verbose_name='Дата окончания')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    is_active = models.BooleanField(db_index=True, verbose_name='Статус', default=False)

    class Meta:
        verbose_name_plural = 'Опросы'
        verbose_name = 'Опрос'
        ordering = ['-start_datetime']