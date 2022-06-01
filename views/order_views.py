from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from orders.services.order_services import OrderService
from orders.services.orders_detail_service import OrderDetailService

orderService = OrderService()

class OrderShipmentsAllListView(APIView):

	def post(self, request, format=None):
		"""
		Return all order shipments list.
		"""
		result = orderService.get_all_order_shipments_list_with_pagination(request, format=None)
		return Response(result, status=status.HTTP_200_OK)

	def get(self, request, format=None):
		"""
		Return order shipments list.
		"""
		result = orderService.get_order_shipments_list(request, format=None)
		return Response(result, status=status.HTTP_200_OK)


class OrderDetailView(APIView):

	def get(self, request, o_Order_ID, format=None):
		"""
		detail view of order
		"""
		result = OrderDetailService.get_detail_view(self, request, o_Order_ID)
		return Response(result, status=status.HTTP_200_OK)

