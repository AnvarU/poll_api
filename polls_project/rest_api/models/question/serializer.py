from rest_framework import serializers
from .model import Question, Choice
from rest_api.models.poll import Poll


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('text',)


class ChoiceShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id',)


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ('text', 'question_type', 'poll', 'choices')


class QuestionGetSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=100, default='', allow_blank=False)

    class Meta:
        model = Question
        fields = ('id',)