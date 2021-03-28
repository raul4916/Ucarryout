from UCarryout.models import Promotion, Restaurant, ClientUser
from django.views import View
from django.http.request import HttpRequest
from django.http.response import *
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView

import json


class StripeView(APIView):

	@staticmethod
	def get(request: HttpRequest):

	@staticmethod
	@login_required
	def post(request: HttpRequest):

	@staticmethod
	def patch(request: HttpRequest):

	@staticmethod
	def delete(request: HttpRequest):







