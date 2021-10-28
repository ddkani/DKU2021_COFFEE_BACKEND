from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response


class UserViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny, )

    # 로그인
    @action(methods=['post'], detail=False, url_path='login')
    def login(self, request: Request, *args, **kwargs):
        pass

    # 로그아웃
    @action(methods=['post'], detail=False, url_path='logout')
    def logout(self, request: Request, *args, **kwargs):
        pass

    # 사용자 정보 열람
    @action(methods=['get'], detail=False, url_path='info')
    def info(self, request: Request, *args, **kwargs):
        pass
