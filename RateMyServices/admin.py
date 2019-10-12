from django.contrib import admin
from .models import *
# from accounts.models import User

# Register your models here.
class ServiceInline(admin.TabularInline):
	model = Service
	list_display = ('provider','service','rate')

class ServiceAdmin(admin.ModelAdmin):
	model = Service
	list_display = ('provider','service','rate')

class RatingAdmin(admin.ModelAdmin):
	model = Rating

	# def get_rater(self, obj):
	# 	full_name = obj.rater.first_name + " " + obj.rater.last_name
	# 	return full_name + " ( " + obj.rater.email + ")"
	# get_rater.short_description = 'Rater'
	list_display = ('provider', 'rater' ,'rating','description')

class ProfessionalUserAdmin(admin.ModelAdmin):
	model = ProfessionalUser
	inlines = [ServiceInline]
	
	def get_full_name(self, obj):
		full_name = obj.generalUserID.first_name + " " + obj.generalUserID.last_name
		return full_name
	get_full_name.short_description = 'Full Name'

	def get_email(self, obj):
		return obj.generalUserID.email
	get_email.short_description = 'email'

	list_display = ('get_full_name','get_email','title')
	# search_fields = ('get_email','get_full_name')


# admin.site.register(GeneralUser, GeneralUserAdmin)
admin.site.register(ProfessionalUser, ProfessionalUserAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Rating, RatingAdmin)