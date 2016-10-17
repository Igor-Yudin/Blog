from django.db import models
from django.utils import timezone

class Post(models.Model):
	authors = models.ForeignKey('auth.User')
	title = models.CharField(max_length = 200)
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)
	content = models.TextField(default = "")


	#def __unicode__(self):
	#	return self.title

	#def get_absolute_url(self):
	#	return str.format("/blog/{0}/", self.id)

	def publish(self):
		self.published_data = timezon.now()
		self.save()

	def __str__(self):
		return self.title