from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from product.models import *
from mptt.admin import MPTTModelAdmin
from suit.admin import SortableTabularInline
from product.forms import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class CollectionAdmin(admin.ModelAdmin):
	list_display = ('name','slug','pub_date_format')
	fields = ('name','slug','description')

	def pub_date_format(self,obj):
		return obj.pub_date.strftime("%Y-%m-%d %H:%M:%S")
	pub_date_format.admin_order_field = 'pub_date'
	pub_date_format.short_description = _('Publish Date')

admin.site.register(Collection,CollectionAdmin)

class ColorAdmin(admin.ModelAdmin):
	list_display = ('name','color')
	fields = ('name','color')
	form = ColorAdminForm

admin.site.register(Color,ColorAdmin)

class DiscountAdmin(admin.ModelAdmin):
	list_display = ('name','discount','icon','starttime_format','endtime_format')
	fields=('name','discount','icon','starttime','endtime')

	def starttime_format(self,obj):
		return obj.starttime.strftime("%Y-%m-%d %H:%M:%S")
	starttime_format.admin_order_field = 'starttime'
	starttime_format.short_description = _('Start Time')

	def endtime_format(self,obj):
		return obj.endtime.strftime("%Y-%m-%d %H:%M:%S")
	endtime_format.admin_order_field = 'endtime'
	endtime_format.short_description = _('End Time')
	form = DiscountAdminForm

admin.site.register(Discount,DiscountAdmin)
admin.site.register(Size)


class CategoryAdmin(MPTTModelAdmin):
	mptt_level_indent = 20
	search_fields = ('name','slug')
	list_display = ('name','slug','banner')
	fields=('name','slug','banner','collection','parent')
	list_display_links = ('name',)
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class ImageInline(admin.TabularInline):
	model = Image
	extra = 1


class ProductAdmin(TranslationAdmin):
	list_display = ('name','short_description','collection','category','discount','pub_date_format')
	fieldsets = (
		(_('Basic Information'), {
			'fields':('serial','stock','name','short_description','long_description','is_recommend')
		}),
		(_('Price Information'),{
			'fields':('price','discount')
		}),
		(_('Category Information'),{
			'classes':('suit-3column'),
			'fields':('category',),
		}),
		(_('Spec Information'),{
			'fields':('color','size')
		}),
		(_('SEO'),{
			'classes': ('collapse',),
			'fields':('page_title','description_meta','keywords_meta')
		}),
	)
	form = ProductAdminForm
	filter_horizontal = ('size',)

	inlines = (ImageInline,)

	def pub_date_format(self,obj):
		return obj.pub_date.strftime("%Y-%m-%d %H:%M:%S")
	pub_date_format.admin_order_field = 'pub_date'
	pub_date_format.short_description = _('Publish Date')

admin.site.register(Product,ProductAdmin)

