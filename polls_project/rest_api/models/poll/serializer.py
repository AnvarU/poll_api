from rest_framework import serializers
from .model import Poll
from rest_api.models.question import QuestionSerializer


class PollSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(required=True)

    class Meta:
        model = Poll
        fields = ('id', 'title', 'start_datetime', 'end_datetime', 'description', 'is_active')


class PollGetSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=100, default='', allow_blank=False)

    class Meta:
        model = Poll
        fields = ('id',)


class PollShortSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        fields = ('id', 'title', 'start_datetime', 'end_datetime', 'description', 'questions')