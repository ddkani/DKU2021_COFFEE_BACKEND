from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response


class KeywordViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, )

    @action()
    def add_keyword(self):
        pass

    @action()
    def delete_keyword(self):
        pass

    @action()
    def user_keyword(self):
        pass

