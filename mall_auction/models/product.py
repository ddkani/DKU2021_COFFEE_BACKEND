from typing import Optional
from django.db import models

from market.models.products import Product as MallProduct


class Product(models.Model):
    NAVER_CATALOG_URL = "https://shopping.naver.com/catalog/"

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    display_image = models.CharField(null=True, max_length=256)
    price = models.PositiveIntegerField(null=False, default=0)

    product_id = models.PositiveIntegerField()
    original_product_extension = models.ForeignKey(
        'market.ProductMallExtension', null=True, on_delete=models.DO_NOTHING,
        related_name='auction_products'
    )

    @property
    # Optional - 파싱 상태에 따라 정보가 존재하지 않을 수 있음.
    def original_product(self) -> Optional[MallProduct]:
        return None if self.original_product_extension is None else \
            self.original_product_extension.product

    # 해당 상품의 정보가 존재하는 URL
    @property
    def url(self):
        return f'{self.NAVER_CATALOG_URL}{self.product_id}'

    # 해당 상품의 대상 서비스에서 존재하는 primary_key 정보
    @property
    def representative_id(self):
        return str(self.product_id)
