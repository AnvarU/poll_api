from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response
from rest_api.models import Answer, AnswerSerializer, AnonymousUser, AnswerGetSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated


class AnswerApi(generics.GenericAPIView):
    serializer_class = {
        'POST': AnswerSerializer
    }

    def get_serializer_class(self):
        return self.serializer_class.get(self.request.method)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        user = AnonymousUser.objects.filter(custom_id=request.data.get('user', None)).first()
        if not user:
            user = AnonymousUser(custom_id=request.data.get('user', None))
            user.save()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        answer = serializer.save(request.data)
        return Response({
            "answer": AnswerGetSerializer(answer, context=self.get_serializer_context()).data,
            "message": "Question created Successfully."
        })