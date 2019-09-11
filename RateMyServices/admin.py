from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(State)
admin.site.register(City)
admin.site.register(Zip)
admin.site.register(Vendor)
admin.site.register(ProfessinalUser)
admin.site.register(GeneralUser)
admin.site.register(ServiceType)
admin.site.register(Service)
admin.site.register(Rating)