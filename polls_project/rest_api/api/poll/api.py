from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response
from rest_api.models import Poll, PollSerializer, PollGetSerializer, PollShortSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated


class PollApi(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = {
        'POST': PollSerializer,
        'PUT': PollSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_class.get(self.request.method)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        poll = serializer.save()
        return Response({
            "poll": self.get_serializer(poll, context=self.get_serializer_context()).data,
            "message": "Poll created Successfully."
        })

    @swagger_auto_schema(
        request_body=PollSerializer(),
        query_serializer=PollGetSerializer(),
        responses={
            '200': PollSerializer,
            '400': "Bad Request"
        },
    )
    @csrf_exempt
    def put(self, request, *args, **kwargs):
        poll = Poll.objects.filter(id=request.GET.get('id', None)).first()
        serializer = self.get_serializer(poll, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        poll = serializer.save()
        return Response({
            "poll": self.get_serializer(poll, context=self.get_serializer_context()).data,
            "message": "Poll created Successfully."
        })

    @swagger_auto_schema(
        query_serializer=PollGetSerializer(),
        responses={
            '200': "Deleted Successfully.",
            '400': "Bad Request"
        },
    )
    @csrf_exempt
    def delete(self, request, *args, **kwargs):
        poll = Poll.objects.filter(id=request.GET.get('id', None)).first()
        poll.delete()
        return Response({
            "message": "Deleted Successfully."
        })


class PollsApi(generics.GenericAPIView):
    serializer_class = {
        'GET': PollShortSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_class.get(self.request.method)

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        polls = Poll.objects.filter(is_active=True).all()
        polls = self.get_serializer(polls, context=self.get_serializer_context(), many=True).data
        return Response({
            "polls": polls,
            "message": "Polls retrieved Successfully.",
        })