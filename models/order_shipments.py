from django.db import models


class OrderShipments(models.Model):
	'''
	Consists of details regarding the order shipments
	'''

	id = models.AutoField(primary_key=True)

	Customer_Org_Level_2 = models.TextField(null=False, blank=False)

	Customer_Org_Level_3 = models.TextField(max_length=255, null=False, blank=False)

	Customer_Org_Level_4 = models.TextField(max_length=255, null=False, blank=False)
	
	Customer_Org_Level_5 = models.TextField(max_length=255, null=False, blank=False)

	Order_ID = models.TextField(max_length=255, null=False, blank=False)
	
	Bill_To = models.TextField(max_length=255, null=False, blank=False)
	
	Special_Service = models.TextField(max_length=255, null=False, blank=False)
	
	Bill_of_Lading = models.TextField(max_length=255, null=False, blank=False)
	
	Purchase_Order = models.TextField(max_length=255, null=False, blank=False)
	
	Origin_Ref_Purchase_Order = models.TextField(max_length=255, null=False, blank=False)
	
	Dest_Ref_Purchase_Order = models.TextField(max_length=255, null=False, blank=False)
	
	Shipment_ID = models.TextField(max_length=255, null=False, blank=False)

	CVN_Order_Reference = models.TextField(max_length=255, null=False, blank=False)
	
	Transport_Mode = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Status = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Cancel_Reason = models.TextField(max_length=255, null=False, blank=False)
	
	Early_Pickup = models.TextField(max_length=255, null=False, blank=False)
	
	Late_Pickup = models.TextField(max_length=255, null=False, blank=False)
	
	Early_Delivery = models.TextField(max_length=255, null=False, blank=False)
	
	Late_Delivery = models.TextField(max_length=255, null=False, blank=False)
	
	Lead_Time = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Origin_Location_Id = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Origin_Location_Type = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Origin_Location_Name = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Origin_Address = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Origin_City = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Origin_State = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Origin_Zip = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Origin_Country = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Destination_Location_ID = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Destination_Loc_Type = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Destination_Loc_Name = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Destination_Address = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Destination_City = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Destination_State = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Destination_Zip = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Destination_Country = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Stop_Seq = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Stop_Location_Type = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Stop_Name = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Stop_Address = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Stop_City = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Stop_State = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Stop_Zip = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Stop_Country = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Stop_Early_Arrival_Date = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Stop_Late_Arrival_Date = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Weight = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Volume_Cube = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Priority = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Best_Direct_Cost_Buy = models.TextField(max_length=255, null=False, blank=False)
	
	Srvprov_Recommendation = models.TextField(max_length=255, null=False, blank=False)
	
	Equipment_Recommendation = models.TextField(max_length=255, null=False, blank=False)
	
	Total_Package_Count = models.TextField(max_length=255, null=False, blank=False)
	
	Planner_Notes = models.TextField(max_length=255, null=False, blank=False)
	
	Planner_Notes_Count = models.TextField(max_length=255, null=False, blank=False)
	
	Service_Provider_Notes = models.TextField(max_length=255, null=False, blank=False)
	
	Service_Provider_Notes_Count = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Create_Method = models.TextField(max_length=255, null=False, blank=False)
	
	Order_Create_Date = models.TextField(max_length=255, null=False, blank=False)


	class Meta:
		db_table = 'order_shipments'
		indexes = [
            models.Index(fields=['id'])
        ]

	def __str__(self):
		return self.Order_ID