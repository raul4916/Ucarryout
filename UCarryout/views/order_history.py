from django.views import View
from UCarryout.models import OrderHistory
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseForbidden
from django.contrib.auth.models import User

from rest_framework.views import APIView

import json


class OrderHistoryView(APIView):

	def get(request: HttpRequest):
		raw_order_history = request.body.decode('UTF-8')
		json_order_history = json.loads(raw_order_history)
		request_filters = { }

		if request.user.is_authenticated:
			ownerID = request.user.clientuser.id;
		else:
			return HttpResponseForbidden(json.dumps({ "response":"ERROR: login required" }),
										 content_type = 'application/json')

		if 'amount_due' in json_order_history:
			request_filters['amount_due'] = json_order_history['amount_due']

		if 'restaurant' in json_order_history:
			request_filters['restaurant'] = json_order_history['restaurant']

		if 'transaction_id' in json_order_history:
			request_filters['transaction_id'] = json_order_history['transaction_id']
		if 'created_date' in json_order_history:
			request_filters['created_date'] = json_order_history['created_date']

		order_histories = OrderHistory.objects.filter(**request_filters)

		order_histories_dict = [obj.as_dict() for obj in order_histories]

		return HttpResponse(json.dumps(order_histories_dict), content_type = 'application/json')

	def post(request: HttpRequest):
		raw_order_history = request.body.decode('UTF-8')
		json_order_history = json.loads(raw_order_history)

		if not request.user.is_authenticated:
			return HttpResponseForbidden(json.dumps({ "response":"Unable to get your response." }),
										 content_type = 'application/json')

		currUser = User.objects.get(username = request.user.username);
		order_history = OrderHistory.objects.create(**json_order_history)
		currUser.clientuser.restaurant.add(order_history)

		return HttpResponse(json.dumps(order_history.as_dict()), content_type = 'application/json')
