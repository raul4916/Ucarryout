"""UCarryoutCompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import path
from UCarryout.views.menu import *
from UCarryout.views.user import *
from UCarryout.views.restaurant import *
from UCarryout.views.promotion import *
from UCarryout.views.temp_user import *

from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('api/menu', MenuView.as_view()),

    path('api/user', UserView.as_view()),
	path('api/user/register', RegisterUserView.as_view()),
	path('api/restaurant', RestaurantView.as_view()),
	path('api/promotions', PromotionView.as_view()),
	path('api/promotions/user', PromotionView.add_user_to_promo),

	path('api/public-restaurant', PublicRestaurantView.as_view()),
	path('user/login', UserView.login_user),
	path('user/logout', UserView.logout_user),
	path('api/user/fav-restaurant', UserView.add_fav_restaurant),

	path('token-auth', obtain_jwt_token),
	path('current-user', current_user),


	]
