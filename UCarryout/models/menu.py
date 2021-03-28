from django.db import models
from UCarryout.models import Food


class MenuType(models.Model):
	value = models.CharField(max_length = 24)


class Menu(models.Model):
	type = models.ManyToManyField(MenuType, related_name = 'menus', related_query_name = 'menu')
	food = models.ManyToManyField(Food, related_name = 'menus', related_query_name = 'menu')
	description = models.CharField(max_length = 255)

	def as_dict(self):
		return {
			'id'         :self.id,
			'description':self.description,
			'type'       :[obj.value for obj in self.type.all()],
			'food'       :[obj.as_dict() for obj in self.food.all()],
			}
