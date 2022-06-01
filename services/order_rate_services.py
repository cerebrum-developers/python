import json
from rest_framework import status
from rest_framework.response import Response

import datetime
from datetime import datetime, date

from django.core.exceptions import ValidationError

# from .order_base_services import OrderBaseService
from orders.serializers.order_serializer import OrderRateLookupSerializer
from orders.models.order_rate_lookup import OrderRateLookUp

from utils.messages.common_messages import * 
from utils.custom_pagination import CustomPagination
from utils import CustomPagination

class OrderRateServices():

	def __init__(self):
		pass

	def get_order_rate_lookup(self, request, format=None):
		"""
		List all order rates
		"""

		order_rate_lookup = OrderRateLookUp.objects.all()

		serializer = OrderRateLookupSerializer(order_rate_lookup, many=True)

		return ({"data": serializer.data,"code": status.HTTP_200_OK, 'message': OK})
