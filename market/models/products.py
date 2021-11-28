from typing import List

from django.db import models


# 카테고리 정보 (1 ~ 2 depths)
from django.db.models import OneToOneField


# 통합 제품 정보
class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    # TODO: 전체 이미지 리스트에서 하나를 가져올 수 도 있을듯
    display_image = models.CharField(null=True, max_length=256)

    class Meta:
        verbose_name = "Product"
        # Text field index
        indexes = [
            models.Index(fields=['name']),
        ]


# 제품에 연결된 각 쇼핑몰의 정보
# 이곳에서는 ForeignKey 정보들을 저장하고 있으며, 공통으로 연결된 외부 상품들을 지정합니다.
class ProductMallExtension(models.Model):
    # !! 필드 입력시에는 뒤의 _products 접미사가 해제됩니다.
    EXTENDED_RELATED_FIELD_NAMES = [
        'naver_shopping_products', 'auction_products'
    ]
    EXTENDED_EXPORT_FIELD_NAMES = [
        'id', 'name', 'display_image', 'representative_id', 'url', 'price'
    ]

    id = models.BigAutoField(primary_key=True)
    product = OneToOneField(Product, on_delete=models.CASCADE, related_name='extended_info')

    @property
    def extended_mall_infos(self) -> dict:
        results = {}
        for field_name in self.EXTENDED_RELATED_FIELD_NAMES:
            mall_results = []

            # TODO: 해당 오브젝트 클랫 정보 - 부모 클래스 사용?
            for product_object in getattr(self, field_name).all():
                object_result = {}

                for _export_field_name in self.EXTENDED_EXPORT_FIELD_NAMES:
                    object_result.setdefault(
                        _export_field_name, getattr(product_object, _export_field_name)
                    )
                mall_results.append(object_result)

            results.setdefault(field_name.replace('_products', ''), mall_results)
        return results


