from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response


class MarketViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny, )

    @swagger_auto_schema(
        operation_description="서버 운용 상태를 체크합니다.",
        responses={
            status.HTTP_200_OK: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'it_works': openapi.Schema(
                        type=[openapi.TYPE_BOOLEAN]
                    ),
                }
            )
        }
    )
    @action()
    def login(self):
        pass

    @action()
    def logout(self):
        pass
