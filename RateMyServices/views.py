from django.shortcuts import *
from django.http import *
from .models import *
from django.template import *
from django.urls import *
from django.views import *

# Create your views here.
def user_profile(request, professionaluser_id, generaluser_id):
	pUser = get_object_or_404(ProfessionalUser, id=professionaluser_id)
	gUser = get_object_or_404(GeneralUser, id=generaluser_id)
	return render(request, 'RateMyServices/user_profile.html', {'pUser': pUser, 'gUser': gUser})

def rate(request, professionaluser_id, generaluser_id):
	pUser = get_object_or_404(ProfessionalUser, id=professionaluser_id)
	gUser = get_object_or_404(GeneralUser, id=generaluser_id)
	selected_rating = pUser.rating_set.create(rater=gUser, provider=pUser, rating=int(request.POST['rating']), description=request.POST['description'])
	return HttpResponseRedirect(reverse('RateMyServices:index'))

def index(request):
	pUsers = ProfessionalUser.objects.all()
	gUser = GeneralUser.objects.get(id=2) #for testing purposes
	context = {
		'pUsers': pUsers,
		'gUser': gUser
	}
	return render(request, 'RateMyServices/index.html', context)

def search(request, generaluser_id):
	gUser = get_object_or_404(GeneralUser, id=generaluser_id)
	services = Service.objects.all()

	if len(request.POST['search']) == 0:
		if len(request.POST['state']) != 0:
			filtered_services = list()
			for service in services:
				if service.provider.generalUserID.state == request.POST['state']:
					if len(request.POST['city']) != 0:
						if service.provider.generalUserID.city == request.POST['city']:
							filtered_services.append(service)

					else:
						filtered_services.append(service)

			services = filtered_services

	

	else:
		services = services.filter(service=request.POST['search'])

		if len(request.POST['state']) != 0:
			filtered_services = list()
			for service in services:
				if service.provider.generalUserID.state == request.POST['state']:
					if len(request.POST['city']) != 0:
						if service.provider.generalUserID.city == request.POST['city']:
							filtered_services.append(service)

					else:
						filtered_services.append(service)

			services = filtered_services

	context = {
		'services': services,
		'gUser': gUser
	}
	return render(request, 'RateMyServices/results.html', context)