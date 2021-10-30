from typing import List

from drf_yasg import openapi
from drf_yasg.openapi import Schema, Parameter

from market.models import ProductMallExtension
from utils.schema_utils import build_list_object_schema

_category_properties = {
    'name': openapi.Schema(type=openapi.TYPE_STRING),
    'code': openapi.Schema(type=openapi.TYPE_STRING)
}


GET_CATEGORY_RESPONSE_SCHEMA: Schema = build_list_object_schema(
    openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            **_category_properties,
            'sub_categories': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(type=openapi.TYPE_OBJECT, properties=_category_properties)
            )
        }
    )
)
