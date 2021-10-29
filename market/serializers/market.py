from rest_framework.fields import CharField, IntegerField
from rest_framework.serializers import ModelSerializer

from market.models import Category, Product


class SubCategoryModelSerializer(ModelSerializer):
    code = CharField()
    name = CharField()

    class Meta:
        model = Category
        fields = ('code', 'name')


class CategoryModelSerializer(ModelSerializer):
    code = CharField()
    name = CharField()
    sub_categories = SubCategoryModelSerializer(many=True)

    class Meta:
        model = Category
        fields = ('code', 'name', 'sub_categories')


# 기본 제품 정보
class ProductModelSerializer(ModelSerializer):
    id = IntegerField()
    name = CharField()
    display_image = CharField()

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
