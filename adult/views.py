from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Table, Field, PermissionPrivilege, Worker
# from .decorators import unauthenticated_user

@login_required(login_url='/login')
def index(request):
    context = {}

    return render(request, 'index.html', context)

# workers
@login_required(login_url='/login')
def workerscreate(request):
	context = {}

	return render(request, 'workers/create.html', context)

@login_required(login_url='/login')
def workerschecktwid(request):
	context = {}

	return render(request, 'workers/checktwid.html', context)

@login_required(login_url='/login')
def workersshow(request, workerid):
	worker = Worker.objects.get(pk = workerid)
	context = {'worker': worker}

	return render(request, 'workers/show.html', context)

# privileges & permissions
@login_required(login_url='/login')
def privilegesandpermissionsindex(request):
	tables = Table.objects.all()
	context = {'tables': tables}

	return render(request, 'privilegesandpermissions/index.html', context)

# dropdown values
@login_required(login_url='/login')
def dropdownvalues(request):
	tables = Table.objects.all()
	context = {'tables': tables}

	return render(request, 'dropdownvalues/index.html', context)

# misc
@login_required(login_url='/login')
def profileedit(request):
	user = request.user
	context = {'user': user}

	return render(request, 'profile/edit.html', context)

@login_required(login_url='/login')
def profile(request):
	user = request.user
	context = {'user': user}

	return render(request, 'profile/show.html', context)