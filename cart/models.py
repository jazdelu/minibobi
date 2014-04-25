from django.db import models
from product.models import Product,Size,Color
# Create your models here.
STATUS_CHOICES = (
		('on','on'),
		('off','off'),
)
class Cart(models.Model):

	session= models.CharField(max_length = 128,blank = True)
	status = models.CharField(max_length = 128,choices = STATUS_CHOICES,default = 'on')
	creation_date = models.DateTimeField(auto_now_add  = True)
	last_modified = models.DateTimeField(auto_now = True)

	def count(self):
		return self.items.all().count()

	def total(self):
		total = 0
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
