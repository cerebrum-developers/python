import json
from rest_framework import status
from rest_framework.response import Response

import datetime
from datetime import datetime, date

from django.core.exceptions import ValidationError
from django.db.models import Q

from .order_base_services import OrderBaseService
from orders.serializers.order_serializer import OrderShipmentsAllListSerializer
from orders.models.order_shipments_all import OrderShipmentsAll

from utils.messages.common_messages import * 
from utils.custom_pagination import CustomPagination
from utils import CustomPagination

class OrderService(OrderBaseService):

	def __init__(self):
		pass

	def get_all_order_shipments_list_with_pagination(self, request, format=None):

		search_type = 'or'
		custom_pagination = CustomPagination()
		search_keys = ['o_id__icontains']

		if 'date_filters' in request.data and request.data['date_filters'] != {}:
			start_date = request.data['date_filters']['start-date']
			end_date = request.data['date_filters']['end-date']

		if 'date_filters' in request.data and not 'mode' in request.data and not 'geography_filters' in request.data:
			print('1')
			if request.data['date_filters'] != {}:
				if 'type' in request.data['date_filters'] and request.data['date_filters']['type'] != None:
					if request.data['date_filters']['type'] == "delivery-today":
						print('delivery')
						if request.data['date_filters']['start-date'] != None or request.data['date_filters']['start-date'] != "":
							print('in delivery 1')
							all_order_shipments = OrderShipmentsAll.objects.filter(s_DEST_ACTUAL_ARRIVAL_DATE_TIME__icontains=start_date)
							# print('Query ---- ', all_order_shipments.query)
						else:
							return ({"code": status.HTTP_200_OK, 'message': 'No results found'})
					elif request.data['date_filters']['type'] == "delivery-today-tomorrow":
						print('delivery')
						if request.data['date_filters']['start-date'] != None or request.data['date_filters']['start-date'] != "" and request.data['date_filters']['end-date'] != "":
							all_order_shipments = OrderShipmentsAll.objects.filter(Q(s_DEST_ACTUAL_ARRIVAL_DATE_TIME__icontains=start_date)|Q(s_DEST_ACTUAL_ARRIVAL_DATE_TIME__icontains=end_date))
						else:
							return ({"code": status.HTTP_200_OK, 'message': 'No results found'})
					elif request.data['date_filters']['type'] == "shipment":
						print('shipment')
						if request.data['date_filters']['start-date'] != "" or request.data['date_filters']['end-date'] != "":
							all_order_shipments = OrderShipmentsAll.objects.filter(s_ORIG_PLANNED_DEPART_DATE_TIME__gte=start_date, s_DEST_ACTUAL_ARRIVAL_DATE_TIME__lte=end_date)
						else:
							return ({"code": status.HTTP_200_OK, 'message': 'No results found'})
					else:
						all_order_shipments = OrderShipmentsAll.objects.all()
			else:
				print('else1')
				all_order_shipments = OrderShipmentsAll.objects.all()
		
		elif 'mode' in request.data and not 'date_filters' in request.data and not 'geography_filters' in request.data:
			print('2')
			if request.data['mode'] == 'Truckload':
				print('Truckload')
				all_order_shipments = OrderShipmentsAll.objects.filter(s_TRANSPORTATION_MODE="TRUCKLOAD TRANSPORT")
			elif request.data['mode'] == 'LTL':
				print('LTL')
				all_order_shipments = OrderShipmentsAll.objects.filter(s_TRANSPORTATION_MODE="LESS-THAN-TRUCKLOAD")
			elif request.data['mode'] == 'Flatbed':
				print('Flatbed')
				all_order_shipments = OrderShipmentsAll.objects.filter(s_TRANSPORTATION_MODE="FLATBED")
			elif request.data['mode'] == 'Intermodal':
				print('Intermodal')
				all_order_shipments = OrderShipmentsAll.objects.filter(s_TRANSPORTATION_MODE="INTERMODAL TRANSPORT")
			elif request.data['mode'] == 'Bulk':
				print('Bulk')
				all_order_shipments = OrderShipmentsAll.objects.filter(s_TRANSPORTATION_MODE="PARCEL TRANSPORT")
			else:
				print('else2')
				return ({"code": status.HTTP_200_OK, 'message': 'No results found'})
		
		elif 'geography_filters' in request.data and not 'date_filters' in request.data and not 'mode' in request.data:
			print('3')
			if 'origin' in request.data['geography_filters'] and not 'destination' in request.data['geography_filters'] and request.data['geography_filters'] != {}:
				if request.data['geography_filters']['origin'] and request.data['geography_filters']['origin'] != {}:
					if 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None:
						print('31')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None:
						print('32')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None:
						print('33')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None:
						print('34')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'])

					else:
						all_order_shipments = OrderShipmentsAll.objects.all()

			elif 'destination' in request.data['geography_filters'] and not 'origin' in request.data['geography_filters']  and request.data['geography_filters'] != {}: 
				if request.data['geography_filters']['destination'] and request.data['geography_filters']['destination'] != {}:
					if 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('41')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('42')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('43')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('44')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])

					else:
						all_order_shipments = OrderShipmentsAll.objects.all()

			elif 'origin' in request.data['geography_filters'] and 'destination' in request.data['geography_filters'] and request.data['geography_filters'] != {}: 
				if request.data['geography_filters']['origin'] and request.data['geography_filters']['origin'] != {} and request.data['geography_filters']['destination'] and request.data['geography_filters']['destination'] != {}:
					
					#####################
					if 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('51')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('52')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('53')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('54')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					#####################
					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('55')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('56')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('57')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					#####################
					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('58')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('59')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('510')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					#####################
					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('511')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('512')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('513')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					#####################
					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('514')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('515')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('516')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])
					#####################

					#####################
					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('517')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('518')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('519')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])
					#####################

					#####################
					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('520')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('521')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('522')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])
					#####################

					#####################
					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('523')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('524')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('525')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])
					#####################

					#####################
					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('526')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('527')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('528')
						all_order_shipments = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					else:
						all_order_shipments = OrderShipmentsAll.objects.all()

			else:
				return ({"code": status.HTTP_200_OK, 'message': 'No results found'})
		
		elif 'date_filters' in request.data and 'mode' in request.data and not 'geography_filters' in request.data:
			print('4')

			if request.data['date_filters'] != {}:
				if 'type' in request.data['date_filters'] and request.data['date_filters']['type'] != None:
					if request.data['date_filters']['type'] == "delivery-today":
						print('delivery')
						if request.data['date_filters']['start-date'] != None or request.data['date_filters']['start-date'] != "":
							date_filters = OrderShipmentsAll.objects.filter(s_DEST_ACTUAL_ARRIVAL_DATE_TIME__icontains=start_date)
						else:
							return ({"code": status.HTTP_200_OK, 'message': 'No results found'})
					elif request.data['date_filters']['type'] == "delivery-today-tomorrow":
						print('delivery')
						if request.data['date_filters']['start-date'] != None or request.data['date_filters']['start-date'] != "" and request.data['date_filters']['end-date'] != "":
							date_filters = OrderShipmentsAll.objects.filter(Q(s_DEST_ACTUAL_ARRIVAL_DATE_TIME__icontains=start_date)|Q(s_DEST_ACTUAL_ARRIVAL_DATE_TIME__icontains=end_date))
						else:
							return ({"code": status.HTTP_200_OK, 'message': 'No results found'})
					elif request.data['date_filters']['type'] == "shipment":
						print('shipment')
						if request.data['date_filters']['start-date'] != "" or request.data['date_filters']['end-date'] != "":
							date_filters = OrderShipmentsAll.objects.filter(s_ORIG_PLANNED_DEPART_DATE_TIME__gte=start_date, s_DEST_ACTUAL_ARRIVAL_DATE_TIME__lte=end_date)
						else:
							return ({"code": status.HTTP_200_OK, 'message': 'No results found'})
					else:
						date_filters = OrderShipmentsAll.objects.all()
			else:
				print('else1')
				date_filters = OrderShipmentsAll.objects.all()


			if request.data['mode'] == 'Truckload':
				print('Truckload')
				all_order_shipments = date_filters.filter(s_TRANSPORTATION_MODE="TRUCKLOAD TRANSPORT")
			elif request.data['mode'] == 'LTL':
				print('LTL')
				all_order_shipments = date_filters.filter(s_TRANSPORTATION_MODE="LESS-THAN-TRUCKLOAD")
			elif request.data['mode'] == 'Flatbed':
				print('Flatbed')
				all_order_shipments = date_filters.filter(s_TRANSPORTATION_MODE="FLATBED")
			elif request.data['mode'] == 'Intermodal':
				print('Intermodal')
				all_order_shipments = date_filters.filter(s_TRANSPORTATION_MODE="INTERMODAL TRANSPORT")
			elif request.data['mode'] == 'Bulk':
				print('Bulk')
				all_order_shipments = date_filters.filter(s_TRANSPORTATION_MODE="PARCEL TRANSPORT")
			else:
				print('else22')
				return ({"code": status.HTTP_200_OK, 'message': 'No results found'})

		elif 'mode' in request.data and 'geography_filters' in request.data and not 'date_filters' in request.data:
			print('5')
			if 'origin' in request.data['geography_filters'] and not 'destination' in request.data['geography_filters'] and request.data['geography_filters'] != {}:
				if request.data['geography_filters']['origin'] and request.data['geography_filters']['origin'] != {}:
					if 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None:
						print('31')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None:
						print('32')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None:
						print('33')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None:
						print('34')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'])

					else:
						geography_filters = OrderShipmentsAll.objects.all()

			elif 'destination' in request.data['geography_filters'] and not 'origin' in request.data['geography_filters']  and request.data['geography_filters'] != {}: 
				if request.data['geography_filters']['destination'] and request.data['geography_filters']['destination'] != {}:
					if 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('41')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('42')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('43')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('44')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])

					else:
						geography_filters = OrderShipmentsAll.objects.all()

			elif 'origin' in request.data['geography_filters'] and 'destination' in request.data['geography_filters'] and request.data['geography_filters'] != {}: 
				if request.data['geography_filters']['origin'] and request.data['geography_filters']['origin'] != {} and request.data['geography_filters']['destination'] and request.data['geography_filters']['destination'] != {}:
					
					#####################
					if 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('51')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('52')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('53')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('54')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					#####################
					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('55')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('56')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('57')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					#####################
					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('58')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('59')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('510')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					#####################
					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('511')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('512')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('513')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					#####################
					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('514')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('515')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('516')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])
					#####################

					#####################
					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('517')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('518')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('519')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])
					#####################

					#####################
					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('520')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('521')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('522')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])
					#####################

					#####################
					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('523')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('524')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('525')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])
					#####################

					#####################
					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('526')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('527')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('528')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					else:
						geography_filters = OrderShipmentsAll.objects.all()


			if request.data['mode'] == 'Truckload':
				print('Truckload')
				all_order_shipments = geography_filters.filter(s_TRANSPORTATION_MODE="TRUCKLOAD TRANSPORT")
			elif request.data['mode'] == 'LTL':
				print('LTL')
				all_order_shipments = geography_filters.filter(s_TRANSPORTATION_MODE="LESS-THAN-TRUCKLOAD")
			elif request.data['mode'] == 'Flatbed':
				print('Flatbed')
				all_order_shipments = geography_filters.filter(s_TRANSPORTATION_MODE="FLATBED")
			elif request.data['mode'] == 'Intermodal':
				print('Intermodal')
				all_order_shipments = geography_filters.filter(s_TRANSPORTATION_MODE="INTERMODAL TRANSPORT")
			elif request.data['mode'] == 'Bulk':
				print('Bulk')
				all_order_shipments = geography_filters.filter(s_TRANSPORTATION_MODE="PARCEL TRANSPORT")
			else:
				print('else2')
				return ({"code": status.HTTP_200_OK, 'message': 'No results found'})

		elif 'date_filters' in request.data and 'geography_filters' in request.data and not 'mode' in request.data:
			print('6')

			if 'origin' in request.data['geography_filters'] and not 'destination' in request.data['geography_filters'] and request.data['geography_filters'] != {}:
				if request.data['geography_filters']['origin'] and request.data['geography_filters']['origin'] != {}:
					if 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None:
						print('31')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None:
						print('32')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None:
						print('33')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None:
						print('34')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'])

					else:
						geography_filters = OrderShipmentsAll.objects.all()

			elif 'destination' in request.data['geography_filters'] and not 'origin' in request.data['geography_filters']  and request.data['geography_filters'] != {}: 
				if request.data['geography_filters']['destination'] and request.data['geography_filters']['destination'] != {}:
					if 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('41')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('42')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('43')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('44')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])

					else:
						geography_filters = OrderShipmentsAll.objects.all()

			elif 'origin' in request.data['geography_filters'] and 'destination' in request.data['geography_filters'] and request.data['geography_filters'] != {}: 
				if request.data['geography_filters']['origin'] and request.data['geography_filters']['origin'] != {} and request.data['geography_filters']['destination'] and request.data['geography_filters']['destination'] != {}:
					
					#####################
					if 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('51')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('52')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('53')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('54')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					#####################
					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('55')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('56')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('57')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					#####################
					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('58')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('59')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('510')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					#####################
					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('511')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('512')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('513')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					#####################
					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('514')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('515')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('516')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])
					#####################

					#####################
					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('517')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('518')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('519')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])
					#####################

					#####################
					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('520')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('521')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('522')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])
					#####################

					#####################
					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('523')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('524')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('525')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])
					#####################

					#####################
					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('526')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('527')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('528')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					else:
						geography_filters = OrderShipmentsAll.objects.all()


			if request.data['date_filters'] != {}:
				if 'type' in request.data['date_filters'] and request.data['date_filters']['type'] != None:
					if request.data['date_filters']['type'] == "delivery-today":
						print('delivery')
						if request.data['date_filters']['start-date'] != None or request.data['date_filters']['start-date'] != "":
							all_order_shipments = geography_filters.filter(s_DEST_ACTUAL_ARRIVAL_DATE_TIME__icontains=start_date)
						else:
							return ({"code": status.HTTP_200_OK, 'message': 'No results found'})
					elif request.data['date_filters']['type'] == "delivery-today-tomorrow":
						print('delivery')
						if request.data['date_filters']['start-date'] != None or request.data['date_filters']['start-date'] != "" and request.data['date_filters']['end-date'] != "":
							all_order_shipments = geography_filters.filter(Q(s_DEST_ACTUAL_ARRIVAL_DATE_TIME__icontains=start_date)|Q(s_DEST_ACTUAL_ARRIVAL_DATE_TIME__icontains=end_date))
						else:
							return ({"code": status.HTTP_200_OK, 'message': 'No results found'})
					elif request.data['date_filters']['type'] == "shipment":
						print('shipment')
						if request.data['date_filters']['start-date'] != "" or request.data['date_filters']['end-date'] != "":
							all_order_shipments = geography_filters.filter(s_ORIG_PLANNED_DEPART_DATE_TIME__gte=start_date, s_DEST_ACTUAL_ARRIVAL_DATE_TIME__lte=end_date)
						else:
							return ({"code": status.HTTP_200_OK, 'message': 'No results found'})
					else:
						all_order_shipments = geography_filters.all()
			else:
				print('else1')
				all_order_shipments = geography_filters.all()
		

		elif 'date_filters' in request.data and 'mode' in request.data and 'geography_filters' in request.data:
			print('7')
			if 'origin' in request.data['geography_filters'] and not 'destination' in request.data['geography_filters'] and request.data['geography_filters'] != {}:
				if request.data['geography_filters']['origin'] and request.data['geography_filters']['origin'] != {}:
					if 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None:
						print('31')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None:
						print('32')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None:
						print('33')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None:
						print('34')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'])

					else:
						geography_filters = OrderShipmentsAll.objects.all()

			elif 'destination' in request.data['geography_filters'] and not 'origin' in request.data['geography_filters']  and request.data['geography_filters'] != {}: 
				if request.data['geography_filters']['destination'] and request.data['geography_filters']['destination'] != {}:
					if 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('41')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('42')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('43')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('44')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])

					else:
						geography_filters = OrderShipmentsAll.objects.all()

			elif 'origin' in request.data['geography_filters'] and 'destination' in request.data['geography_filters'] and request.data['geography_filters'] != {}: 
				if request.data['geography_filters']['origin'] and request.data['geography_filters']['origin'] != {} and request.data['geography_filters']['destination'] and request.data['geography_filters']['destination'] != {}:
					
					#####################
					if 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('51')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('52')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('53')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('54')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					#####################
					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('55')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('56')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('57')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					#####################
					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('58')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('59')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('510')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					#####################
					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('511')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('512')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('513')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					#####################
					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('514')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('515')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('516')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])
					#####################

					#####################
					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('517')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('518')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'state' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['state'] != None:
						print('519')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_STATE=request.data['geography_filters']['destination']['state'])
					#####################

					#####################
					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('520')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('521')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'city' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['city'] != None:
						print('522')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_CITY=request.data['geography_filters']['destination']['city'])
					#####################

					#####################
					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('523')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('524')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])

					elif 'zipcode' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['zipcode'] != None and 'country' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['country'] != None:
						print('525')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_ZIP=request.data['geography_filters']['origin']['zipcode'], s_SHIPMENT_DESTINATION_COUNTRY=request.data['geography_filters']['destination']['country'])
					#####################

					#####################
					elif 'state' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['state'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('526')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_STATE=request.data['geography_filters']['origin']['state'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])

					elif 'city' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['city'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('527')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_CITY=request.data['geography_filters']['origin']['city'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])

					elif 'country' in request.data['geography_filters']['origin'] and request.data['geography_filters']['origin']['country'] != None and 'zipcode' in request.data['geography_filters']['destination'] and request.data['geography_filters']['destination']['zipcode'] != None:
						print('528')
						geography_filters = OrderShipmentsAll.objects.filter(s_SHIPMENT_ORIGIN_COUNTRY=request.data['geography_filters']['origin']['country'], s_SHIPMENT_DESTINATION_ZIP=request.data['geography_filters']['destination']['zipcode'])
					#####################

					else:
						geography_filters = OrderShipmentsAll.objects.all()


			if request.data['date_filters'] != {}:
				if 'type' in request.data['date_filters'] and request.data['date_filters']['type'] != None:
					if request.data['date_filters']['type'] == "delivery-today":
						print('delivery')
						if request.data['date_filters']['start-date'] != None or request.data['date_filters']['start-date'] != "":
							date_filters = geography_filters.filter(s_DEST_ACTUAL_ARRIVAL_DATE_TIME__icontains=start_date)
						else:
							return ({"code": status.HTTP_200_OK, 'message': 'No results found'})
					elif request.data['date_filters']['type'] == "delivery-today-tomorrow":
						print('delivery')
						if request.data['date_filters']['start-date'] != None or request.data['date_filters']['start-date'] != "" and request.data['date_filters']['end-date'] != "":
							date_filters = geography_filters.filter(Q(s_DEST_ACTUAL_ARRIVAL_DATE_TIME__icontains=start_date)|Q(s_DEST_ACTUAL_ARRIVAL_DATE_TIME__icontains=end_date))
						else:
							return ({"code": status.HTTP_200_OK, 'message': 'No results found'})
					elif request.data['date_filters']['type'] == "shipment":
						print('shipment')
						if request.data['date_filters']['start-date'] != "" or request.data['date_filters']['end-date'] != "":
							date_filters = geography_filters.filter(s_ORIG_PLANNED_DEPART_DATE_TIME__gte=start_date, s_DEST_ACTUAL_ARRIVAL_DATE_TIME__lte=end_date)
						else:
							return ({"code": status.HTTP_200_OK, 'message': 'No results found'})
					else:
						date_filters = geography_filters.all()
			else:
				print('else1')
				date_filters = geography_filters.all()
				

			if request.data['mode'] == 'Truckload':
				print('Truckload')
				all_order_shipments = date_filters.filter(s_TRANSPORTATION_MODE="TRUCKLOAD TRANSPORT")
			elif request.data['mode'] == 'LTL':
				print('LTL')
				all_order_shipments = date_filters.filter(s_TRANSPORTATION_MODE="LESS-THAN-TRUCKLOAD")
			elif request.data['mode'] == 'Flatbed':
				print('Flatbed')
				all_order_shipments = date_filters.filter(s_TRANSPORTATION_MODE="FLATBED")
			elif request.data['mode'] == 'Intermodal':
				print('Intermodal')
				all_order_shipments = date_filters.filter(s_TRANSPORTATION_MODE="INTERMODAL TRANSPORT")
			elif request.data['mode'] == 'Bulk':
				print('Bulk')
				all_order_shipments = date_filters.filter(s_TRANSPORTATION_MODE="PARCEL TRANSPORT")
			else:
				print('else222')
				return ({"code": status.HTTP_200_OK, 'message': 'No results found'})

		else:
			print('else')
			all_order_shipments = OrderShipmentsAll.objects.all()

		response = custom_pagination.custom_pagination(request, OrderShipmentsAll, search_keys, search_type, OrderShipmentsAllListSerializer, all_order_shipments)

		return ({"data": response,"code": status.HTTP_200_OK, 'message': OK})


	def get_order_shipments_list(self, request, format=None):
		"""
		List all order shipments
		"""

		all_order_shipments = OrderShipmentsAll.objects.all()

		serializer = OrderShipmentsAllListSerializer(all_order_shipments, many=True)

		return ({"data": serializer.data,"code": status.HTTP_200_OK, 'message': OK})
