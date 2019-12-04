from django.db import models
from accounts.models import User
from django.db import models

# Create your models here.

# class GeneralUser(models.Model):
# 	first_name = models.CharField(max_length=30)
# 	last_name = models.CharField(max_length=30)
# 	email = models.EmailField()
# 	password = models.CharField(max_length=30)
# 	state = models.CharField(max_length=30)
# 	city = models.CharField(max_length=30)
# 	zips = models.CharField(max_length=5)
# 	street = models.CharField(max_length=100)
# 	phone = models.CharField(max_length=12)
	
# 	def __str__(self):
# 		return self.first_name + " " + self.last_name + ", " + self.email

# 	def get_full_name(self):
# 		full_name = self.first_name + " " + self.last_name
# 		return self.full_name

class ProfessionalUser(models.Model):
	generalUserID = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=30, default='')
	description = models.CharField(max_length=200, default='')
	avg_rating = models.FloatField(default=0.0)
	isPlatinum = models.BooleanField(default=False)
	isDiamond = models.BooleanField(default=False)
	def __str__(self):
		return self.generalUserID.first_name + " " + self.generalUserID.last_name + " (" + self.generalUserID.email + ")"

class Service(models.Model):
	service = models.CharField(max_length=30)
	provider = models.ForeignKey(ProfessionalUser, on_delete=models.CASCADE)
	rate = models.FloatField()
	avg_rating = models.FloatField(default=0.0)
	description = models.CharField(max_length=200, default='')
	isHour = models.BooleanField(default=False)
	image = models.ImageField(upload_to='service_pics/',blank=True)
	def __str__(self):
		return self.service + ": " + self.provider.generalUserID.first_name + " " + self.provider.generalUserID.last_name + ", " + str(self.rate)

class Rating(models.Model):
	rater = models.ForeignKey(User, on_delete=models.CASCADE)
	provider = models.ForeignKey(ProfessionalUser, on_delete=models.CASCADE)
	service = models.ForeignKey(Service, on_delete=models.CASCADE, default=None)
	rating = models.IntegerField()
	description = models.CharField(max_length=200)
	verified = models.BooleanField(default=False)
	def __str__(self):
		return self.rater.first_name + ", " + self.provider.generalUserID.first_name + ", " + str(self.rating)

class Transaction(models.Model):
	buyer = models.ForeignKey(User, on_delete=models.CASCADE)
	provider = models.ForeignKey(ProfessionalUser, on_delete=models.CASCADE)
	service = models.ForeignKey(Service, on_delete=models.CASCADE)
	def __str__(self):
		return self.buyer.first_name + ", " + self.provider.generalUserID.first_name + ", " + self.service.service

class Advertisment(models.Model):
	provider = models.ForeignKey(ProfessionalUser, on_delete=models.CASCADE)
	ad = models.ImageField(upload_to='static/images/ads')

class UserImages(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='static/images/users')

# PostPicutre
class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')