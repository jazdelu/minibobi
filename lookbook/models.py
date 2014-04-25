from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
class Lookbook(models.Model):
	name = models.CharField(max_length = 128,verbose_name = _('Name'))
	description = models.TextField(blank = True, null = True,verbose_name = _('Description'))

	class Meta:
		verbose_name = _('Lookbook')
		verbose_name_plural = _('Lookbook')

	def __unicode__(self):
		return self.name

class Image(models.Model):

	image = models.ImageField(upload_to='lookbook/', verbose_name = _('Image'))
	lookbook = models.ForeignKey(Lookbook)
	class Meta:
		verbose_name = _('Image')
		verbose_name_plural = _('Image')

	def __unicode__(self):
		return self.image.url

