# -*- coding: utf-8 -*-
from django.forms import *
from suit.widgets import *
class ColorAdminForm(ModelForm):
	class Media:
		js = ('http://minibobi.qiniudn.com/static/minibobi/js/jquery-1.8.3.min.js','http://minibobi.qiniudn.com/static/color/js/pick-a-color-1.1.8.min.js','http://minibobi.qiniudn.com/static/color/js/tinycolor-0.9.15.min.js','http://minibobi.qiniudn.com/static/minibobi/js/color.js')
		css ={
			"all": ('http://minibobi.qiniudn.com/static/color/css/pick-a-color-1.2.2.min.css','http://minibobi.qiniudn.com/static/minibobi/css/admin_extra.css')
		}
		

class DiscountAdminForm(ModelForm):
	class Meta:
		widgets = {
			'discount':EnclosedInput(append='%',attrs={'class':'input-mini'}),
			'starttime':SuitSplitDateTimeWidget,
			'endtime':SuitSplitDateTimeWidget,
		}


class ProductAdminForm(ModelForm):
	class Meta:
		widgets = {
			'stock':NumberInput(attrs={'class':'input-mini'}),
			'long_description':AutosizedTextarea,
			'price':EnclosedInput(prepend=u'¥',attrs={'class':'input-mini'})
		}