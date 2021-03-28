from UCarryout.models import Menu, MenuType, Food, FoodCategory, ClientUser
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView

import json


class FoodView(APIView):

	@staticmethod
	def get(request: HttpRequest):
		raw_food = request.body.decode('UTF-8')
		json_food = json.loads(raw_food)
		request_filters = { }

		if 'name' in json_food:
			request_filters['name'] = json_food['name']

		if 'price' in json_food:
			request_filters['price'] = json_food['price']

		if 'description' in json_food:
			request_filters['description'] = json_food['description']

		if 'calories' in json_food:
			request_filters['calories'] = json_food['calories']

		if 'calories' in json_food:
			request_filters['calories'] = json_food['calories']

		if 'category' in json_food:
			request_filters['category'] = FoodCategory.objects.get(json_food['category'])

		foods = Food.objects.filter(**request_filters);

		foods_dict = [obj.as_dict() for obj in foods]

		return HttpResponse(json.dumps(foods_dict), content_type = 'application/json')

	@staticmethod
	@login_required
	def post(request: HttpRequest):
		raw_food = request.body.decode('UTF-8')
		json_food = json.loads(raw_food)

		for food in json_food:
			for food_category in food['food_category']:
				food_category_obj = FoodCategory.objects.get_or_create(name = food_category['name'])[0]

			food_obj = Food.objects.get_or_create(
					name = food['name'],
					price = food['price'],
					description = food['description'],
					calories = food['calories'],
					)

			food_obj.category.add(food_category_obj)

	@staticmethod
	def patch(request: HttpRequest):
		raw_food = request.body.decode('UTF-8')
		json_food = json.loads(raw_food)

		food = Food.objects.get(id = json_food['id']);

		if 'name' in json_food:
			food.name = json_food['name']

		if 'price' in json_food:
			food.category = json_food['category']

		if 'description' in json_food:
			food.average_price = json_food['average_price']

		if 'calories' in json_food:
			food.calories = json_food['calories']

		if 'category' in json_food:
			food.category = food.objects.get(json_food['category'])

		food.save()

		return HttpResponse(json.dumps(food.as_dict()), content_type = 'application/json')

	@staticmethod
	def delete(request: HttpRequest):
		raw_food = request.body.decode('UTF-8')
		json_food = json.loads(raw_food)

		food = Food.objects.get(id = json_food['id'])

		food.delete()
