from django.db.models import Manager


class UserManager(Manager):

	def valid_user(self, username):
		current_user = self.objects.get(username = username)

		if current_user is None:
			return False
		else:
			return True
