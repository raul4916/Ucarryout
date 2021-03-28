from UCarryout.models import Menu, MenuType, Food, FoodCategory, Restaurant
from django.views import View

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from rest_framework.views import APIView

import json



class MenuView(APIView):
	def get(self, request: HttpRequest):

		menu_dict = Menu.objects.get(id=request.GET['id']).as_dict()

		return HttpResponse(json.dumps(menu_dict),'application/json')


	def post(self, request: HttpRequest):
		raw_menu = request.body.decode('UTF-8')
		json_menu = json.loads(raw_menu)
		menu = Menu()
		menu.description = json_menu['description']
		menu.save()

		for menu_type in json_menu['menu_types']:
			menu_type_obj = MenuType.objects.get_or_create(value = menu_type)[0]
			menu.type.add(menu_type_obj)

		if 'food' in json_menu:
			food_arr = self.add_food(json_menu['food'])

		if food_arr is not None:
			for food_obj in food_arr:
				menu.food.add(food_obj)

		menu.save()

		restaurant = Restaurant.objects.get(id=json_menu['restaurant']['id'])

		restaurant.menu.add(menu)

		return HttpResponse(json.dumps(menu.as_dict()),'application/json')

	def patch(self, request: HttpRequest):
		raw_menu = request.body.decode('UTF-8')
		json_menu = json.loads(raw_menu)
		menu = Menu.objects.get(id = json_menu['id'])

		if json_menu['food'] is not None:
			food_obj = self.add_food(json_menu['food'])

		if food_obj is None:
			menu.food.add(food_obj)

		menu.save()

		return HttpResponse(json.dumps(menu.as_dict()),'application/json')


	def delete(self, request: HttpRequest):
		raw_menu = request.body.decode('UTF-8')
		json_menu = json.loads(raw_menu)
		menu = Menu.objects.get(id = json_menu['id']).delete()

	def add_food(self, food_json):
		food_arr = []
		for food in food_json:
			for food_category in food['category']:
				food_category_obj = FoodCategory.objects.get_or_create(name = food_category)[0]

			food_obj = Food.objects.get_or_create(
					name = food['name'],
					price = food['price'],
					description = food['description'],
					calories = food['calories'],
					)[0]

			food_obj.category.add(food_category_obj)
			food_arr.append(food_obj);

		return food_arr
