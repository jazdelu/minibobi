from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
class Lookbook(models.Model):
	name = models.CharField(max_length = 128,verbose_name = _('Name'))
	description = models.TextField(blank = True, null = True,verbose_name = _('Description'))
	is_active = models.BooleanField(verbose_name = 'Publish this lookbook?',default = False)

	class Meta:
		verbose_name = _('Lookbook')
		verbose_name_plural = _('Lookbook')

	def __unicode__(self):
		return self.name

	def save(self,*args, **kwargs):
		if self.is_active:
			try:
				l = Lookbook.objects.get(is_active = True)
				l.is_active = False
				l.save()
			except:
				pass
		super(Lookbook, self).save(*args, **kwargs)

class Image(models.Model):

	image = models.ImageField(upload_to='lookbook/', verbose_name = _('Image'))
	lookbook = models.ForeignKey(Lookbook, related_name = 'images')
	class Meta:
		verbose_name = _('Image')
		verbose_name_plural = _('Image')

	def __unicode__(self):
		return self.image.url

