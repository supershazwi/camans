from django.urls import path

from . import views

app_name = 'adult'

urlpatterns = [
	path('privileges-and-permissions', views.privilegesandpermissionsindex, name='privilegesandpermissions.index'),
	path('workers/<int:workerid>', views.workersshow, name='workers.show'),
	path('workers/create', views.workerscreate, name='workers.create'),
	path('workers/check-twid', views.workerschecktwid, name='workers.checktwid'),
	path('profile/edit', views.profileedit, name='profile.edit'),
	path('profile', views.profile, name='profile.show'),
	path('dropdown-values', views.dropdownvalues, name='dropdownvalues.index'),
	path('', views.index, name='adult.index'),
]