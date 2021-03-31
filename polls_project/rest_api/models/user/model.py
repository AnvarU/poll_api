from django.db import models


class AnonymousUser(models.Model):
    custom_id = models.IntegerField(verbose_name='ID')
    answers = models.ManyToManyField('rest_api.Answer')