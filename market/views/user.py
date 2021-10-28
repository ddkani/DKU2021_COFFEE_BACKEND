from copy import copy

from django.contrib.auth.models import User
from django.db import IntegrityError
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from market.schemas.user import USER_LOGIN_REQUEST_SCHEMA, COMMON_RESPONSE_SCHEMA, USER_JOIN_REQUEST_SCHEMA


class UserViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    generic_response = {
        'result': False,
        'error_message': "",
        'token': None
    }
    def _get_generic_response(self): return copy(self.generic_response)

    @swagger_auto_schema(
        operation_description="로그인",
        request_body=USER_LOGIN_REQUEST_SCHEMA,
        responses={status.HTTP_200_OK: COMMON_RESPONSE_SCHEMA},
        security=[]
    )
    @action(methods=['post'], detail=False, url_path='login')
    def login(self, request: Request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        resp = self._get_generic_response()

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            resp['error_message'] = '일치하는 사용자가 없습니다.'
            return Response(resp)

        if not user.check_password(password):
            resp['error_message'] = '비밀번호가 다릅니다.'
            return Response(resp)

        token, created = Token.objects.get_or_create(user=user)
        resp['result'] = True
        resp['token'] = token.key
        return Response(resp)

    @swagger_auto_schema(
        operation_description="로그아웃",
        responses={status.HTTP_200_OK: COMMON_RESPONSE_SCHEMA}
    )
    @action(methods=['post'], detail=False, url_path='logout', permission_classes=(IsAuthenticated, ))
    def logout(self, request: Request, *args, **kwargs):
        token = request.auth  # type: Token
        token.delete()

        response = self._get_generic_response()
        response['result'] = True
        return Response(response)

    @swagger_auto_schema(
        operation_description="회원가입",
        request_body=USER_JOIN_REQUEST_SCHEMA,
        responses={status.HTTP_200_OK: COMMON_RESPONSE_SCHEMA},
        security=[]
    )
    @action(methods=['post'], detail=False, url_path='join')
    def join(self, request: Request, *args, **kwargs):
        resp = self._get_generic_response()

        email = request.data.get("email")
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            user = User.objects.create_user(
                email=email, username=username, password=password
            )
        except IntegrityError:
            resp['error_message'] = "중복된 이메일이 또는 닉네임이 있습니다."
            return Response(resp)

        token = Token.objects.create(user=user)
        resp['result'] = True
        resp['token'] = token.key
        return Response(resp)
