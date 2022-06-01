from django.db import models


class OrderShipmentsAll(models.Model):
	'''
	Consists of details regarding the orders and shipments
	'''

	# o_id = models.AutoField(primary_key=True)
	o_id = models.AutoField(primary_key=True)

	o_Customer_Org_Level_2 = models.TextField(null=False, blank=False)

	o_Customer_Org_Level_3 = models.TextField(max_length=255, null=False, blank=False)

	o_Customer_Org_Level_4 = models.TextField(max_length=255, null=False, blank=False)

	o_Customer_Org_Level_5 = models.TextField(max_length=255, null=False, blank=False)

	o_Order_ID = models.TextField(max_length=255, null=False, blank=False)

	o_Bill_To = models.TextField(max_length=255, null=False, blank=False)

	o_Special_Service = models.TextField(max_length=255, null=False, blank=False)

	o_Bill_of_Lading = models.TextField(max_length=255, null=False, blank=False)

	o_Purchase_Order = models.TextField(max_length=255, null=False, blank=False)

	o_Origin_Ref_Purchase_Order = models.TextField(max_length=255, null=False, blank=False)
	
	o_Dest_Ref_Purchase_Order = models.TextField(max_length=255, null=False, blank=False)
	
	o_Shipment_ID = models.TextField(max_length=255, null=False, blank=False)
	
	o_CVN_Order_Reference = models.TextField(max_length=255, null=False, blank=False)
	
	o_Transport_Mode = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Status = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Cancel_Reason = models.TextField(max_length=255, null=False, blank=False)
	
	o_Early_Pickup = models.TextField(max_length=255, null=False, blank=False)
	
	o_Late_Pickup = models.TextField(max_length=255, null=False, blank=False)
	
	o_Early_Delivery = models.TextField(max_length=255, null=False, blank=False)
	
	o_Late_Delivery = models.TextField(max_length=255, null=False, blank=False)
	
	o_Lead_Time = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Origin_Location_Id = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Origin_Location_Type = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Origin_Location_Name = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Origin_Address = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Origin_City = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Origin_State = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Origin_Zip = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Origin_Country = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Destination_Location_ID = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Destination_Loc_Type = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Destination_Loc_Name = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Destination_Address = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Destination_City = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Destination_State = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Destination_Zip = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Destination_Country = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Stop_Seq = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Stop_Location_Type = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Stop_Name = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Stop_Address = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Stop_City = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Stop_State = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Stop_Zip = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Stop_Country = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Stop_Early_Arrival_Date = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Stop_Late_Arrival_Date = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Weight = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Volume_Cube = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Priority = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Best_Direct_Cost_Buy = models.TextField(max_length=255, null=False, blank=False)
	
	o_Srvprov_Recommendation = models.TextField(max_length=255, null=False, blank=False)
	
	o_Equipment_Recommendation = models.TextField(max_length=255, null=False, blank=False)
	
	o_Total_Package_Count = models.TextField(max_length=255, null=False, blank=False)
	
	o_Planner_Notes = models.TextField(max_length=255, null=False, blank=False)
	
	o_Planner_Notes_Count = models.TextField(max_length=255, null=False, blank=False)
	
	o_Service_Provider_Notes = models.TextField(max_length=255, null=False, blank=False)
	
	o_Service_Provider_Notes_Count = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Create_Method = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Create_Method = models.TextField(max_length=255, null=False, blank=False)
	
	o_Order_Create_Date = models.TextField(max_length=255, null=False, blank=False)
	
	s_id = models.TextField(max_length=255, null=False, blank=False)
	
	s_CUSTOMER_ORG_LEVEL_2 = models.TextField(max_length=255, null=False, blank=False)
	
	s_CUSTOMER_ORG_LEVEL_3 = models.TextField(max_length=255, null=False, blank=False)
	
	s_CUSTOMER_ORG_LEVEL_4 = models.TextField(max_length=255, null=False, blank=False)
	
	s_CUSTOMER_ORG_LEVEL_5 = models.TextField(max_length=255, null=False, blank=False)
	
	s_CUSTOMER_FREIGHT_CAT = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_ID = models.TextField(max_length=255, null=False, blank=False)
	
	s_MNGD_SHP_FLG = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_MASTER_BILL_OF_LADING = models.TextField(max_length=255, null=False, blank=False)
	
	s_ORDER_MASTER_BILL_OF_LADING = models.TextField(max_length=255, null=False, blank=False)
	
	s_ORDER_PURCHASE_ORDER = models.TextField(max_length=255, null=False, blank=False)
	
	s_ORDER_ORIG_REF_PURCHASE_ORDER = models.TextField(max_length=255, null=False, blank=False)
	
	s_ORDER_DEST_REF_PURCHASE_ORDER = models.TextField(max_length=255, null=False, blank=False)
	
	s_ORDER_RELEASE_NBRS = models.TextField(max_length=255, null=False, blank=False)
	
	s_CARRIER_PRO_NBR = models.TextField(max_length=255, null=False, blank=False)
	
	s_TRANSPORTATION_MODE = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_CANCELLED = models.TextField(max_length=255, null=False, blank=False)
	
	s_TENDER_STATUS = models.TextField(max_length=255, null=False, blank=False)
	
	s_ENROUTE_STATUS = models.TextField(max_length=255, null=False, blank=False)
	
	s_PLANNED_SERVICE_PROVIDER_NAME = models.TextField(max_length=255, null=False, blank=False)
	
	s_PLANNED_SRVPROV_SCAC_CODE = models.TextField(max_length=255, null=False, blank=False)
	
	s_PLANNED_SERVICE_PROV_ID = models.TextField(max_length=255, null=False, blank=False)
	
	s_ACTUAL_SERVICE_PROVIDER_NAME = models.TextField(max_length=255, null=False, blank=False)
	
	s_ACTUAL_SRVPROV_SCAC_CODE = models.TextField(max_length=255, null=False, blank=False)
	
	s_ACTUAL_SERVICE_PROV_ID = models.TextField(max_length=255, null=False, blank=False)
	
	s_SERV_PROV_TRAILER_NUMBER = models.TextField(max_length=255, null=False, blank=False)
	
	s_EQUIPMENT_DESCRIPTION = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_STOP_CT = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_STOP_TOTAL_COST = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_STOP_LHL_COST = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_STOP_FUEL_COST = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_TOTAL_WEIGHT = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_WEIGHT_UOM = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_TOTAL_DISTANCE = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_DISTANCE_UOM = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_TOTAL_VOLUME = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_VOLUME_UOM = models.TextField(max_length=255, null=False, blank=False)
	
	s_ORIG_PLANNED_DEPART_DATE_TIME = models.TextField(max_length=255, null=False, blank=False)
	
	s_ORIG_PLANNED_ARRIVAL_DATE = models.TextField(max_length=255, null=False, blank=False)
	
	s_ORIG_ACTUAL_ARRIVAL_DATE = models.TextField(max_length=255, null=False, blank=False)
	
	s_DEST_PLANNED_DEPART_DATE_TIME = models.TextField(max_length=255, null=False, blank=False)
	
	s_DEST_ACTUAL_ARRIVAL_DATE_TIME = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_ORIGIN_ID = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_ORIGIN_LOCATION_NAME = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_ORIGIN_LOCATION_TYPE = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_ORIGIN_ADDRESS = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_ORIGIN_CITY = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_ORIGIN_STATE = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_ORIGIN_ZIP = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_ORIGIN_COUNTRY = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_DEST_LOCATION_ID = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_DEST_LOCATION_TYPE = models.TextField(max_length=255, null=False, blank=False)

	s_SHIPMENT_DESTINATION_NAME = models.TextField(max_length=255, null=False, blank=False)

	s_SHIPMENT_DESTINATION_ADDRESS = models.TextField(max_length=255, null=False, blank=False)

	s_SHIPMENT_DESTINATION_CITY = models.TextField(max_length=255, null=False, blank=False)

	s_SHIPMENT_DESTINATION_STATE = models.TextField(max_length=255, null=False, blank=False)

	s_SHIPMENT_DESTINATION_ZIP = models.TextField(max_length=255, null=False, blank=False)

	s_SHIPMENT_DESTINATION_COUNTRY = models.TextField(max_length=255, null=False, blank=False)

	s_FIRST_ESTIMATED_DEPARTURE = models.TextField(max_length=255, null=False, blank=False)

	s_FIRST_ESTIMATED_ARRIVAL = models.TextField(max_length=255, null=False, blank=False)

	s_FIRST_ACTUAL_DEPARTURE = models.TextField(max_length=255, null=False, blank=False)

	s_FIRST_APPOINTMENT_PICKUP = models.TextField(max_length=255, null=False, blank=False)
	
	s_LAST_PLANNED_ARRIVAL = models.TextField(max_length=255, null=False, blank=False)
	
	s_LAST_ESTIMATED_DEPARTURE = models.TextField(max_length=255, null=False, blank=False)

	s_LAST_ESTIMATED_ARRIVAL = models.TextField(max_length=255, null=False, blank=False)
	
	s_LAST_ACTUAL_DEPARTURE = models.TextField(max_length=255, null=False, blank=False)
	
	s_LAST_APPOINTMENT_DELIVERY = models.TextField(max_length=255, null=False, blank=False)

	s_SHIPMENT_INSERT_USERID = models.TextField(max_length=255, null=False, blank=False)
	
	s_SHIPMENT_INSERT_DT = models.TextField(max_length=255, null=False, blank=False)
	
	s_LAST_EV_LOC_UPDATE = models.TextField(max_length=255, null=False, blank=False)
	
	s_LAST_EV_TRACKING_STATUS_UPDATE = models.TextField(max_length=255, null=False, blank=False)

	s_LAST_STOPREFID_EV_ETA_UPDATE = models.TextField(max_length=255, null=False, blank=False)
	
	s_LAST_EV_LOC_DTTM_UPDATE = models.TextField(max_length=255, null=False, blank=False)
	
	s_LAST_EV_ETA_DTTM_UPDATE = models.TextField(max_length=255, null=False, blank=False)


class Meta:
	db_table = 'order_shipments_all'
	indexes = [
				models.Index(fields=['o_id'])
			]

def __str__(self):
	return self.o_Order_ID