from django.db.models import Manager
from UCarryout.models import restaurant, menu


class MenuManager(Manager):

	def init_menu(self, restaurant_id, menu_type, description):
		restaurant_qs = restaurant.Restaurant.objects.get(id = restaurant_id);
		menu_type = menu.MenuType.objects.get(value = menu_type)
		return super().create(restaurant = restaurant_qs, type = menu_type, description = description)

