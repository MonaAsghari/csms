from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class ChargingProcessCDRSerializer(serializers.Serializer):
    """
        Serializer for CDR (charge detail record) component
    """
    meterStart = serializers.IntegerField(required=True, help_text='start meter value of the electricity')
    timestampStart = serializers.DateTimeField(
        format='iso-8601',
        required=True,
        label='ISO 8601 time format: 2021-04-05T10:04:00Z',
        help_text='charging process timestamp start')
    meterStop = serializers.IntegerField(required=True, help_text='stop meter value of the electricity')
    timestampStop = serializers.DateTimeField(
        format='iso-8601',
        required=True,
        label='ISO 8601 time format: 2021-04-05T10:04:00Z',
        help_text='charging process timestamp stop')

    def validate(self, data):
        if 0 < data['meterStop'] < data['meterStart']:
            raise serializers.ValidationError("The meterStop should be greater than meterStart")

        if data['meterStart'] <= 0 or data['meterStop'] <= 0:
            raise serializers.ValidationError("The meter value should be greater than Zero")

        if data['timestampStop'] < data['timestampStart']:
            raise serializers.ValidationError("The timestampStop should be greater than timestampStart")

        return data


class ChargingProcessRateSerializer(serializers.Serializer):
    """
        Serializer for rate component
    """
    energy = serializers.FloatField(required=True, help_text="energy per kWh")
    time = serializers.FloatField(required=True, help_text='time per hour')
    transaction = serializers.FloatField(required=True, help_text='service fee')


class ChargingProcessSerializer(serializers.Serializer):
    """
        Serializer for Charging Process Rating
    """
    cdr = ChargingProcessCDRSerializer(many=False)
    rate = ChargingProcessRateSerializer(many=False)
