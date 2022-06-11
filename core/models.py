from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evento(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	event_data = models.DateTimeField(verbose_name="Event data")
	creation_data = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	class Meta:
		db_table = "event" 
	
	def __str__(self):
		return self.title

	def get_event_data(self):
		return self.event_data.strftime('%m/%d/%Y %H:%M')
