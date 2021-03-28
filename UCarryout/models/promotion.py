from django.db import models


class Promotion(models.Model):
	title = models.CharField(max_length = 150)
	description = models.CharField(max_length = 150)
	img_url = models.CharField(max_length = 150)
	bonus_points = models.IntegerField()
	requirements = models.CharField(max_length = 150)
	valid_date = models.DateTimeField()

	def as_dict(self):
		return {
			'id'          :self.id,
			'title'       :self.title,
			'description' :self.description,
			'bonus_points':self.bonus_points,
			'img_url'     :self.img_url,
			'requirements':self.requirements,
			'valid_date'  :self.valid_date.__str__(),

			}
