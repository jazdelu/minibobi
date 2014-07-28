from django.shortcuts import render_to_response
from django.template import RequestContext
from product.models import Product, Category,Collection
from banner.models import Banner
from django.http import Http404,HttpResponse
from django.db.models import Q

def get_products(request):
	products = []
	if request.GET:
		if request.GET['s'] != '':
			s = request.GET['s']
			products = Product.objects.filter(
					Q(name_en__contains=s) | Q(name_zh_cn__contains=s) | Q(short_description_en__contains=s) | Q(short_description_zh_cn__contains=s) 
				)
		else:
			products = Product.objects.all()
	else:
		products = Product.objects.all()
	return render_to_response('index.html',{'products':products},context_instance = RequestContext(request))

def get_products_by_category(request,s):
	slugs = filter(None,s.split('/'))
	category = ''
	products = []
	query_c = []
	banners = []
	try:
		category = Category.objects.get(slug = slugs[-1])
		for c in category.get_descendants(include_self=True):
			query_c.append(c)
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))
		raise Http404
	if category:
		products = Product.objects.filter(category__in = query_c)
		banners = Banner.objects.filter(location = category)

	return render_to_response('list.html',{'products':products,'category':category,'banners':banners}, context_instance=RequestContext(request))


def get_product_by_id(request,pid):
	product = ''
	try:
		product = Product.objects.get(id = pid)
	except Product.DoesNotExist:
		raise Http404

	products = Product.objects.filter(is_recommend = True)
	return render_to_response('product.html',{'product':product, 'products':products},context_instance = RequestContext(request))



def get_products_by_collection(request,cid):
	products = []
	try:
		c = Collection.objects.get(id = cid)
		products = Product.objects.filter(collection = c)
	except Collection.DoesNotExist:
		raise Http404

	return render_to_response('list.html',{'products':product},context_instance = RequestContext(request))

def get_sales(request):
	products = Product.objects.exclude(discount__isnull = True)
	return render_to_response('list.html',{'products':products},context_instance = RequestContext(request))




