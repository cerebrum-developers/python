from django.db import models


class OrderRateLookUp(models.Model):
	'''
	Consists of details regarding the rate lookups
	'''

	id = models.AutoField(primary_key=True)

	o_id = models.IntegerField()

	o_city = models.TextField(max_length=255, null=True, blank=True)

	o_state = models.TextField(max_length=255, null=True, blank=True)
	
	o_country = models.TextField(max_length=255, null=True, blank=True)

	o_location = models.TextField(max_length=255, null=True, blank=True)
	
	o_zip_code = models.IntegerField()
	
	o_transporation_type = models.TextField(max_length=255, null=True, blank=True)
	
	o_company = models.TextField(max_length=255, null=True, blank=True)
	
	o_weight = models.FloatField()
	
	o_volume = models.FloatField()
	
	o_rate = models.FloatField()
	
	s_id = models.IntegerField()

	s_city = models.TextField(max_length=255, null=True, blank=True)
	
	s_state = models.TextField(max_length=255, null=True, blank=True)
	
	s_country = models.TextField(max_length=255, null=True, blank=True)
	
	s_location = models.TextField(max_length=255, null=True, blank=True)
	
	s_zip_code = models.IntegerField()
	
	s_transporation_type = models.TextField(max_length=255, null=True, blank=True)
	
	s_company = models.TextField(max_length=255, null=True, blank=True)
	
	s_weight = models.FloatField()
	
	s_volume = models.FloatField()
	
	s_rate = models.FloatField()
		
	created_at =  models.DateTimeField(auto_now_add=True)

	updated_at =  models.DateTimeField(auto_now_add=True)
	
	deleted_at =  models.DateTimeField(auto_now_add=True)

class Meta:
	db_table = 'order_rate_lookup'
	

def __str__(self):
	return self.id