from django.db import models


class PriceIndex(models.Model):
	value = models.IntegerField(max_length = 5)


class OperationHours(models.Model):
	open_hour = models.CharField(max_length = 5)
	close_hour = models.CharField(max_length = 5)
