from drf_yasg import openapi
from drf_yasg.openapi import Schema


def build_list_object_schema(schema: Schema):
    return openapi.Schema(type=openapi.TYPE_ARRAY, items=schema)

