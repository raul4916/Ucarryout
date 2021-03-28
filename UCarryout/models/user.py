from django.contrib.auth.models import User, Permission
from django.db import models
from UCarryout.models import Restaurant, OrderHistory, Location, Promotion
from UCarryout.serializers import *


class ClientUser(models.Model):
	user_auth = models.OneToOneField(User, on_delete = models.PROTECT)
	permission = models.ManyToManyField(Permission)
	location = models.ManyToManyField(Location, related_name = 'userLocations', related_query_name = 'userLocation')
	phone = models.CharField(max_length = 50)
	restaurant = models.ManyToManyField(Restaurant)
	order_history = models.ManyToManyField(OrderHistory)
	active_promotions = models.ManyToManyField(Promotion, related_name = 'user_in_promos',
											   related_query_name = 'user_in_promo')
	fav_restaurants = models.ManyToManyField(Restaurant, related_name = 'fav_restaurants',
											 related_query_name = 'fav_restaurant')

	def as_dict(self):
		return {
			'id'               :self.id,
			'username'         :self.user_auth.username,
			'phone'            :self.phone,
			'restaurants'      :[obj.as_dict() for obj in self.restaurant.all()],
			'order_history'    :[obj.as_dict() for obj in self.order_history.all()],
			'location'         :[obj.as_dict() for obj in self.location.all()],
			'points'           :[obj.as_dict() for obj in self.customerpoints_set.all()],
			'active_promotions':[obj.as_dict() for obj in self.active_promotions.all()],
			'fav_restaurants'  :[obj.as_dict() for obj in self.fav_restaurants.all()],

			}

	def get_token(self):
		jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
		jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

		payload = jwt_payload_handler(self.user_auth)
		token = jwt_encode_handler(payload)
		return token
