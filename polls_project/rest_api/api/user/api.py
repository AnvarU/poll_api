from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response
from rest_api.models import AnonymousUser, AnonymousUserSerializer, AnonymousUserGetSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated


class AnonymousUserApi(generics.GenericAPIView):
    serializer_class = {
        'GET': AnonymousUserSerializer
    }

    def get_serializer_class(self):
        return self.serializer_class.get(self.request.method)

    @swagger_auto_schema(
        query_serializer=AnonymousUserGetSerializer(),
        responses={
            '200': AnonymousUserSerializer,
            '400': "Bad Request"
        },
    )
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        user = AnonymousUser.objects.filter(custom_id=request.GET.get('id')).first()
        users = self.get_serializer(user, context=self.get_serializer_context()).data
        return Response({
            "users": users,
            "message": "Question created Successfully."
        })