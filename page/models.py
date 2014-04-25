from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Page(models.Model):
	name = models.CharField(max_length = 128,verbose_name = _('Name'))
	content = models.TextField(verbose_name = _('Page Text Content'))

	class Meta:
		verbose_name = _('Page')
		verbose_name_plural = _('Page')

	def __unicode__(self):
		return self.name