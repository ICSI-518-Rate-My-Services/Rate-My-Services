from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'RateMyServices'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:generaluser_id>/search', views.search, name='search'),
	path('<int:generaluser_id>/search/filter', views.filter, name='filter'),
	path('<int:professionaluser_id>&<int:generaluser_id>/', views.user_profile, name='user_profile'),
	path('<int:professionaluser_id>&<int:generaluser_id>/rate/', views.rate, name='rate'),
	# userprofile
	path('login', auth_views.LoginView.as_view(), name='login'),
	path('logout', auth_views.LogoutView.as_view(), name='logout'),
	path('signup', views.signup_view , name='signup_view'),
	path('MyProfile', views.my_profile, name='my_profile'),
	path('general_profile/<int:generaluser_id>/', views.general_profile, name='general_profile'),
	path('professional_profile/<int:professionaluser_id>/', views.professional_profile, name='professional_profile'),

	path('becomeProUser/<int:generaluser_id>/', views.becomeProUser, name='becomeProUser'),
	path('addProUser/<int:generaluser_id>/', views.addProUser, name="addProUser"),
	path('addService/<int:generaluser_id>/', views.addService, name='addService'),
	path('addServicePage/<int:generaluser_id>/', views.addServicePage, name='addServicePage')
]