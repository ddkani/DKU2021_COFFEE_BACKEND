from typing import List

from drf_yasg import openapi
from drf_yasg.openapi import Schema, Parameter

from utils.schema_utils import build_list_object_schema

_category = {
    'name': openapi.Schema(type=openapi.TYPE_STRING),
    'code': openapi.Schema(type=openapi.TYPE_STRING)
}


GET_CATEGORY_RESPONSE_SCHEMA: Schema = build_list_object_schema(
    openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            **_category,
            'sub_categories': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(type=openapi.TYPE_OBJECT, properties=_category)
            )
        }
    )
)


SEARCH_PRODUCT_REQUEST_PARAMETERS: List[Parameter] = [
    openapi.Parameter(
        name='keyword', type=openapi.TYPE_STRING, in_=openapi.IN_QUERY,  required=True
    ),
    openapi.Parameter(
        name='page', type=openapi.TYPE_NUMBER, in_=openapi.IN_QUERY,  required=False
    )
]


SEARCH_PRODUCT_RESPONSE_SCHEMA: Schema = build_list_object_schema(
    openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={

        }
    )
)
