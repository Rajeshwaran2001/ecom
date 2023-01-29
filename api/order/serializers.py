from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('user','product_names', 'transaction_id', 'created_at')
        # TODO: add product and quantity
