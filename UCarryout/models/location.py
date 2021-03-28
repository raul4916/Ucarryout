from django.db import models


class Location(models.Model):
	street = models.CharField(max_length = 150)
	city = models.CharField(max_length = 150)
	state = models.CharField(max_length = 150)
	country = models.CharField(max_length = 150)
	zip_code = models.CharField(max_length = 150)

	def as_dict(self):
		return {
			'id'      :self.id,
			'street'  :self.street,
			'city'    :self.city,
			'state'   :self.state,
			'country' :self.country,
			'zip_code':self.zip_code,
			}
