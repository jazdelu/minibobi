from django.shortcuts import render_to_response
from django.http import Http404,HttpResponseRedirect
from django.template import RequestContext
from django.utils import translation
from django.conf import settings
from product.models import Product
from banner.models import Banner
from page.models import Page

def home(request):
	products = Product.objects.all()
	banners = Banner.objects.exclude(location__isnull=False)
	return render_to_response("index.html",{"products":products,"banners":banners},context_instance = RequestContext(request))

def about(request):
	page=''
	try:
		page = Page.objects.get(name = 'about')
	except:
		pass

	return render_to_response("about.html",{"page":page},context_instance = RequestContext(request))



def lang(request):
	if request.GET:
		translation.activate('zh')
		response = HttpResponseRedirect('/')
		response.set_cookie(settings.LANGUAGE_COOKIE_NAME, 'zh')
	return response