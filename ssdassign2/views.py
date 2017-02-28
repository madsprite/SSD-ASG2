from django.shortcuts import render
from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext
from ssdassign2.models import Users


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def profile(request):
	#need to know who currently logged in
	current_user = request.Users
	current_username = current_user.username
	
	profile_info=Users.objects.filter(username=current_username)

	profile_data= {
		"profile_detail" : profile_info
	}
	print profile_data
    return render_to_response('users/profile.html', profile_data, context_instance=RequestContext(request))

def profile-edit(request):
    return render(request, 'users/profile-edit.html')

def avatar(request):
    return render(request, 'users/avatar.html')

def avatar-edit(request):
    return render(request, 'users/avatar-edit.html')