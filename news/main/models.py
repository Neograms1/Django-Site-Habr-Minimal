from django.db import models

# Create your models here.

class TipaChat(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	full_text = models.TextField()


	def __str__(self):
		return self.title
	

	class Meta:
		verbose_name = 'Данные'
		verbose_name_plural = 'Данные'