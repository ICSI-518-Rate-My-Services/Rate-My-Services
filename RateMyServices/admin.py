from django.contrib import admin
from .models import *

# Register your models here.
class ServiceInline(admin.TabularInline):
	model = Service

class ProfessinalUserAdmin(admin.ModelAdmin):
	inlines = [ServiceInline]
	list_display = ('first_name', 'last_name', 'email')
	search_fields = ['first_name', 'Last_name', 'email']


admin.site.register(State)
admin.site.register(City)
admin.site.register(Zip)
admin.site.register(Vendor)
admin.site.register(ProfessinalUser, ProfessinalUserAdmin)
admin.site.register(GeneralUser)
admin.site.register(Service)
admin.site.register(Rating)