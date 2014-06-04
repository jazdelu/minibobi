from django.shortcuts import render_to_response
from django.http import Http404,HttpResponseRedirect
from django.template import RequestContext
from django.utils import translation
from django.conf import settings
from product.models import Product
from banner.models import Banner
from page.models import Page
from django.core.mail import EmailMultiAlternatives

def home(request):
	products = Product.objects.all()
	banners = Banner.objects.exclude(location__isnull=False)
	if request.user.is_authenticated():
		return render_to_response("index.html",{"products":products,"banners":banners},context_instance = RequestContext(request))
	else:
		return HttpResponseRedirect('/admin/')

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


def notice(request):
	return render_to_response("notice.html",context_instance = RequestContext(request))


def contact(request):
	status = 0
	if request.POST:
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		content = request.POST.get('content')
		from_email = 'robot@minibobi.com'
		text_content=''
		text_content += name+'('+email+')'+':  '
		text_content += content
		msg = EmailMultiAlternatives(subject, text_content, from_email, ['lushizhao@qq.com'])
		msg.send()
		status = 1
		return render_to_response("contact.html",{ "status":status }, context_instance = RequestContext(request))
	else:
		return render_to_response("contact.html",{ "status":status }, context_instance = RequestContext(request))