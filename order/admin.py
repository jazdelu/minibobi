#coding:utf8
from django.contrib import admin
from order.models import Express, Order
from django.utils.translation import ugettext_lazy as _
from django.forms import *
from suit.widgets import AutosizedTextarea
# Register your models here.
class ExpressAdmin(admin.ModelAdmin):
	list_display = ('name','link')
	fields = ('name','link')

admin.site.register(Express,ExpressAdmin)


class OrderAdminForm(ModelForm):
	class Media:
		js=('/static/minibobi/js/jquery-1.8.3.min.js',"/static/minibobi/js/admin_extra.js")

	class Meta:
		widgets = {
			'r_address':AutosizedTextarea,
		}


class OrderAdmin(admin.ModelAdmin):
	list_display = ('serial','c_name','c_phone','r_name','r_phone','status','creation_date_format')
	fieldsets = (
		(_('Basic Information'), {
			'fields':('serial','status','express','enum',)
		}),
		(_('Contact Information'),{
			'fields':('c_name','c_phone','c_email')
		}),
		(_('Receiver Information'),{
			'classes':('suit-3column'),
			'fields':('r_name','r_phone','r_address','r_postcode'),
		}),
		(_('Order Detail'),{
			'classes':('suit_3column'),
			'fields':('item_list',),
		}),
	)
	readonly_fields = ('serial','item_list')
	search_fields = ('serial','c_name','c_phone')
	list_filter=('status',)
	form = OrderAdminForm
	def creation_date_format(self,obj):
		return obj.creation_date.strftime("%Y-%m-%d %H:%M:%S")
	creation_date_format.admin_order_field = 'creation_date'
	creation_date_format.short_description = _('Creation Date')

	def item_list(self,obj):
		html  = u"<table class='table'>"
		html += u"<tr><th>name</th><th>quantity</th><th>amount</th><th>size</th><th>color</th></tr>"
		tr= ""
		for i in obj.cart.items.all():
			tr+=u"<tr>"
			tr+=u"<td>"+ i.product.name+"</td>"
			tr+=u"<td>"+  str(i.quantity) +"</td>"
			tr+=u"<td>"+  str(i.get_price())  +"</td>"
			tr+=u"<td>"+  i.size.size  +"</td>"
			tr+=u"<td>"+  i.color.name  +"</td>"
			tr+=u"</tr>"
		html+=tr
		html+=u"<tr><td colspan ='5'>total:"+str(obj.cart.total())+"</td></tr>"
		html+=u"</table>"
		return html
	item_list.short_description = _("Item List")
	item_list.allow_tags = True

admin.site.register(Order,OrderAdmin)