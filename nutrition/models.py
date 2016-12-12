from django.db import models
from django.utils import timezone

from core.models import RootModel

class CalorieInput(RootModel):
	#user = models.ForeignKey(UserProfile)
	date = models.DateField(default=timezone.now)
	code = models.CharField(max_length=10, null=True)
	name = models.CharField(max_length=100, null=True)
	unit = models.CharField(max_length=10, null=True)
	quantity = models.FloatField(null=False, default=0)
	calorie = models.FloatField(null=False, default=0)
	nutrients = models.TextField(null=True)

	class Meta:
		ordering = ['date']
		verbose_name = 'calorieInput'
		verbose_name_plural = 'calorieInputList'

	@property
	def full_name(self):
		return '%s - %s' % (self.code, self.name)

	def __str__(self):
		result = [('%s=%s' % (key, value)) for key, value in self.__dict__.items()]
		return result.__str__()


class CalorieOutput(RootModel):
	#user = models.ForeignKey(UserProfile)
	date = models.DateField(default=timezone.now)
	code = models.CharField(max_length=10, null=True)
	name = models.CharField(max_length=100, null=True)
	unit = models.CharField(max_length=10, null=True)
	quantity = models.FloatField(null=False, default=0)
	calorie = models.FloatField(null=False, default=0)

	class Meta:
		ordering = ['date']
		verbose_name = 'calorieInput'
		verbose_name_plural = 'calorieInputList'

	@property
	def full_name(self):
		return '%s - %s' % (self.code, self.name)

	def __str__(self):
		result = [('%s=%s' % (key, value)) for key, value in self.__dict__.items()]
		return result.__str__()