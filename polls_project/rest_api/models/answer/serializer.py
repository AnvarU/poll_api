from rest_framework import serializers
from .model import Answer
from rest_api.models.user.model import AnonymousUser
from rest_api.models.question.model import Question, Choice
from rest_api.models.question.serializer import ChoiceShortSerializer


class AnswerShortSerializer(serializers.ModelSerializer):
    # choice = ChoiceShortSerializer(many=True, required=False)

    class Meta:
        model = Answer
        fields = ('question', 'text', 'choice')


class AnswerGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    answers = AnswerShortSerializer(many=True)

    class Meta:
        model = Answer
        fields = ('user', 'answers')

    def save(self, validated_data):
        custom_id = validated_data.get('user')
        user = AnonymousUser.objects.filter(custom_id=custom_id).first()
        answers = validated_data.get('answers')
        for answer in answers:
            question_id = answer.get('question', None)
            text = answer.get('text', '')
            choices = answer.get('choice', [])
            question = Question.objects.filter(id=question_id).first()
            if not question:
                raise serializers.ValidationError({'message': 'Question does not exist.'})
            if not question.poll.is_active:
                raise serializers.ValidationError({'message': 'Poll is not active.'})
            if question.question_type == 0:
                answer = Answer(user=user, question=question, text=text)
                answer.save()
                user.answers.set([answer])
                return answer
            elif question.question_type == 1:
                if len(choices) == 1:
                    choice_id = choices[0]
                    if not Choice.objects.filter(id=choice_id, question=question_id).first():
                        raise serializers.ValidationError({'message': 'Choice does not exist.'})
                    else:
                        choice = Choice.objects.filter(id=choice_id, question=question_id).first()
                        answer = Answer(user=user, question=question, text=text)
                        answer.save()
                        answer.choice.set([choice])
                        user.answers.set([answer])
                        return answer
                else:
                    raise serializers.ValidationError({'message': 'You must choose one choice.'})
            elif question.question_type == 2:
                answer = Answer(user=user, question=question, text=text)
                answer.save()
                if len(choices) > 1:
                    choice_list = []
                    for choice_id in choices:
                        if not Choice.objects.filter(id=choice_id, question=question_id).first():
                            raise serializers.ValidationError({'message': 'Choice does not exist.'})
                        else:
                            choice_list.append(Choice.objects.filter(id=choice_id, question=question_id).first())
                        answer.choice.set(choices)
                        user.answers.set([answer])
                        return answer
                else:
                    raise serializers.ValidationError({'message': 'You must choose more than one choice.'})
            else:
                raise serializers.ValidationError({'message': 'Invalid question type.'})