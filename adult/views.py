from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import connection

from .models import Table, Field, PermissionPrivilege, Worker, Twid
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
	subsidiary_tables_rows = []

	subsidiary_tables = Table.objects.all().filter(subsidiary_to = 'workers')
	for subsidiary_table in subsidiary_tables:
		subsidiary_table_row_dictionary = {}
		field_values = []
		cursor = connection.cursor()

		query = "SELECT label, table_index, name FROM public.adult_field WHERE table_id = %s" % subsidiary_table.id
		cursor.execute(query) 
		
		subsidiary_table_row_dictionary['columns'] = cursor.fetchall()
		for (label, table_index, name) in subsidiary_table_row_dictionary['columns']:
			field_values.append(name)
		field_values = ','.join(field_values) 

		query = "SELECT %s FROM public.adult_%s WHERE worker_id = %s" % (field_values, subsidiary_table.database_table, workerid)
		cursor.execute(query) 

		subsidiary_table_row_dictionary['key'] = subsidiary_table.name
		subsidiary_table_row_dictionary['values'] = cursor.fetchall()
		subsidiary_table_row_dictionary['count'] = len(subsidiary_table_row_dictionary['values'])

		subsidiary_tables_rows.append(subsidiary_table_row_dictionary)

	context = {'worker': worker, 'subsidiary_tables': subsidiary_tables, 'subsidiary_tables_rows': subsidiary_tables_rows}

	return render(request, 'workers/show.html', context)

@login_required(login_url='/login')
def workersedit(request, workerid):
	worker = Worker.objects.get(pk = workerid)
	context = {'worker': worker}

	return render(request, 'workers/edit.html', context)

@login_required(login_url='/login')
def workerssubsidiarycreate(request, workerid, workersubsidiaryurlstring):
	worker = Worker.objects.get(pk = workerid)
	subsidiary_table = Table.objects.get(url_string = workersubsidiaryurlstring)
	context = {'worker': worker, 'subsidiary_table': subsidiary_table}

	return render(request, 'workers/subsidiaries/create.html', context)

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