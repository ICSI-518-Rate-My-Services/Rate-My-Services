from django.urls import path
from . import views

app_name = 'RateMyServices'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:generaluser_id>/search', views.search, name='search'),
	path('<int:generaluser_id>/search/filter', views.filter, name='filter'),
	path('<int:professionaluser_id>&<int:generaluser_id>/', views.user_profile, name='user_profile'),
	path('<int:professionaluser_id>&<int:generaluser_id>/rate/', views.rate, name='rate'),
	path('general_profile/<int:generaluser_id>/', views.general_profile, name='general_profile'),
	path('professional_profile/<int:professionaluser_id>/', views.professional_profile, name='professional_profile'),
]