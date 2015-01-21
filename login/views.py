from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader


from django.contrib.auth.models import User

# Create your views here.
def jet(request):
    return render_to_response('t.html',
                              {},
                              context_instance=RequestContext(request))

def home(request):  #This is the view function to home
    return render_to_response('introindextry.html',
                              {},
                              context_instance=RequestContext(request))



def signup(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	email = request.POST.get('email')

	if User.objects.filter(username=username).exists():
		return HttpResponse('taken')

	User.objects.create_user(username, email, password)
	return HttpResponse('successful')




