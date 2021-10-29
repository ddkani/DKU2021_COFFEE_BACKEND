from drf_yasg.utils import swagger_auto_schema
from requests import Request
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from market.schemas.market import GET_CATEGORY_RESPONSE_SCHEMA, SEARCH_PRODUCT_REQUEST_PARAMETERS, \
    SEARCH_PRODUCT_RESPONSE_SCHEMA


class MarketViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny, )

    # 2 depths 까지 구성된 키워드 정보를 반환합니다.
    @swagger_auto_schema(
        operation_description="카테고리 정보를 불러옵니다.",
        responses={status.HTTP_200_OK: GET_CATEGORY_RESPONSE_SCHEMA},
        security=[]
    )
    @action(methods=['get'], detail=False, url_path='category')
    def get_category(self, request: Request, *args, **kwargs):
        # TODO: 카테고리 serializer 작성해서 내보내기
        pass

    # TODO: pagination / 상품 모델링 후 API 세부 구성
    @swagger_auto_schema(
        operation_description="입력한 키워드로 상품 리스트를 검색합니다.",
        manual_parameters=SEARCH_PRODUCT_REQUEST_PARAMETERS,
        responses={status.HTTP_200_OK: SEARCH_PRODUCT_RESPONSE_SCHEMA},
        security=[]
    )
    @action(methods=['get'], detail=False, url_path='search')
    def search_product(self, request: Request, *args, **kwargs):
        pass
