from UCarryout.models import Promotion, Restaurant, ClientUser
from django.views import View
from django.http.request import HttpRequest
from django.http.response import *
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView

import json


class PromotionView(APIView):

	@staticmethod
	def get(request: HttpRequest):
		raw_promo = request.body.decode('UTF-8')
		json_promo = json.loads(raw_promo)
		request_filters = { }

		if 'restaurant_id' in json_promo:
			request_filters['restaurant_id'] = json_promo['restaurant_id']

		if 'id' in json_promo:
			request_filters['id'] = json_promo['id']

		promotions = Promotion.objects.filter(**request_filters);

		promotions_dict = [obj.as_dict() for obj in promotions]

		return HttpResponse(json.dumps(promotions_dict), content_type = 'application/json')

	@staticmethod
	@login_required
	def post(request: HttpRequest):
		raw_promo = request.body.decode('UTF-8')
		json_promo = json.loads(raw_promo)

		raw_promo = request.body.decode('UTF-8')
		json_promo = json.loads(raw_promo)

		if request.user.is_authenticated:
			ownerID = request.user.clientuser.id
		else:
			return HttpResponseForbidden(json.dumps({ "response":"Unable to get your response." + str(request.user) }),
										 content_type = 'application/json')

		promotion = Promotion.objects.create(**json_promo['promotion'])

		promotion.promotions.add(Restaurant.objects.get(id = json_promo['restaurant_id']));

		promotion.save()

		return HttpResponse(json.dumps(promotion.as_dict()), content_type = 'application/json')

	@staticmethod
	def patch(request: HttpRequest):
		raw_promo = request.body.decode('UTF-8')
		json_promo = json.loads(raw_promo)

	@staticmethod
	def delete(request: HttpRequest):
		raw_promo = request.body.decode('UTF-8')
		json_promo = json.loads(raw_promo)

	@staticmethod
	def add_user_to_promo(request: HttpRequest):
		raw_promo = request.body.decode('UTF-8')
		json_promo = json.loads(raw_promo)
		request_filters = { }

		if 'promotion' in json_promo and 'id' in json_promo['promotion']:
			request_filters['id'] = json_promo['promotion']['id']
		else:
			return HttpResponseBadRequest(json.dumps({ "response":"Missing promotion ID"}),
										 content_type = 'application/json')

		promotion = Promotion.objects.get(**request_filters)
		user = ClientUser.objects.get(id=json_promo['user']['id'])
		promotion.user_in_promos.add(user)

		return HttpResponse(json.dumps(promotion.as_dict()), content_type = 'application/json')




