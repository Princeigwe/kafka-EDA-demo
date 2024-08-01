from rest_framework import serializers


class CartSerializer(serializers.Serializer):
  quantity = serializers.IntegerField()