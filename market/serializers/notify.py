from rest_framework.fields import CharField, IntegerField
from rest_framework.serializers import Serializer, ModelSerializer

from market.models import UserNotify


class SetNotifyProductRequestSerializer(Serializer):
    product_id = IntegerField(required=True)


class RemoveNotifyProductRequestSerializer(Serializer):
    product_id = IntegerField(required=True)


class UserNotifyModelSerializer(ModelSerializer):
    id = IntegerField()
    product_id = IntegerField()
    mall_name = CharField()

    class Meta:
        model = UserNotify
        fields = ('id', 'product_id', 'mall_name')
