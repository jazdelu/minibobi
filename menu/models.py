# -*- coding: utf-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from product.models import Category
from page.models import Page
# Create your models here.

MTYPE_CHOICE = (
	( '0', u'Category'),
	( '1', u'Page'),
	( '2', u'URL'),
)

MENU_CHOICE = (
	( '0', u'sidebar'),
	( '1', u'main'),
)

class MenuItem(MPTTModel):
	name = models.CharField(max_length = 128, verbose_name = u'Name')
	menu = models.CharField(max_length = 128, verbose_name = u'Location', choices = MENU_CHOICE, default = 0)
	parent = TreeForeignKey('self',verbose_name = u'Parent',null = True, blank = True)
	mtype = models.CharField(max_length = 128, choices = MTYPE_CHOICE, verbose_name = u'Menu Type')
	category = TreeForeignKey(Category,verbose_name = u'Category', blank = True, null = True,related_name = 'items')
	page = models.ForeignKey(Page, verbose_name = u'Page', blank = True, null = True,related_name = 'items')
	url = models.CharField(max_length = 512, verbose_name = u'URL', null = True , blank = True)
	weight = models.IntegerField(verbose_name = u'Weight', help_text = u'Order matters')


	class MPTTMeta:
		order_insertion_by = ['menu','-weight']

	class Meta:
		verbose_name = u'Menu'
		verbose_name_plural = u'Menu'

	def __unicode__(self):
		return self.name



	def save(self, *args, **kwargs):
		s = ''
		if self.mtype == '0':
			s+='/product/category/'+str(self.category.id)+'/'
			print s
			self.url = s
		if self.mtype == '1':
			s+='/page/'+str(self.page.id)+'/'
			print s
			self.url = s
		super(MenuItem, self).save(*args, **kwargs)
		MenuItem.objects.rebuild()