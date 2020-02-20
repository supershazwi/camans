from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

def login(request, error=""):
    if request.method == 'POST':
    	email = request.POST['email']
    	password = request.POST['password']

    	user = authenticate(request, username=email, password=password)

    	if user is not None:
    		auth_login(request, user)
    		return redirect('adult/')
    	else:
    		context = {'error': 'Email and password entered do not match.'}
    		return render(request, 'login.html', context)

    else:
    	context = {'error': error}

    	return render(request, 'login.html', context)

@login_required(login_url='/login')
def logout(request):
	auth_logout(request)
	return redirect('login')