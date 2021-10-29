from drf_yasg import openapi

COMMON_RESPONSE_SCHEMA = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'result': openapi.Schema(type=openapi.TYPE_BOOLEAN),
        'error_message': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
        'token': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
    }
)


USER_LOGIN_REQUEST_SCHEMA = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING),
        'password': openapi.Schema(type=openapi.TYPE_STRING),
    }
)


USER_JOIN_REQUEST_SCHEMA = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING),
        'password': openapi.Schema(type=openapi.TYPE_STRING),
        'nickname': openapi.Schema(type=openapi.TYPE_STRING),
    }
)
