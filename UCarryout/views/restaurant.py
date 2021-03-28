from UCarryout.models import Restaurant, Location, ClientUser
from django.views import View

from django.http.request import HttpRequest
from django.http.response import *

from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny

import json


class RestaurantView(APIView):
	def post(self, request: HttpRequest):
		raw_restaurant = request.body.decode('UTF-8')
		json_restaurant = json.loads(raw_restaurant)

		if request.user.is_authenticated:
			ownerID = request.user.clientuser.id
		else:
			return HttpResponseForbidden(json.dumps({"response":"Unable to get your response." + str(request.user)}), content_type = 'application/json')

		owner = ClientUser.objects.get(id = ownerID);

		restaurant = Restaurant.objects.create(**json_restaurant['restaurant'])
		restaurant.locations = Location.objects.create(**json_restaurant['location'])

		owner.restaurant.add(restaurant)

		return HttpResponse(json.dumps   (restaurant.as_dict()), content_type = 'application/json')

	def patch(self, request: HttpRequest):
		raw_restaurant = request.body.decode('UTF-8')
		json_restaurant = json.loads(raw_restaurant)
		restaurant = Restaurant.objects.get(id = json_restaurant['id']);

		if 'name' in json_restaurant:
			restaurant.name = json_restaurant['name']

		if 'category' in json_restaurant:
			restaurant.category = json_restaurant['category']

		if 'description' in json_restaurant:
				restaurant.description = json_restaurant['description']

		if 'average_price' in json_restaurant:
			restaurant.average_price = json_restaurant['average_price']

		if 'hours' in json_restaurant:
			restaurant.hours = json_restaurant['hours']

		if 'location' in json_restaurant:
			restaurant.location.create(**json_restaurant['location'])

		restaurant.save()

		return HttpResponse(json.dumps(restaurant.as_dict()), content_type = 'application/json')

	def delete(self, request: HttpRequest):
		raw_menu = request.body.decode('UTF-8')
		json_menu = json.loads(raw_menu)



@permission_classes([AllowAny])
@authentication_classes([])
class PublicRestaurantView(APIView):
	def get(self, request: HttpRequest):

		json_restaurant = request.GET
		request_filters = { }

		if 'id' in json_restaurant:
			request_filters['id'] = json_restaurant['id']

		if 'name' in json_restaurant:
			request_filters['name'] = json_restaurant['name']

		if 'category' in json_restaurant:
			request_filters['category'] = json_restaurant['category']

		if 'average_price' in json_restaurant:
			request_filters['average_price'] = json_restaurant['average_price']

		if 'hours' in json_restaurant:
			request_filters['hours'] = json_restaurant['hours']

		if 'location' in json_restaurant:
			request_filters['location'] = Location.objects.filter(**json_restaurant['location'])

		restaurants = Restaurant.objects.filter(**request_filters)

		restaurants_dict = [obj.as_dict() for obj in restaurants]

		return HttpResponse(json.dumps(restaurants_dict), content_type = 'application/json')
