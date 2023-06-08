from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login
from users.serializers import UserSignUpSerializer


class UserSignUpViewSet(viewsets.ViewSet):
    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
    
    def create(self, request):
        serializer = UserSignUpSerializer(data=request.data, context={ 'request': request })
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response(user, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_202_ACCEPTED)