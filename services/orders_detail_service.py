import json
from rest_framework import status
from rest_framework.response import Response

from django.core.exceptions import ValidationError

from .order_base_services import OrderBaseService
from orders.serializers.order_serializer import OrderShipmentsAllListSerializer, OrderShipmentsDetailSerializer
from orders.models.order_shipments_all import OrderShipmentsAll


class OrderDetailService():
	"""
	 This api is used to get detail of the order
	"""

	def get_detail_view(self, request, o_Order_ID, foramt=None):

		orders = OrderShipmentsAll.objects.get(o_Order_ID=o_Order_ID)
		if orders:
			serializer = OrderShipmentsDetailSerializer(orders)
			return ({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})
		else:
			return ({"data": None, "code": status.HTTP_400_BAD_REQUEST, "message": RECORD_NOT_FOUND})

