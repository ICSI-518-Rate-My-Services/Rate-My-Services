from django.shortcuts import *
from django.http import *
from .models import *
from django.template import *
from django.urls import *
from django.views import *
from django.core import *

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url

# Create your views here.
def user_profile(request, professionaluser_id, generaluser_id):
	pUser = get_object_or_404(ProfessionalUser, id=professionaluser_id)
	gUser = get_object_or_404(GeneralUser, id=generaluser_id)
	return render(request, 'RateMyServices/user_profile.html', {'pUser': pUser, 'gUser': gUser})

def rate(request, professionaluser_id, generaluser_id):
	pUser = get_object_or_404(ProfessionalUser, id=professionaluser_id)
	gUser = get_object_or_404(GeneralUser, id=generaluser_id)
	selected_rating = pUser.rating_set.create(rater=gUser, provider=pUser, rating=int(request.POST['rating']), description=request.POST['description'])

	if pUser.avg_rating == 0:
		pUser.avg_rating = float(request.POST['rating'])
		pUser.save()

	else:
		new_rating = (pUser.avg_rating + float(request.POST['rating']))/2.0
		pUser.avg_rating = new_rating
		pUser.save()

	return HttpResponseRedirect(reverse('RateMyServices:index'))

def index(request): 
	pUsers = ProfessionalUser.objects.all()
	gUser = GeneralUser.objects.get(id= 2) #id = 2 : for testing purposes
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

	json_services = serializers.serialize('json', services)

	request.session['services'] = json_services

	context = {
		'services': services,
		'gUser': gUser
	}
	return render(request, 'RateMyServices/results.html', context)

def filter(request, generaluser_id):
	gUser = get_object_or_404(GeneralUser, id=generaluser_id)
	serialize_list = request.session.get('services', None)
	deserialize_list = serializers.deserialize("json", serialize_list )
	services = [item.object for item in deserialize_list]

	#if 'rating' in request.POST:


	context = {
		'services': services,
		'gUser': gUser
	}
	return render(request, 'RateMyServices/results.html', context)

def signup(request):
	return render(request, 'RateMyServices/signuppage.html')

#def login(request):
#	return render(request, 'RateMyServices/login.html')


urlpatterns = [
    url(r'^login/$', auth_views.LoginView, name='login'),
	url(r'^logout/$', auth_views.LogoutView, {'next_page': '/RateMyServices'}, name='logout'),
    url(r'^admin/', admin.site.urls),
]

def general_profile(request, generaluser_id):
	gUser = get_object_or_404(GeneralUser, id=generaluser_id)

	return render(request, 'RateMyServices/general_profile.html', {'gUser': gUser})

def professional_profile(request, professionaluser_id):
	pUser = get_object_or_404(ProfessionalUser, id=professionaluser_id)
	return render(request, 'RateMyServices/professional_profile.html', {'pUser': pUser})
