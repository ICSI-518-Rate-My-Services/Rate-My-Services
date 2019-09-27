from django.urls import path
from . import views

app_name = 'RateMyServices'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:generaluser_id>/', views.search, name='search'),
	path('<int:professionaluser_id>&<int:generaluser_id>/', views.user_profile, name='user_profile'),
	path('<int:professionaluser_id>&<int:generaluser_id>/rate/', views.rate, name='rate'),
	path('login', views.login, name='login'),
	path('submit_login',views.submit_login, name='submit_login'),
	path('signup', views.signup, name='signup'),
	path('submit_logout', views.logout, name='submit_logout')
]