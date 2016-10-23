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
	return render_to_response("index.html",{"products":products,"banners":banners},context_instance = RequestContext(request))

def about(request):
	page=''
	try:
		page = Page.objects.get(name = 'about')
	except:
		pass

	return render_to_response("about.html",{"page":page},context_instance = RequestContext(request))

def set_language(request):
    next = request.REQUEST.get('next', None)
    if not next:
        next = request.META.get('HTTP_REFERER', None)
    if not next:
        next = '/'
    response = HttpResponseRedirect(next)
    if request.method == 'GET':
        lang_code = request.GET.get('language', None)
        if lang_code and translation.check_for_language(lang_code):
            if hasattr(request, 'session'):
                request.session['django_language'] = lang_code
            else:
                response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
            translation.activate(lang_code)
    return response


def notice(request):
	return render_to_response("notice.html",context_instance = RequestContext(request))

def legal(request):
	return render_to_response("legal.html",context_instance = RequestContext(request))


def contact(request):
	status = 0
	if request.POST:
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		content = request.POST.get('content')
		from_email = 'noreply@minibobi.com'
		text_content=''
		text_content += name+'('+email+')'+':  '
		text_content += content
		msg = EmailMultiAlternatives(subject, text_content, from_email, ['lushizhao@qq.com','info@minibobi.com',])
		msg.send()
		status = 1
		return render_to_response("contact.html",{ "status":status }, context_instance = RequestContext(request))
	else:
		return render_to_response("contact.html",{ "status":status }, context_instance = RequestContext(request))


