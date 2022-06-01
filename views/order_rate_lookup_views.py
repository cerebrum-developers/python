from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from orders.services.order_rate_services import OrderRateServices

orderRateService = OrderRateServices()

class OrderRateLookupView(APIView):

	def post(self, request, format=None):
		"""
		Return rates of order.
		"""
		result = orderRateService.get_order_rate_lookup(request, format=None)
		return Response(result, status=status.HTTP_200_OK)

