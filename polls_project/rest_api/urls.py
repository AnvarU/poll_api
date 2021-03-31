from django.urls import path
from rest_api.api import PollApi, PollsApi, QuestionApi, AnswerApi, AnonymousUserApi

urlpatterns = [
      path('poll', PollApi.as_view()),
      path('polls', PollsApi.as_view()),
      path('question', QuestionApi.as_view()),
      path('answer', AnswerApi.as_view()),
      path('user', AnonymousUserApi.as_view())
]
