from django.shortcuts import render_to_response
from django.template import RequestContext
from product.models import Product, Category,Collection
from django.http import Http404,HttpResponse

def get_products(request):
	products = Product.objects.all()
	return render_to_response('index.html',{'products':products},context_instance = RequestContext(request))

def get_products_by_category(request,s):
	slugs = filter(None,s.split('/'))
	category = ''
	products = []
	query_c = []
	try:
		category = Category.objects.get(slug = slugs[-1])
		for c in category.get_descendants(include_self=True):
			query_c.append(c)
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))
		raise Http404
	if category:
		products = Product.objects.filter(category__in = query_c)

	return render_to_response('list.html',{'products':products,'category':category}, context_instance=RequestContext(request))


def get_product_by_id(request,pid):
	product = ''
	try:
		product = Product.objects.get(id = pid)
	except Product.DoesNotExist:
		raise Http404
	return render_to_response('product.html',{'product':product},context_instance = RequestContext(request))



def get_products_by_collection(request,cid):
	products = []
	try:
		c = Collection.objects.get(id = cid)
		products = Product.objects.filter(collection = c)
	except Collection.DoesNotExist:
		raise Http404

	return render_to_response('list.html',{'products':product},context_instance = RequestContext(request))

def get_sales(request):
	products = Product.objects.exclude(discount = None)
	return render_to_response('list.html',{'products':product},context_instance = RequestContext(request))


