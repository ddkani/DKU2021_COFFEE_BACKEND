from django.contrib.auth.models import User
from django.db import models

from market.models import Product


class UserNotify(models.Model):
    """
    사용자에게 전달되는 알림입니다.
    """

    id = models.BigAutoField(primary_key=True)

    product = models.ForeignKey(Product, null=False, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING, related_name='notifications')

    # TODO: 원래대로였으면 데이터 가져올때 enum 필드 할당해서 과져옴
    mall_name = models.CharField(null=False, max_length=32)
    created_at = models.DateTimeField(null=True, auto_now_add=True)

    is_read = models.BooleanField(null=False, default=False)
    is_read_at = models.DateTimeField(null=True)

    class Meta:
        verbose_name = "UserNotify"
        unique_together = [
            ['product', 'user']
        ]


class UserProductNotify(models.Model):
    """
    사용자가 알림을 받기 위해 설정하는 제품입니다.
    """

    id = models.BigAutoField(primary_key=True)

    product = models.ForeignKey(Product, null=False, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(Product, null=False, on_delete=models.DO_NOTHING, related_name='product_notifications')
    created_at = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        verbose_name = "UserProductNotify"
        unique_together = [
            ['product', 'user']
        ]
