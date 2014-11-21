from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from product.models import Category
# Create your models here.


class Banner(models.Model):
	image = models.ImageField(upload_to = 'banner/',verbose_name = _('Image'))
	location = TreeForeignKey(Category,blank = True, null = True, help_text="Leave blank for the homepage banners")
	weight = models.IntegerField(verbose_name = _('Weight'),help_text = _('Matters the order of banners'))
	url = models.URLField(verbose_name = _('URL'),blank = True, null = True,default = '#', help_text = 'The website you want to link')

	class Meta:
		verbose_name = _('Banner')
		verbose_name_plural = _('Banner')
		ordering = ['-weight']

	def __unicode__(self):
		return self.image.url