from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .models import Poll, Question, Answer
from .serializers import PollSerializer, QuestionSerializer, AnswerSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


@api_view(['GET'])
def user_polls(request, user_id):
    # Найти все ответы пользователя
    answers = Answer.objects.filter(
        user_id=user_id).select_related('question__poll')

    # Собрать все уникальные опросы
    poll_ids = {answer.question.poll_id for answer in answers}
    polls = Poll.objects.filter(
        id__in=poll_ids).prefetch_related('questions__answers')

    # Сериализовать данные
    serializer = PollSerializer(polls, many=True)
    return Response(serializer.data)
