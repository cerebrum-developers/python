from rest_framework import serializers
from orders.models.order_shipments_all import OrderShipmentsAll
from orders.models.order_rate_lookup import OrderRateLookUp

class OrderShipmentsAllListSerializer(serializers.ModelSerializer):

	class Meta:
		model = OrderShipmentsAll
		fields = '__all__'

class OrderShipmentsDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model = OrderShipmentsAll
		fields = ('o_Order_Origin_Location_Name', 'o_Order_Origin_Address', 'o_Order_Origin_City', 'o_Order_Origin_State',
				'o_Order_Origin_Zip', 'o_Order_Origin_Country', 'o_Order_Destination_Loc_Name', 'o_Order_Destination_Address', 'o_Order_Destination_City',
				'o_Order_Destination_State', 'o_Order_Destination_Zip', 'o_Order_Destination_Country', 'o_Order_ID', 's_ACTUAL_SERVICE_PROVIDER_NAME', 's_TRANSPORTATION_MODE',
				's_ACTUAL_SRVPROV_SCAC_CODE', 's_ENROUTE_STATUS', 's_EQUIPMENT_DESCRIPTION', 'o_Total_Package_Count', 's_SHIPMENT_TOTAL_WEIGHT', 's_SHIPMENT_ORIGIN_LOCATION_NAME',
				's_SHIPMENT_DESTINATION_NAME')

class OrderRateLookupSerializer(serializers.ModelSerializer):

	class Meta:
		model = OrderRateLookUp
		fields = '__all__'