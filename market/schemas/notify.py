from typing import List

from drf_yasg import openapi
from drf_yasg.openapi import Schema, Parameter

from utils.schema_utils import build_list_object_schema


SET_NOTIFY_PRODUCT_REQUEST_BODY = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'product_id': openapi.Schema(type=openapi.TYPE_NUMBER)
    }
)

READ_NOTIFY_PRODUCT_REQUEST_BODY = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'notification_id': openapi.Schema(type=openapi.TYPE_NUMBER)
    }
)

GENERIC_RESULT_RESPONSE_BODY = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'result': openapi.Schema(type=openapi.TYPE_BOOLEAN)
    }
)

# 특정 쇼핑몰을 말해주어야 하는데 ->
GET_NOTIFY_PRODUCT_RESPONSE_BODY = build_list_object_schema(
    openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'notification_id': openapi.Schema(type=openapi.TYPE_NUMBER, description='알림 고유아이디, 알림 읽음처리 시 사용'),
            'product_id': openapi.Schema(type=openapi.TYPE_NUMBER, description='알림이 발생한 상품의 고유아이디'),
            'mall_info': openapi.Schema(
                type=openapi.TYPE_STRING,
                description='해당 고유 상품에서의 알림이 발생한 쇼핑몰 이름 (naver_shopping_products, auction_products) 등 위 API 참조 소스'
            )
        }
    )
)


