from django.shortcuts import *
from django.http import *
from .models import *
from django.template import *
from django.urls import *
from django.views import *
from django.core import *

# for signup
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from accounts.forms import RegisterForm
from accounts.models import User


# Create your views here.
def user_profile(request, professionaluser_id, generaluser_id):
	pUser = get_object_or_404(ProfessionalUser, id=professionaluser_id)
	gUser = get_object_or_404(User, id=generaluser_id)
	return render(request, 'RateMyServices/user_profile.html', {'pUser': pUser, 'gUser': gUser})

def rate(request, professionaluser_id, generaluser_id, service_id):
	pUser = get_object_or_404(ProfessionalUser, id=professionaluser_id)
	gUser = get_object_or_404(User, id=generaluser_id)
	service = get_object_or_404(Service, id=service_id)

	if Transactions.objects.filter(buyer=gUser, provider=pUser, service=search).count() == 0:
		verified = False

	else:
		verified = True

	pUser.rating_set.create(rater=gUser, provider=pUser, service=service, rating=int(request.POST['rating']), description=request.POST['description'], verified=verified)

	if pUser.avg_rating == 0:
		pUser.avg_rating = float(request.POST['rating'])
		pUser.save()

	else:
		new_rating = (pUser.avg_rating + float(request.POST['rating']))/2.0
		pUser.avg_rating = new_rating
		pUser.save()

	if service.avg_rating == 0:
		service.avg_rating = float(request.POST['rating'])
		service.save()
	
	else:
		new_rating = (service.avg_rating + float(request.POST['rating']))/2.0
		service.avg_rating = new_rating
		service.save()

	return HttpResponseRedirect(reverse('RateMyServices:index'))

def index(request): 
	pUsers = ProfessionalUser.objects.all()
	gUser = User.objects.get(id=1) #id = 2 : for testing purposes
	context = {
		'pUsers': pUsers,
		'gUser': gUser
	}
	return render(request, 'RateMyServices/index.html', context)

def search(request, generaluser_id):
	gUser = get_object_or_404(User, id=generaluser_id)
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
	gUser = get_object_or_404(User, id=generaluser_id)
	serialize_list = request.session.get('services', None)
	deserialize_list = serializers.deserialize("json", serialize_list )
	services = [item.object for item in deserialize_list]

	#if 'rating' in request.POST:


	context = {
		'services': services,
		'gUser': gUser
	}
	return render(request, 'RateMyServices/results.html', context)

 
# Unused for now
'''
def login(request):
	return render(request, 'registration/login.html')
'''

def general_profile(request, generaluser_id):
	gUser = get_object_or_404(User, id=generaluser_id)

	return render(request, 'RateMyServices/general_profile.html', {'gUser': gUser})

def professional_profile(request, professionaluser_id):
	pUser = get_object_or_404(ProfessionalUser, id=professionaluser_id)
	return render(request, 'RateMyServices/professional_profile.html', {'pUser': pUser})

def hire_service(request, professionaluser_id, generaluser_id, service_id):
	pUser = get_object_or_404(ProfessionalUser, id=professionaluser_id)
	gUser = get_object_or_404(User, id=generaluser_id)
	service = get_object_or_404(Service, id=service_id)
	pUser.transaction_set.create(buyer=gUser, provider=pUser, service=service)

def addServicePage(request, generaluser_id):
	gUser = get_object_or_404(User, id=generaluser_id)
	return render(request,'RateMyServices/addServices.html', {'gUser': gUser})

def addService(request, generaluser_id):
	gUser = get_object_or_404(User, id=generaluser_id)
	pUser = get_object_or_404(ProfessionalUser, generalUserID=gUser)
	pUser.service_set.create(service=request.POST['service'], rate=request.POST['rate'], description=request.POST['description'])
	if request.POST['submit'] == 'service':
		return render(request,'RateMyServices/addServices.html', {'gUser': gUser})
	else:
		return render(request, 'RateMyServices/professional_profile.html', {'pUser': pUser})

def becomeProUser(request, generaluser_id):
	gUser = get_object_or_404(User, id=generaluser_id)
	return render(request, 'RateMyServices/becomeProUser.html', {'gUser': gUser})


def addProUser(request, generaluser_id):
	gUser = get_object_or_404(User, id=generaluser_id)
	gUser.professional = True
	gUser.save()
	pUser = ProfessionalUser.objects.create(generalUserID=gUser, title=request.POST['title'], description=request.POST['description'])
	return render(request, 'RateMyServices/addServices.html', {'pUser': pUser})

# Old signup
'''
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('RateMyServices:login')
    template_name = 'registration/signup.html'
'''

# New signup
def signup_view(request):
	#next = request.GET.get('next')
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		form.save()
		
	context = {
		'form': form,
	}
	return render(request, 'RateMyServices/signuppage.html', context)
