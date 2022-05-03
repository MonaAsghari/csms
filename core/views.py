from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.cdr_method import CDR
from utils.rate_method import Rate
from .serializers import ChargingProcessSerializer


@method_decorator(name='post', decorator=swagger_auto_schema(
    operation_id='charging process rating',
    request_body=ChargingProcessSerializer,
))
class ChargingProcessRating(APIView, CDR, Rate):
    """
        Class for calculating the price of the car charging process
    """
    def post(self, request):
        serializer = ChargingProcessSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cdr = serializer.validated_data["cdr"]
        rate = serializer.validated_data["rate"]

        cdr_component = self.cdr(
            cdr['meterStart'],
            cdr['timestampStart'],
            cdr['meterStop'],
            cdr['timestampStop'])

        result = self.rate(
            rate['energy'],
            rate['time'],
            rate['transaction'],
            cdr_component)

        return Response(result, status=status.HTTP_200_OK)
