from rest_framework import serializers


class OilAccumulationSerializer(serializers.Serializer):
    date = serializers.DateField()
    oil_accumulated = serializers.FloatField()
    water_accumulated = serializers.FloatField()
    water_accumulated_upload = serializers.FloatField()


class OilStockSerializer(serializers.Serializer):
    date = serializers.DateField()
    oil_stock_value = serializers.FloatField()


class OilDebitSerializer(serializers.Serializer):
    date = serializers.DateField()
    oil_debit = serializers.FloatField()
    water_debit = serializers.FloatField()
    liquid_debit = serializers.FloatField()
    water_throttle_response = serializers.FloatField()
