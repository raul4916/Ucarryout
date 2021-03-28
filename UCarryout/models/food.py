from django.db import models


class FoodCategory(models.Model):
	name = models.CharField(max_length = 25)

	def as_dict(self):
		return {
			'id'  :self.id,
			'name':self.name,
			}


class Food(models.Model):
	name = models.CharField(max_length = 25)
	price = models.CharField(max_length = 25)
	description = models.CharField(max_length = 255)
	calories = models.CharField(max_length = 25)
	category = models.ManyToManyField(FoodCategory, related_name = 'food_category',
									  related_query_name = 'food_category')
	imgURL = models.CharField(max_length = 255)

	def as_dict(self):
		return {
			'id'         :self.id,
			'name'       :self.name,
			'price'      :self.price,
			'description':self.description,
			'calories'   :self.calories,
			'category'   :[obj.as_dict() for obj in self.category.all()],
			'imgURL'     :self.imgURL
			}
