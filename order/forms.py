from django.forms import ModelForm
from order.models import Order
class OrderForm(ModelForm):

	class Meta:
		model = Order
		fields = ['c_name','c_phone','c_email','r_name','r_phone','r_address','r_postcode','markup','delivery']
