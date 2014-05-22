from django.db import models
from product.models import Product,Size,Color
# Create your models here.
STATUS_CHOICES = (
		('on','on'),
		('off','off'),
)

DELIVERY_CHOICES = (
		('0','0'),
		('50','50'),
)

class Cart(models.Model):

	session= models.CharField(max_length = 128,blank = True)
	status = models.CharField(max_length = 128,choices = STATUS_CHOICES)
	delivery = models.CharField(max_length = 128,choices = DELIVERY_CHOICES,default="0")
	creation_date = models.DateTimeField(auto_now_add  = True)
	last_modified = models.DateTimeField(auto_now = True)

	def count(self):
		return self.items.all().count()

	def total(self):
		total = 0
		if self.delivery != '0':
			total+=int(self.delivery)
		for i in self.items.all():
			total+=i.product.price*i.quantity
		return total



class CartItem(models.Model):
	cart = models.ForeignKey(Cart,related_name = 'items')
	product = models.ForeignKey(Product)
	color = models.ForeignKey(Color)
	size = models.ForeignKey(Size)
	quantity = models.IntegerField()

	def get_price(self):
		return self.product.price * self.quantity

	def is_same_spec(self,i):
		if self.color == i.color and self.size ==i.size :
			return True
		else:
			return False
