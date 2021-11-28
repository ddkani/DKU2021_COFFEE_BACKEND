from rest_framework.fields import CharField, IntegerField, DateTimeField
from rest_framework.serializers import Serializer, ModelSerializer

from market.models import UserNotify, UserProductNotify


class SetNotifyProductRequestSerializer(Serializer):
    product_id = IntegerField(required=True)


class RemoveNotifyProductRequestSerializer(Serializer):
    product_id = IntegerField(required=True)


class UserProductNotifySerializer(ModelSerializer):
    """
    사용자가 지정한 알림 옵션
    """
    id = IntegerField()
    product_id = IntegerField()
    created_at = DateTimeField()

    class Meta:
        model = UserProductNotify
        fields = ('id', 'product_id', 'created_at')


class UserNotifyModelSerializer(ModelSerializer):
    """
    사용자에게 제공되는 알림 정보
    """
    id = IntegerField()
    product_id = IntegerField()
    mall_name = CharField()
    created_at = DateTimeField()

    class Meta:
        model = UserNotify
        fields = ('id', 'product_id', 'mall_name', 'created_at')
