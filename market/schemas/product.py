from typing import List

from drf_yasg import openapi
from drf_yasg.openapi import Schema, Parameter

from market.models import ProductMallExtension
from utils.schema_utils import build_list_object_schema


SEARCH_PRODUCT_REQUEST_PARAMETERS: List[Parameter] = [
    openapi.Parameter(
        name='keyword', type=openapi.TYPE_STRING, in_=openapi.IN_QUERY,  required=True
    ),
    openapi.Parameter(
        name='page', type=openapi.TYPE_NUMBER, in_=openapi.IN_QUERY,  required=False
    )
]


_product_properties = {
    'id': openapi.Schema(type=openapi.TYPE_NUMBER),
    'name': openapi.Schema(type=openapi.TYPE_STRING),
    'display_image': openapi.Schema(type=openapi.TYPE_STRING)
}


SEARCH_PRODUCT_RESPONSE_SCHEMA: Schema = build_list_object_schema(
    openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties=_product_properties
    )
)


PRODUCT_REQUEST_PARAMETERS: List[Parameter] = [
    openapi.Parameter(
        name="product_id", type=openapi.TYPE_NUMBER, in_=openapi.IN_PATH, required=True,
        description="상품의 고유 id입니다."
    )
]


# build extended mall information
_mall_product_properties = {}
for field_name in ProductMallExtension.EXTENDED_RELATED_FIELD_NAMES:
    _mall_product_properties.setdefault(
        field_name.replace('_products', ''), build_list_object_schema(
            openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    **_product_properties,
                    'representative_id': openapi.Schema(type=openapi.TYPE_STRING),
                    'url': openapi.Schema(type=openapi.TYPE_STRING)
                }
            )
        )
    )


PRODUCT_RESPONSE_SCHEMA: Schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        **_product_properties,
        'mall_products': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties=_mall_product_properties
        )
    }
)


