from django.shortcuts import *
from django.http import *
from .models import *
from django.template import *
from django.urls import *
from django.views import *
from django.core import *

# for signup
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views import generic
from accounts.forms import RegisterForm
from accounts.models import User

#for Image Upload
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

#Edit User Details
from accounts.forms import UserChangeForm


# Create your views here.
def user_profile(request, professionaluser_id, generaluser_id):
	pUser = get_object_or_404(ProfessionalUser, id=professionaluser_id)
	gUser = get_object_or_404(User, id=generaluser_id)
	return render(request, 'RateMyServices/user_profile.html', {'pUser': pUser, 'gUser': gUser})

def rate(request):
	pUser = get_object_or_404(ProfessionalUser, id=request.POST['provider'])
	gUser = get_object_or_404(User, id=request.user.id)
	service = get_object_or_404(Service, id=request.POST['service'])

	if Transaction.objects.filter(buyer=gUser, provider=pUser, service=service).count() == 0:
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

	return HttpResponseRedirect(reverse('RateMyServices:professional_profile', args=(pUser.id,)))

def index(request): 
	pUsers = ProfessionalUser.objects.all()
	gUser = User.objects.get(id=1) #id = 2 : for testing purposes
	dummy_normalpuser= [
		{	'name': 'Musa Aghayev',
			'service': 'Software Developper',
			'location': 'Albany, NY',
			'description': 'I can offer ...',
			'rate': 4.8,
			'numOfRate': 180,
			'avgRates': 50,
			'isHour': False,
			'imgUrls': 'https://www.joc.com/sites/default/files/field_feature_image/Software%20development%20concept.jpg',
			'profilePic': '',
		},
		{	'name': 'Pankti Satishkumar Bardolia',
			'service': 'Software Developper',
			'location': 'Albany, NY',
			'description': 'I can offer ...',
			'rate': 4.8,
			'numOfRate': 151,
			'avgRates': 50,
			'isHour': False,
			'imgUrls': 'https://www.plm.automation.siemens.com/media/global/en/is-820219790-640x360_tcm27-49149.jpg',
			'profilePic': '',
		},
		{	'name': 'Jogn Bradburn',
			'service': 'Software Developper',
			'location': 'Albany, NY',
			'description': 'I can offer ...',
			'rate': 4.8,
			'numOfRate': 169,
			'avgRates': 50,
			'isHour': False,
			'imgUrls': 'https://cdn0.tnwcdn.com/wp-content/blogs.dir/1/files/2017/08/code-1839406_1920-796x531.jpg',
			'profilePic': '',
		},
		{	'name': 'Jerrison Chang-Sundin',
			'service': 'Logo Design',
			'location': 'Troy, NY',
			'description': 'I can offer ...',
			'rate': 4.5,
			'numOfRate': 34,
			'avgRates': 40,
			'isHour': False,
			'imgUrls': 'https://img.freepik.com/free-vector/golden-bird-logo-design_1195-336.jpg?size=338&ext=jpg',
			'profilePic': '',
		},
		{	'name': 'William Dahl',
			'service': 'Software Developper',
			'location': 'Altamont, NY',
			'description': 'I can offer ...',
			'rate': 4.8,
			'numOfRate': 180,
			'avgRates': 50,
			'isHour': False,
			'imgUrls': 'https://cdn.nextgov.com/media/img/upload/2018/12/04/120418softwaredevNG/860x394.jpg',
			'profilePic': '',
		},
	]
	dummy_premiumpuser=[
		{	'Urls': 'http://www.partnersinenglish.eu/uploads/1/2/0/0/120044573/skype-teaching_orig.jpeg',
			'Service': 'Online English Tutoring',
		},
		{	'Urls': 'https://www.cuelogic.com/wp-content/uploads/2019/05/Custom-Software-Development.jpg',
			'Service': 'Software Engineering',
		},
		{	'Urls': 'https://www.creativeboom.com/uploads/articles/a4/a4dbaac1edf2d4dd8409afe8d6be9e3879d020d2_1100.jpg',
			'Service': 'Freelance Illustration',
		},
	]

	context = {
		'pUsers': pUsers,
		'gUser': gUser,
		'dummyList': dummy_normalpuser,
		'dummyPremiumList': dummy_premiumpuser,
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
	filtered_services = list()

	if 'rating' in request.POST:
		rating_value = int(request.POST['rating'])
		for service in services:
			if service.avg_rating >= rating_value:
				filtered_services.append(service)

	elif 'rate' in request.POST:
		rate_value = int(request.POST['rate'])
		for service in services:
			if service.rate <= rate_value:
				filtered_services.append(service)

	services = filtered_services

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

def my_profile(request):
	editable = True
	if request.user.is_authenticated:
		if request.user.is_professional:
			puser_id = request.user.professionaluser_set.all()[0].id
			if request.method == 'POST':
				uploaded_file = request.FILES['profile_image']
				# fs = FileSystemStorage()
				# file_name = 'profile_pic' + str(request.user.id)
				# name = fs.save(file_name, uploaded_file)
				request.user.profile_image = uploaded_file
				request.user.save()
				# print(uploaded_file.name)
			return professional_profile(request, puser_id, editable)
		else:
			guser_id = request.user.id
			return general_profile(request, guser_id, editable)
	else:
		message = 'The action you try to do requires log in, please log in and precede.'
		context = {
			'message': message,
		}
		return HttpResponseRedirect(reverse('RateMyServices:login'))

def general_profile(request, generaluser_id, editable=False):
	gUser = get_object_or_404(User, id=generaluser_id)
	context = {
		'gUser': gUser,
		'editable': editable,
	}
	return render(request, 'RateMyServices/general_profile.html', context)

def professional_profile(request, professionaluser_id, editable=False):
	pUser = get_object_or_404(ProfessionalUser, id=professionaluser_id)
	nonEmptyReviewList = [] #a collection of nonempty review list for the professional user
	for i in pUser.service_set.all():
		tempList =[] #a list of nonempty review object for a single service
		for j in i.rating_set.exclude(description=''):
			tempList.append(j)
		nonEmptyReviewList.append(tempList)

	finalList = zip(pUser.service_set.all(),nonEmptyReviewList) 
	# e.g. [(serviceObj, nonEmptyreviewList for that service), ...]
	
	context = {
		'pUser': pUser,
		'editable': editable,
		'serviceWithReviews': finalList,
	}
	return render(request, 'RateMyServices/professional_profile.html', context)

def hire_service(request):
	pUser = get_object_or_404(ProfessionalUser, id=request.POST['provider'])
	gUser = get_object_or_404(User, id=request.user.id)
	service = get_object_or_404(Service, id=request.POST['service'])
	pUser.transaction_set.create(buyer=gUser, provider=pUser, service=service)
	return HttpResponseRedirect(reverse('RateMyServices:professional_profile', args=(pUser.id,)))

def addServicePage(request, generaluser_id):
	gUser = get_object_or_404(User, id=generaluser_id)
	return render(request,'RateMyServices/addServices.html', {'gUser': gUser})

def addService(request, generaluser_id):
	gUser = get_object_or_404(User, id=generaluser_id)
	pUser = get_object_or_404(ProfessionalUser, generalUserID=gUser)
	if request.POST['isHour'] == 'Yes':
		pUser.service_set.create(service=request.POST['service'], rate=request.POST['rate'], description=request.POST['description'], isHour=True)
	else:
		pUser.service_set.create(service=request.POST['service'], rate=request.POST['rate'], description=request.POST['description'], isHour=False)
		
	if request.POST['submit'] == 'service':
		return HttpResponseRedirect(reverse('RateMyServices:addServicePage', args=(gUser.id,)))
	else:
		return HttpResponseRedirect(reverse('RateMyServices:my_profile'))

def delete_service(request):
	service = get_object_or_404(Service, id=request.POST['service'])
	Service.objects.filter(id=service.id).delete()
	return HttpResponseRedirect(reverse('RateMyServices:my_profile'))


def becomeProUser(request, generaluser_id):
	gUser = get_object_or_404(User, id=generaluser_id)
	return render(request, 'RateMyServices/becomeProUser.html', {'gUser': gUser})


def addProUser(request, generaluser_id):
	gUser = get_object_or_404(User, id=generaluser_id)
	gUser.professional = True
	gUser.save()
	ProfessionalUser.objects.create(generalUserID=gUser, title=request.POST['title'], description=request.POST['description'])
	return render(request, 'RateMyServices/addServices.html', {'gUser': gUser})

# Old signup
'''
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('RateMyServices:login')
    template_name = 'registration/signup.html'
'''

# New signup
def signup_view(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		new_user = form.save()
		new_user = authenticate(username=form.cleaned_data['email'],
								password=form.cleaned_data['password1'],
								)
		login(request, new_user)
		return HttpResponseRedirect(reverse('RateMyServices:index'))
		
	context = {
		'form': form,
	}
	return render(request, 'RateMyServices/signuppage.html', context)

# Edit User Details
def editUser_view(request):
	form = UserChangeForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/RateMyServices/professional_profile.html')
		
	context = {
		'form': form,
	}
	return render(request, 'RateMyServices/edit_profile.html', context)
def update_user_info(request):
	gUser = get_object_or_404(User, id=request.user.id)
	if request.POST['email'] != '':
		gUser.email = request.POST['email']

	if request.POST['state'] != '':
		gUser.state = request.POST['state']
	
	if request.POST['city'] != '':
		gUser.city = request.POST['city']

	if request.POST['street'] != '':
		gUser.street = request.POST['street']
	
	if request.POST['zips'] != '':
		gUser.zips = request.POST['zips']

	gUser.save()
	return HttpResponseRedirect(reverse('RateMyServices:my_profile'))
