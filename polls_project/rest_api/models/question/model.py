from django.db import models

from django.utils.translation import gettext_lazy as _

from rest_api.models.poll import Poll


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    question_type = models.IntegerField(choices=(
        (0, _("Text answer")), (1, _("Text answer with one choice")),
        (2, _("Text answer with multiple choice"))))

    class Meta:
        verbose_name_plural = 'Вопросы'
        verbose_name = 'Вопрос'


class Choice(models.Model):
    text = models.CharField(max_length=256)
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Варианты'
        verbose_name = 'Вариант'