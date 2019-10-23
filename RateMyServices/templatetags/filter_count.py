from RateMyServices.models import *
from django import template

register = template.Library()

@register.filter(name='filter_count')
def filter_count(gUser):
    return ProfessionalUser.objects.filter(generalUserID=gUser).count()