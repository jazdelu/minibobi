from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.db.models import Q
from order.models import Order
from order.forms import OrderForm
from product.models import Size
from cart.models import Cart
import datetime,random
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

def serial_generator():
	serial ='BB'
	serial+= datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	serial+= str(random.randint(100,999))

	return serial
# Create your views here.

def send_mail(order,request):
	html_content = render_to_string('email_template.html', {'order':order},context_instance=RequestContext(request))
	text_content = strip_tags(html_content)
	from_email = 'noreply@minibobi.com'
	subject = 'New Order:'+ order.serial
	msg = EmailMultiAlternatives(subject, text_content, from_email, ['sales@minibobi.com','lushizhao@qq.com',])
	msg.attach_alternative(html_content, "text/html")
	msg.send()

def order(request):
	if request.POST:
		form = OrderForm(request.POST)
		if form.is_valid():
			order = form.save(commit=False)
		else:
			return render_to_response("order.html",{"form":form},context_instance=RequestContext(request))
		try:
			cart = Cart.objects.get(id = request.session.get("cart"))
		except:
			return HttpResponse("Server Error")
		cart.status = 'off'
		cart.save()
		order.cart = cart
		order.delivery = cart.delivery
		del request.session['cart']
		order.serial = serial_generator()
		order.save()
		send_mail(order,request)
		for i in cart.items.all():
			i.size.stock-=i.quantity
			i.size.save()
		return render_to_response("thanks.html",{ "order":order }, context_instance=RequestContext(request))
	else:
		form = OrderForm()
		return render_to_response("order.html",{"form":form},context_instance=RequestContext(request))

def get_orders(request,key):

	orders = Order.objects.filter(
		Q(serial = key) | Q(phone = key ) | Q(name = key)
	)
	return render_to_response('order.html',{"orders":orders},context_instance=RequestContext(request))