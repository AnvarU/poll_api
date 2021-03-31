from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response
from rest_api.models import Question, QuestionSerializer, QuestionGetSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated


class QuestionApi(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = {
        'POST': QuestionSerializer,
        'PUT': QuestionSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_class.get(self.request.method)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = serializer.save()
        return Response({
            "question": self.get_serializer(question, context=self.get_serializer_context()).data,
            "message": "Question created Successfully."
        })

    @swagger_auto_schema(
        request_body=QuestionSerializer(),
        query_serializer=QuestionGetSerializer(),
        responses={
            '200': QuestionSerializer,
            '400': "Bad Request"
        },
    )
    @csrf_exempt
    def put(self, request, *args, **kwargs):
        question = Question.objects.filter(id=request.GET.get('id', None)).first()
        serializer = self.get_serializer(question, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        question = serializer.save()
        return Response({
            "question": self.get_serializer(question, context=self.get_serializer_context()).data,
            "message": "Question created Successfully."
        })

    @swagger_auto_schema(
        query_serializer=QuestionGetSerializer(),
        responses={
            '200': "Deleted Successfully.",
            '400': "Bad Request"
        },
    )
    @csrf_exempt
    def delete(self, request, *args, **kwargs):
        question = Question.objects.filter(id=request.GET.get('id', None)).first()
        question.delete()
        return Response({
            "message": "Deleted Successfully."
        })