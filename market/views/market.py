from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from market.models import Category
from market.serializers.market import CategoryModelSerializer


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
