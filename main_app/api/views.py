from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from api.models import Answer, Question
from api.serializers import (
    AnswerSerializer,
    QuestionSerializer,
)
from django.shortcuts import get_object_or_404


class QuestionViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Question.objects.prefetch_related('answers')
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class AnswerViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            user_id=self.request.user,
            question_id=get_object_or_404(
                Question,
                pk=self.kwargs['post_id']
            )
        )
