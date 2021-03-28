from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseForbidden
from UCarryout.models import ClientUser, Location, Restaurant
from django.contrib.auth import authenticate, login, logout
from UCarryout.serializers import *

from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny

import json


class UserView(APIView):

	@staticmethod
	def get(request: HttpRequest):
		request_dict = dict(request.GET.items())

		user_queryset = ClientUser.objects.filter(**request_dict)
		users = [obj.as_dict() for obj in user_queryset]

		return HttpResponse(json.dumps(users), 'application/json')

	@staticmethod
	def patch(request):
		raw_user = request.body.decode('UTF-8')
		json_user = json.loads(raw_user)

		user = User.objects.get(username = request.user.username).clientuser

		if 'email' in json_user:
			user.user_auth.email = (json_user['user_auth']['email'])

		if 'password' in json_user:
			user.user_auth.set_password(json_user['password'])

		if 'location' in json_user:
			user.location.all().delete()
			user.location.create(**json_user['location'])

		if 'phone' in json_user['client_user']:
			user.phone = json_user['client_user']['phone']

		if 'restaurant' in json_user: 
			user.restaurant.create(**json_user['restaurant'])

		user.save()

		response = HttpResponse(json.dumps(user.as_dict()), 'application/json')

		return response

	@staticmethod
	def login_user(request: HttpRequest):
		raw_user = request.body.decode('UTF-8')
		json_user = json.loads(raw_user)

		user = authenticate(username = json_user['username'], password = json_user['password'])

		if user is not None:
			token = user.clientuser.get_token()
			user_dict = user.clientuser.as_dict()
			user_dict['token'] = token
			return HttpResponse(json.dumps(user_dict), 'application/json')
		else:
			return HttpResponseForbidden("{'login':'fail'}", 'application/json')

	@staticmethod
	def logout_user(request: HttpRequest):
		logout(request)
		return HttpResponse("{'logout':'success'}", 'application/json')

	@staticmethod
	def add_fav_restaurant(request: HttpRequest):
		raw_user = request.body.decode('UTF-8')
		json_user = json.loads(raw_user)

		user = ClientUser.objects.get(id=json_user['user_id'])
		fav_restaurant = Restaurant.objects.get(id=json_user['restaurant_id'])
		user.fav_restaurants.add(fav_restaurant);

		response = HttpResponse(json.dumps(user.as_dict()), 'application/json')

		return response


@permission_classes([AllowAny])
@authentication_classes([])
class RegisterUserView(APIView):

	@staticmethod
	def post(request: HttpRequest):
		raw_user = request.body.decode('UTF-8')
		json_user = json.loads(raw_user)
		user = User.objects.create_user(**json_user['user_auth'])
		client_user = ClientUser(**json_user['client_user'], user_auth = user)
		client_user.save()
		client_user.location.create(**json_user['location'])

		response = HttpResponse(json.dumps(client_user.as_dict()), 'application/json')
		return response
