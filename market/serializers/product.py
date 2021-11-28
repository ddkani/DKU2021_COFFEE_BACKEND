from rest_framework.fields import CharField, IntegerField
from rest_framework.serializers import ModelSerializer


# 기본 제품 정보
from market.models import UserProductNotify
from market.models.products import Product


class ProductModelSerializer(ModelSerializer):
    id = IntegerField()
    name = CharField()
    display_image = CharField()

    def to_representation(self, instance: Product):
        result: dict = super().to_representation(instance)

        user = self.context['request'].user
        result['user_notification_id'] = None

        if user.id:
            queryset = UserProductNotify.objects.filter(
                user_id=user.id, product_id=instance.id
            )
            try:
                result['user_notification_id'] = queryset.get().id
            except UserProductNotify.DoesNotExist:
                pass

        return result

    class Meta:
        model = Product
        fields = ('id', 'name', 'display_image')


# 제품 전체 정보 (쇼핑몰 정보 제공)
# Naming - 동일한 ProductModel 에 대해서 제공하는 데이터가 변경된 것이므로 "Detail"
# 명칭은 "Model" 뒤에 입력한다.
class ProductModelDetailSerializer(ProductModelSerializer):
    def to_representation(self, instance: Product):
        result: dict = super().to_representation(instance)
        result['mall_products'] = instance.extended_info.extended_mall_infos
        return result

    class Meta:
        model = Product
        fields = ('id', 'name', 'display_image')
