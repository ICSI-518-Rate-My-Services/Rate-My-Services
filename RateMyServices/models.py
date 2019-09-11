from django.db import models

# Create your models here.
class State(models.Model):
	state = models.CharField(max_length=30)
	def __str__(self):
		return self.state

class City(models.Model):
	city = models.CharField(max_length=30)
	state = models.ForeignKey(State, on_delete=models.CASCADE)	
	def __str__(self):
		return self.city + ", " + self.state.state

class Zip(models.Model):
	zips = models.CharField(max_length=5)
	def __str__(self):
		return self.zips

class Vendor(models.Model):
	vendor = models.CharField(max_length=30)
	def __str__(self):
		return self.vendor

class ProfessinalUser(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField()
	password = models.CharField(max_length=30)
	title = models.CharField(max_length=30)
	description = models.CharField(max_length=100)
	state = models.ForeignKey(State, on_delete=models.CASCADE)
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	zips = models.ForeignKey(Zip, on_delete=models.CASCADE)
	street = models.CharField(max_length=100)
	phone = models.CharField(max_length=12)
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
	def __str__(self):
		return self.first_name + ", " + self.last_name + ", " + self.email

class GeneralUser(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField()
	password = models.CharField(max_length=30)
	state = models.ForeignKey(State, on_delete=models.CASCADE)
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	zips = models.ForeignKey(Zip, on_delete=models.CASCADE)
	street = models.CharField(max_length=100)
	phone = models.CharField(max_length=12)
	def __str__(self):
		return self.first_name + ", " + self.last_name + ", " + self.email

class ServiceType(models.Model):
	service_type = models.CharField(max_length=30)
	def __str__(self):
		return self.service_type

class Service(models.Model):
	service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
	provider = models.ForeignKey(ProfessinalUser, on_delete=models.CASCADE)
	rate = models.CharField(max_length=6)
	def __str__(self):
		return self.service_type.service_type + ", " + self.provider.first_name + ", " + self.rate

class Rating(models.Model):
	rater = models.ForeignKey(GeneralUser, on_delete=models.CASCADE)
	provider = models.ForeignKey(ProfessinalUser, on_delete=models.CASCADE)
	rating = models.IntegerField()
	description = models.CharField(max_length=100)
	def __str__(self):
		return self.rater.first_name + ", " + self.provider.first_name + ", " + self.rating