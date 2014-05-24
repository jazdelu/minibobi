from django.shortcuts import render_to_response
from lookbook.models import Lookbook
from django.template import RequestContext
# Create your views here.
def get_lookbooks(request):
	lookbook = ''
	try:
		lookbook = Lookbook.objects.get(is_active = True)
	except:
		pass
	return render_to_response('lookbook.html',{"lookbooks":lookbooks},context_instance = RequestContext(request) )

