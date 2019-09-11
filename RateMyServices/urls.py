from django.urls import path
from . import views

app_name = 'RateMyServices'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:professinaluser_id>&<int:generaluser_id>/', views.user_profile, name='user_profile'),
	path('<int:professinaluser_id>&<int:generaluser_id>/rate/', views.rate, name='rate')
]