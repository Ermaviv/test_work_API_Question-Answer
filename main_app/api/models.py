from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(
        max_length=30,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )


class Answer(models.Model):
    question_id = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        auto_created=True,
        related_name='answers',
    )

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=30)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
