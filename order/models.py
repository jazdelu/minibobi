from django.db import models
from cart.models import Cart
from django.utils.translation import ugettext_lazy as _
# Create your models here.
import datetime
STATUS_CHOICES=(
    (u'new',_('New')),
    (u'paid',_('Paid')),
    (u'deliver',_('Deliver')),
    (u'complete',_('Complete')),
    (u'discard',_('Discard')),
)

class Express(models.Model):
	name = models.CharField(max_length = 128,verbose_name = _('Name'))
	link = models.CharField(max_length = 128,verbose_name = _('Link'))

	class Meta:
		verbose_name = _('Express')
		verbose_name_plural = _('Express')

	def __unicode__(self):
		return self.name

def serial_generator():
	return datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')

class Order(models.Model):
	serial = models.CharField(max_length = 128,unique = True, verbose_name = _('Serial Number'))
	cart = models.ForeignKey(Cart)
	c_name = models.CharField(max_length = 128,verbose_name='Contact Name')
	c_phone = models.CharField(max_length = 128,verbose_name='Contact Phone')
	c_email = models.EmailField(max_length = 128,verbose_name='Contact Email')
	r_name = models.CharField(max_length = 128,verbose_name='Receiver Name')
	r_phone = models.CharField(max_length = 128,verbose_name='Receiver Phone')
	r_address = models.TextField(max_length = 128,verbose_name = 'Receiver Address')
	r_postcode = models.CharField(max_length = 128, blank = True, null = True,verbose_name = 'Receiver Postcode')
	markup = models.CharField(max_length = 1024,blank = True, null = True,verbose_name = 'Mark up')
	status = models.CharField(max_length = 128, choices = STATUS_CHOICES, default = 'new')
	express = models. CharField(max_length = 128,blank = True, null = True )
	enum = models.CharField(max_length = 128,blank = True, null = True)
	creation_date = models.DateTimeField(auto_now_add = True,verbose_name = _('Creation Date'))
	last_modified = models.DateTimeField(auto_now = True,verbose_name = _('Last Modified'))

	class Meta:
		verbose_name = _('Order')
		verbose_name_plural = ('Order')
		ordering = ['-creation_date']

	def __unicode__(self):
		return self.serial
