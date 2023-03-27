from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView

from authentication import models as m
from authentication.api import serializers as s


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    permission_classes = [IsAuthenticated]
    serializer_class = s.UserSerializer
    queryset = m.User.objects.all().order_by('pk')



