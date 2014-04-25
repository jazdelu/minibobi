from django.shortcuts import render_to_response
from cart.models import Cart, CartItem
from product.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import RequestContext
# Create your views here.

def cart(request):
	return render_to_response('cart.html', context_instance = RequestContext(request))

def add(request):
	if request.GET:
		cart = ''
		product = ''
		is_exist = False
		try:
			cart = Cart.objects.get(id = request.session.get("cart"))
			product = Product.objects.get(id = int(request.GET['pid']))
		except:
			raise Http404

		item = CartItem()
		item.product = product
		item.cart = cart
		item.quantity = int(request.GET['quantity'])
		item.color  = Color.objects.get(id=int(request.GET['color']))
		item.size = Size.objects.get(id=int(request.GET['size']))

		for i in CartItem.objects.filter(cart = cart).filter(product = product):
			if i.is_same_spec(item):
				i.quantity+=item.quantity
				i.save()
				break;
		else:
			item.save()

		return HttpResponseRedirect("/cart/")

def delete(request,iid):
	try:
		item = CartItem.objects.get(id = iid)
		item.delete()
	except:
		raise Http404

	return HttpResponseRedirect("/cart/")

def update(request):
	if request.GET:
		item = CartItem.objects.get(id = int(request.GET['iid']))
		item.quantity = int(request.GET['quantity'])
		item.save()
	return HttpResponseRedirect("/cart/")





