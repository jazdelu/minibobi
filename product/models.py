# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
import datetime
# Create your models here.

class Collection(models.Model):
	name = models.CharField(max_length = 128,verbose_name=_('Name'))
	slug = models.SlugField(max_length = 128,verbose_name=_('Slug'),help_text = _('Displayed in the URL'))
	description = models.TextField(blank = True,verbose_name=_('Description'))
	pub_date = models.DateTimeField(auto_now_add = True,verbose_name=_('Publish Date'))
	last_modified = models.DateTimeField(auto_now = True,verbose_name=_('Last Modified Date'))

	class Meta:
		verbose_name = _('Collection')
		verbose_name_plural = _('Collection')

	def __unicode__(self):
		return self.name

class Color(models.Model):
	name = models.CharField(max_length = 128, verbose_name=_('Name'))
	color = models.CharField(max_length = 128, verbose_name =_('Color'))

	class Meta:
		verbose_name = _('Color')
		verbose_name_plural = _('Color')

	def __unicode__(self):
		return self.name

class Size(models.Model):
	size = models.CharField(max_length = 128, verbose_name = _('Size'))

	class Meta:
		verbose_name = _('Size')
		verbose_name_plural = _('Size')

	def __unicode__(self):
		return self.size


class Discount(models.Model):
	name = models.CharField(max_length = 128,verbose_name = _('Name'))
	discount = models.IntegerField(verbose_name=_('Discount'))
	icon = models.ImageField(upload_to = 'icon/',verbose_name = _('Icon'),blank = True)
	starttime = models.DateTimeField(verbose_name = _('Start Time'))
	endtime = models.DateTimeField(verbose_name = _('End Time'))

	class Meta:
		verbose_name = _('Discount')
		verbose_name_plural = ('Discount')

	def __unicode__(self):
		return self.name



class Category(MPTTModel):
	name = models.CharField(max_length = 128, verbose_name = _('Name'))
	slug = models.SlugField(max_length = 128, verbose_name = _('Slug'),unique = True,help_text = _('Displayed in the URL,should be unique.'))
	banner = models.ImageField(upload_to='banner/',verbose_name= _('Banner'),blank = True, null = True,help_text = _('Category page fix picture'))
	parent = TreeForeignKey('self',verbose_name = _('Parent'),null = True, blank = True, related_name = 'children')
	collection = models.ForeignKey(Collection,verbose_name = _('Collection'),default = 1)
	
	class Meta:
		verbose_name = _('Category')
		verbose_name_plural = _('Category')

	class MPTTMeta:
		ordering_insertion_by = ['name']

	def get_url(self):
		url= '/'+self.collection.slug+'/'
		c = self
		for c in c.get_ancestors(include_self = True):
			url += c.slug+'/'
		return url

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		super(Category, self).save(*args, **kwargs)
		Category.objects.rebuild()


class Product(models.Model):
	name = models.CharField(max_length=128, verbose_name = _('Name'))
	serial = models.CharField(max_length = 128,verbose_name = _('Serial'),blank = True,null = True)
	short_description = models.CharField(max_length = 128,verbose_name = _('Short Description'))
	collection = models.ForeignKey(Collection,related_name= 'products',default = 1)
	category = TreeForeignKey('product.Category',related_name = 'products')
	price = models.FloatField(verbose_name = _('Price'))
	stock = models.IntegerField(verbose_name = _('Stock'))
	color = models.ForeignKey(Color,related_name='products')
	size = models.ManyToManyField(Size,related_name = 'products')
	discount= models.ForeignKey(Discount,blank= True, null = True)
	long_description = models.TextField(blank = True,verbose_name = _('Long Description'))
	page_title = models.CharField(max_length=128,blank = True,verbose_name = _('Page Title'),help_text = _('Overwrites what is displayed at the top of your browser or in bookmarks'))
	description_meta = models.TextField(blank = True,verbose_name = _('Description Meta Tag'),help_text = _('A description of the page sometimes used by search engines.'))
	keywords_meta = models.TextField(blank = True,verbose_name = _('Keywords Meta Tag'),help_text = _('A list of comma separated keywords sometimes used by search engines.'))
	pub_date = models.DateTimeField(auto_now_add = True)
	last_modified = models.DateTimeField(auto_now = True)

	class Meta:
		verbose_name = _('Product')
		verbose_name_plural = _('Product')
		ordering =['-pub_date']

	def is_new(self):
		delta = datetime.datetime.now()-self.pub_date
		if delta.days<=3:
			return True
		else:
			return False

	def is_soldout(self):
		if self.stock == 0:
			return True
		else:
			return False

	def is_discount(self):
		if self.discount:
			if datetime.datetime.today()>self.discount.starttime and datetime.datetime.today()<self.discount.endtime:
				return True
		return False


	def get_real_price(self):
		p = self.price
		p = self.price *(1-self.discount.discount/100.0)
		return p


	def get_cover(self):
		image = ''
		if self.images.all():
			try:
				image = self.images.all().get(is_cover = True)
			except:
				image = self.images.all()[0]
		return image
		
	def __unicode__(self):
		return self.name


class Image(models.Model):
	product = models.ForeignKey(Product,related_name = "images")
	image = models.ImageField(upload_to='product/',verbose_name = _('Image'))
	is_cover = models.BooleanField(verbose_name = _('Set this image to product cover?'))
	class Meta:
		verbose_name = _('Image')
		verbose_name_plural = _('Image')

	def __unicode__(self):
		return self.image.url

	def thumb_small(self):
		return self.image.url+"-small"

	def thumb_middle(self):
		return self.image.url+"-middle"

	def thumb_big(self):
		return self.image.url+"-big"

	def thumb_list(self):
		return self.image.url+"-list"




