from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from api.models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
    text = serializers.CharField(
        required=True,
        validators=[
            UniqueValidator(queryset=Answer.objects.all())
        ],
    )
    user_id = serializers.CharField(
        read_only=True
    )

    class Meta:
        model = Answer
        fields = ['id', 'text', 'user_id']


class QuestionSerializer(serializers.ModelSerializer):
    text = serializers.CharField(
        required=True,
        validators=[
            UniqueValidator(queryset=Question.objects.all())
        ]
    )
    answers = AnswerSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ('id', 'text', 'answers')


'''
# отдельно вопросы без ответов я пока не знаю, как реализовать
# траблы во вьюхе
class QuestionIdSerializer(QuestionSerializer):
    answers = AnswerSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ('id', 'text', 'answers')
'''
