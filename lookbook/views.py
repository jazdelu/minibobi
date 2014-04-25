from django.shortcuts import render_to_response
from lookbook.models import Lookbook
from django.template import RequestContext
# Create your views here.
def get_lookbooks(request):
	lookbooks = Lookbook.objects.all()
	return render_to_response('lookbook.html',{"lookbooks":lookbook},context_instance = RequestContext(request) )
