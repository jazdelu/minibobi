from django.contrib import admin
from banner.models import Banner
from django.forms import ModelForm
from suit.widgets import NumberInput
# Register your models here.

class BannerAdminForm(ModelForm):
	class Meta:
		widgets = {
			'weight':NumberInput(attrs={'class':'input-mini'}),
		}

class BannerAdmin(admin.ModelAdmin):
	list_display=("image","location","weight")
	form  = BannerAdminForm


admin.site.register(Banner, BannerAdmin)