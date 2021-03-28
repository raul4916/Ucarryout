from django.db import models
from UCarryout.models.restaurant import Restaurant
from UCarryout.models.user import ClientUser


class CustomerPoints(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete = models.PROTECT)
	user = models.ForeignKey(ClientUser, on_delete = models.PROTECT)
	points = models.IntegerField()

	def as_dict(self):
		return {
			'points'    :self.points,
			'restaurant':{
				'id':'self.restaurant.id'
				}
			}
