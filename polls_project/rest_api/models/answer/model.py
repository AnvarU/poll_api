from django.db import models

from rest_api.models import Question, Choice


class Answer(models.Model):
    user = models.ForeignKey('rest_api.AnonymousUser', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ManyToManyField(Choice)
    text = models.TextField(max_length=4096, null=True)