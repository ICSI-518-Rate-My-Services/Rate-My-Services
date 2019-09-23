from django.urls import path
from . import views

app_name = 'RateMyServices'
urlpatterns = [
	path('', views.index, name='index'),
	path('search/', views.search, name='search'),
	path('<int:professionaluser_id>&<int:generaluser_id>/', views.user_profile, name='user_profile'),
	path('<int:professionaluser_id>&<int:generaluser_id>/rate/', views.rate, name='rate')
]