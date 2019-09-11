from django.shortcuts import *
from django.http import *
from .models import *
from django.template import *
from django.urls import *
from django.views import *

# Create your views here.
def user_profile(request, professinaluser_id, generaluser_id):
	pUser = get_object_or_404(ProfessinalUser, id=professinaluser_id)
	gUser = get_object_or_404(GeneralUser, id=generaluser_id)
	return render(request, 'RateMyServices/user_profile.html', {'pUser': pUser, 'gUser': gUser})

def rate(request, professinaluser_id, generaluser_id):
	pUser = get_object_or_404(ProfessinalUser, id=professinaluser_id)
	gUser = get_object_or_404(GeneralUser, id=generaluser_id)
	selected_rating = pUser.rating_set.create(rater=gUser, provider=pUser, rating=int(request.POST['rating']), description=request.POST['description'])
	return HttpResponseRedirect(reverse('RateMyServices:index'))

def index(request):
	pUsers = ProfessinalUser.objects.all()
	gUser = GeneralUser.objects.get(id=2) #for testing purposes
	context = {
		'pUsers': pUsers,
		'gUser': gUser
	}
	return render(request, 'RateMyServices/index.html', context)