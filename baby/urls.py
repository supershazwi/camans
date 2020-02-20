from django.urls import path

from . import views

app_name = 'baby'

urlpatterns = [
	path('case-operations/<int:workerid>', views.caseoperationsworkersshow, name='baby.caseoperationsworkersshow'),
	path('case-operations', views.caseoperationsworkerssearch, name='baby.caseoperationsworkerssearch'),
	path('workers/search', views.workerssearch, name='baby.workerssearch'),
	path('', views.index, name='baby.index'),
]