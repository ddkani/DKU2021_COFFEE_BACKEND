from django.db import IntegrityError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from market.models import UserProductNotify, UserNotify
from market.schemas.notify import SET_NOTIFY_PRODUCT_REQUEST_BODY, GET_NOTIFY_PRODUCT_RESPONSE_BODY, \
    GENERIC_RESULT_RESPONSE_BODY, READ_NOTIFY_PRODUCT_REQUEST_BODY, GET_NOTIFY_RESPONSE_BODY
from market.serializers.notify import SetNotifyProductRequestSerializer, RemoveNotifyProductRequestSerializer, \
    UserNotifyModelSerializer, UserProductNotifySerializer


class NotifyViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, )

    # ==== 사용자가 알림을 지정하는 기준

    @swagger_auto_schema(
        operation_description="사용자가 선택한 제품으로 알림을 지정합니다.",
        request_body=SET_NOTIFY_PRODUCT_REQUEST_BODY,
        responses={
            status.HTTP_200_OK: GENERIC_RESULT_RESPONSE_BODY
        }
    )
    @action(methods=['post'], detail=False, url_path='set_product_notify')
    def set_notify_product(self, request: Request, *args, **kwargs):
        req_serializer = SetNotifyProductRequestSerializer(data=request.data)

        req_serializer.is_valid(raise_exception=True)
        req_data = req_serializer.validated_data

        try:
            UserProductNotify(
                product_id=req_data['product_id'],
                user=request.user
            ).save()
        except IntegrityError as e:
            return Response({
                'result': False, 'error_message': '이미 동일한 정보가 존재하거나, 해당 product가 존재하지 않습니다.'
            })

        return Response({
            'result': True, 'error_message': None
        })

    @swagger_auto_schema(
        operation_description="사용자가 지정한 제품의 알림을 해제합니다.",
        request_body=SET_NOTIFY_PRODUCT_REQUEST_BODY,
        responses={
            status.HTTP_200_OK: GENERIC_RESULT_RESPONSE_BODY
        }
    )
    @action(methods=['post'], detail=False, url_path='remove_product_notify')
    def remove_notify_product(self, request: Request, *args, **kwargs):
        req_serializer = RemoveNotifyProductRequestSerializer(data=request.data)

        req_serializer.is_valid(raise_exception=True)
        req_data = req_serializer.data

        try:
            affected, _ = UserProductNotify.objects.filter(
                product_id=req_data['product_id'],
                user=request.user
            ).delete()
            if affected == 0:
                raise IntegrityError()

        except IntegrityError as e:
            return Response({
                'result': False, 'error_message': '요청한 제품 알림이 사용자에 대해 존재하지 않습니다.'
            })

        return Response({
            'result': True, 'error_message': None
        })

    @swagger_auto_schema(
        operation_description='사용자가 지정한 제품 알림 리스트를 가져옵니다.',
        responses={
            status.HTTP_200_OK: GET_NOTIFY_RESPONSE_BODY
        }
    )
    @action(methods=['get'], detail=False, url_path='get_product_notify')
    def get_notify_product(self, request: Request, *args, **kwargs):
        return UserProductNotifySerializer(
            data=UserProductNotify.objects.filter(user=request.user),
            many=True
        )

    # ==== 사용자에게 제공되는 알림 기준

    @swagger_auto_schema(
        operation_description="사용자에게 지정되어있는 알림이 있는지 확인합니다. 더이상 받지 않을 경우, 읽음 처리 API를 호출해야 합니다.",
        responses={
            status.HTTP_200_OK: GET_NOTIFY_PRODUCT_RESPONSE_BODY
        }
    )
    @action(methods=['get'], detail=False, url_path="get_notify")
    def get_notify(self, request: Request, *args, **kwargsj):
        return UserNotifyModelSerializer(
            data=UserNotify.objects.filter(
                user=request.user, is_read=False
            ),
            many=True
        )

    @swagger_auto_schema(
        operation_description="사용자에게 제공되는 알림을 읽음 처리합니다.",
        request_body=READ_NOTIFY_PRODUCT_REQUEST_BODY,
        responses={
            status.HTTP_200_OK: GENERIC_RESULT_RESPONSE_BODY
        }
    )
    @action(methods=['post'], detail=False, url_path="read_notify")
    def read_notify(self, request: Request, *args, **kwargs):
        UserNotify.objects.filter(
            user=request.user,
        ).update(is_read=True)
        return Response({'result': True, 'error_message': None})
