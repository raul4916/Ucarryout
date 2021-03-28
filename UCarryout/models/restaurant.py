from UCarryout.models import Menu, Location, Promotion

from django.db import models


class Restaurant(models.Model):
	name = models.CharField(max_length = 50)
	category = models.CharField(max_length = 50)
	description = models.TextField()
	average_price = models.CharField(max_length = 50)
	hours = models.CharField(max_length = 50)
	location = models.ManyToManyField(Location, related_name = 'locations', related_query_name = 'location')
	menu = models.ManyToManyField(Menu, related_name = 'menus', related_query_name = 'menu')
	img_url = models.CharField(max_length = 255)
	promotions = models.ManyToManyField(Promotion, related_name = 'promotions', related_query_name = 'promotion')

	def as_dict(self):
		return {
			'id'           :self.id,
			'name'         :self.name,
			'category'     :self.category,
			'description'  :self.description,
			'average_price':self.average_price,
			'hours'        :self.hours,
			'img_url'      :self.img_url,
			'owners'       :[obj.id for obj in self.clientuser_set.all()],
			'location'     :[obj.as_dict() for obj in self.location.all()],
			'menu'         :[obj.as_dict() for obj in self.menu.all()],
			'promotions'   :[obj.as_dict() for obj in self.promotions.all()],
			}
