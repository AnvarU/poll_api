from rest_framework import serializers
from .model import AnonymousUser
from rest_api.models.answer import Answer
from rest_api.models.question import ChoiceSerializer


class AnswerShortSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer(many=True)

    class Meta:
        model = Answer
        fields = ('question', 'text', 'choice')


class AnonymousUserSerializer(serializers.ModelSerializer):
    answers = AnswerShortSerializer(many=True)

    class Meta:
        model = AnonymousUser
        fields = ('id', 'custom_id', 'answers')


class AnonymousUserGetSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=100, default='', allow_blank=False)

    class Meta:
        model = AnonymousUser
        fields = ('id',)