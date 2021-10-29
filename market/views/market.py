from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from market.models import Category, Product
from market.schemas.market import SEARCH_PRODUCT_REQUEST_PARAMETERS, \
    SEARCH_PRODUCT_RESPONSE_SCHEMA, PRODUCT_REQUEST_PARAMETERS
from market.serializers.market import CategoryModelSerializer, ProductModelSerializer, ProductModelDetailSerializer


class MarketViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny, )

    # 2 depths 까지 구성된 키워드 정보를 반환합니다.
    @swagger_auto_schema(
        operation_description="카테고리 정보를 불러옵니다.",
        responses={status.HTTP_200_OK: CategoryModelSerializer(many=True)},
        security=[]
    )
    @action(methods=['get'], detail=False, url_path='category')
    def get_category(self, request: Request, *args, **kwargs):
        queryset = Category.objects.filter(parent_id__isnull=True)
        serializer = CategoryModelSerializer(queryset, many=True)
        return Response(data=serializer.data)

    @swagger_auto_schema(
        operation_description="입력한 키워드로 상품 리스트를 검색합니다.",
        manual_parameters=SEARCH_PRODUCT_REQUEST_PARAMETERS,
        responses={status.HTTP_200_OK: SEARCH_PRODUCT_RESPONSE_SCHEMA},
        security=[]
    )
    @action(methods=['get'], detail=False, url_path='search')
    def search_product(self, request: Request, *args, **kwargs):
        queryset = Product.objects.filter(name__search=request.query_params.get('keyword'))
        serializer = ProductModelSerializer(queryset, many=True)
        return Response(data=serializer.data)

    @swagger_auto_schema(
        operation_description="상품의 세부 정보를 불러옵니다.",
        manual_parameters=PRODUCT_REQUEST_PARAMETERS,
        responses={
            status.HTTP_200_OK: SEARCH_PRODUCT_RESPONSE_SCHEMA,
            status.HTTP_404_NOT_FOUND: {}
        },
        security=[]
    )
    @action(methods=['get'], detail=False, url_path=r'product/<int:product_id>/')
    def product(self, request: Request, product_id: int, *args, **kwargs):
        try:
            queryset = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductModelDetailSerializer(queryset)
        return Response(data=serializer.data)
