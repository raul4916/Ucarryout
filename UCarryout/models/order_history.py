from UCarryout.models import Restaurant, Food
from django.db import models


class OrderHistory(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete = models.PROTECT)
	amount_due = models.IntegerField
	transaction_id = models.CharField(max_length = 255)
	items_purchased = models.ManyToManyField(Food, related_name = 'item_purchased',
											 related_query_name = 'items_purchased')
	processed_date = models.DateTimeField()
	created_date = models.DateTimeField()

	def as_dict(self):
		return {
			'id'             :self.id,
			'amount_due'     :self.amount_due,
			'restaurant'     :self.restaurant,
			'processed_date' :self.processed_date,
			'created_date'   :self.created_date,
			'transaction_id' :self.transaction_id,
			'items_purchased':[obj.as_dict() for obj in self.items_purchased.all()],
			}
