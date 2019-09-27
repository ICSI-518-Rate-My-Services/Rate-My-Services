from django.shortcuts import *
from django.http import *
from .models import *
from django.template import *
from django.urls import *
from django.views import *
from django.contrib.auth import *


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
	gUser = GeneralUser.objects.get(id= 2) #id = 2 : for testing purposes
	context = {
		'pUsers': pUsers,
		'gUser': gUser
	}
	return render(request, 'RateMyServices/index.html', context)

def search(request, generaluser_id):
	services = Service.objects.all().filter(service=request.POST['search'])
	gUser = get_object_or_404(GeneralUser, id=generaluser_id)
	context = {
		'services': services,
		'gUser': gUser
	}
	return render(request, 'RateMyServices/results.html', context)

def signup(request):
	return render(request, 'RateMyServices/signuppage.html')

def login(request):
	return render(request, 'RateMyServices/loginpage.html')

def submit_login(request):
	#this is not working yet
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username = username, password = password)
	if user is not None:
		return HttpResponseRedirect(reverse('RateMyServices:index'))

def submit_logout(request):
	#this is not working properly either, will log out but redirect doesn't work
	logout(request)
	return render(request,'RateMyServices/index.html')
