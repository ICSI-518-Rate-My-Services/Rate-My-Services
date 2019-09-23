from django.contrib import admin
from .models import *

# Register your models here.
class ServiceInline(admin.TabularInline):
	model = Service

class ProfessionalUserAdmin(admin.ModelAdmin):
	inlines = [ServiceInline]

admin.site.register(GeneralUser)
admin.site.register(ProfessionalUser, ProfessionalUserAdmin)
admin.site.register(Service)
admin.site.register(Rating)