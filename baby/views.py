from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from adult.models import Table, Field, PermissionPrivilege, Worker
# from .decorators import unauthenticated_user

# @login_required(login_url='/login')
def index(request):
    context = {}

    return render(request, 'baby.index.html', context)

# @login_required(login_url='/login')
def workerssearch(request):
    context = {}

    return render(request, 'workers/baby.workerssearch.html', context)

# @login_required(login_url='/login')
def caseoperationsworkerssearch(request):
    context = {}

    return render(request, 'caseoperations/baby.caseoperationsworkerssearch.html', context)

# @login_required(login_url='/login')
def caseoperationsworkersshow(request, workerid):
	# worker = Worker.objects.get(pk = workerid)
	# context = {'worker': worker}

	context = {}

	return render(request, 'caseoperations/baby.caseoperationsworkersshow.html', context)