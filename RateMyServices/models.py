from django.db import models

# Create your models here.
class GeneralUser(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField()
	password = models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	zips = models.CharField(max_length=5)
	street = models.CharField(max_length=100)
	phone = models.CharField(max_length=12)
	
	def __str__(self):
		return self.first_name + " " + self.last_name + ", " + self.email

class ProfessionalUser(models.Model):
	generalUserID = models.ForeignKey(GeneralUser, on_delete=models.CASCADE)
	title = models.CharField(max_length=30, default='')
	description = models.CharField(max_length=200, default='')
	avg_rating = models.FloatField(default=0.0)
	def __str__(self):
		return self.generalUserID.first_name + " " + self.generalUserID.last_name + ", " + self.generalUserID.email

class Service(models.Model):
	service = models.CharField(max_length=30)
	provider = models.ForeignKey(ProfessionalUser, on_delete=models.CASCADE)
	rate = models.FloatField()
	avg_rating = models.FloatField(default=0.0)
	description = models.CharField(max_length=200, default='')
	def __str__(self):
		return self.service + ": " + self.provider.generalUserID.first_name + " " + self.provider.generalUserID.last_name + ", " + self.rate

class Rating(models.Model):
	rater = models.ForeignKey(GeneralUser, on_delete=models.CASCADE)
	provider = models.ForeignKey(ProfessionalUser, on_delete=models.CASCADE)
	service = models.ForeignKey(Service, on_delete=models.CASCADE, default=None)
	rating = models.IntegerField()
	description = models.CharField(max_length=200)
	verified = models.BooleanField(default=False)
	def __str__(self):
		return self.rater.first_name + ", " + self.provider.generalUserID.first_name + ", " + str(self.rating)

class Transactions(models.Model):
	buyer = models.ForeignKey(GeneralUser, on_delete=models.CASCADE)
	provider = models.ForeignKey(ProfessionalUser, on_delete=models.CASCADE)
	service = models.ForeignKey(Service, on_delete=models.CASCADE)