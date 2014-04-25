from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
LOCATION_CHOICES=(
		('homepage',_('Homepage')),
)

class Banner(models.Model):
	image = models.ImageField(upload_to = 'banner/',verbose_name = _('Image'))
	location = models.CharField(max_length = 128, choices = LOCATION_CHOICES, default = 'homepage')
	weight = models.IntegerField(verbose_name = _('Weight'),help_text = _('Matters the order of banners'))

	class Meta:
		verbose_name = _('Banner')
		verbose_name_plural = _('Banner')
		ordering = ['-weight']

	def __unicode__(self):
		return self.image.url