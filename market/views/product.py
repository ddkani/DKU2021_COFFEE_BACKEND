from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from market.models.products import Product
from market.schemas.product import SEARCH_PRODUCT_REQUEST_PARAMETERS, PRODUCT_LIST_RESPONSE_SCHEMA, \
    PRODUCT_REQUEST_PARAMETERS, PRODUCT_DETAIL_RESPONSE_SCHEMA, LIST_PRODUCT_REQUEST_PARAMETERS
from market.serializers.product import ProductModelSerializer, ProductModelDetailSerializer


class ProductViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    queryset = Product.objects.all()
    # serializer_class = ProductModelDetailSerializer

    def get_serializer_class(self):
        return {
            'list': ProductModelSerializer,
            'retrieve': ProductModelDetailSerializer
        }[self.action]

    # notify 등으로 받은 상품 정보
    # https://stackoverflow.com/questions/68246391/url-path-is-matching-the-wrong-view-in-drf-viewsets
    @swagger_auto_schema(
        operation_description="상품의 세부 정보를 불러옵니다.",
        manual_parameters=PRODUCT_REQUEST_PARAMETERS,
        responses={
            status.HTTP_200_OK: PRODUCT_DETAIL_RESPONSE_SCHEMA,
            status.HTTP_404_NOT_FOUND: {}
        },
        security=[]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="상품의 리스트를 불러옵니다.",
        manual_parameters=LIST_PRODUCT_REQUEST_PARAMETERS,
        responses={
            # status.HTTP_200_OK: PRODUCT_LIST_RESPONSE_SCHEMA,
            # status.HTTP_404_NOT_FOUND: {}
        },
        security=[]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="입력한 키워드로 상품 리스트를 검색합니다.",
        manual_parameters=SEARCH_PRODUCT_REQUEST_PARAMETERS,
        responses={status.HTTP_200_OK: PRODUCT_LIST_RESPONSE_SCHEMA},
        security=[]
    )
    @action(methods=['get'], detail=False, url_path='search')
    def search_product(self, request: Request, *args, **kwargs):
        queryset = Product.objects.filter(name__contains=request.query_params.get('keyword'))
        serializer = ProductModelSerializer(queryset, many=True)
        return Response(data=serializer.data)


    # https://stackoverflow.com/questions/68246391/url-path-is-matching-the-wrong-view-in-drf-viewsets
    # @swagger_auto_schema(
    #     operation_description="상품의 세부 정보를 불러옵니다.",
    #     manual_parameters=PRODUCT_REQUEST_PARAMETERS,
    #     responses={
    #         status.HTTP_200_OK: PRODUCT_RESPONSE_SCHEMA,
    #         status.HTTP_404_NOT_FOUND: {}
    #     },
    #     security=[]
    # )
    # @action(methods=['get'], detail=False, url_path=r'(?P<product_id>\w+)')
    # def product(self, request: Request, product_id: int, *args, **kwargs):
    #     try:
    #         queryset = Product.objects.get(id=product_id)
    #     except Product.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #
    #     serializer = ProductModelDetailSerializer(queryset)
    #     return Response(data=serializer.data)
