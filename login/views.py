from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader

# Create your views here.
def jet(request):
    return render_to_response('t.html',
                              {},
                              context_instance=RequestContext(request))



def home(request):
    return render_to_response('introindextry.html',
                              {},
                              context_instance=RequestContext(request))