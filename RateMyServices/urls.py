from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls import url

app_name = 'RateMyServices'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:generaluser_id>/search', views.search, name='search'),
	path('<int:generaluser_id>/search/filter', views.filter, name='filter'),
	path('<int:professionaluser_id>&<int:generaluser_id>/', views.user_profile, name='user_profile'),
	path('<int:professionaluser_id>&<int:generaluser_id>/rate/', views.rate, name='rate'),
	# Default Login/Logout views until we make something more unique.
	###
	path('login', auth_views.LoginView.as_view(), name='login'),
	path('logout', auth_views.LogoutView.as_view(), name='logout'),
	#path('signup', views.SignUp.as_view(), name='signup'),
	path('signup', views.signup_view , name='signup_view'),
	###
	path('general_profile/<int:generaluser_id>/', views.general_profile, name='general_profile'),
	path('professional_profile/<int:professionaluser_id>/', views.professional_profile, name='professional_profile'),
	path('becomeProUser/<int:generaluser_id>/', views.becomeProUser, name='becomeProUser'),
	path('addProUser/<int:generaluser_id>/', views.addProUser, name="addProUser")
]