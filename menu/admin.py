from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from menu.models import MenuItem, Menu
from django.forms import ModelForm
from suit.widgets import EnclosedInput
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class MenuAdmin(MPTTModelAdmin):
	mptt_level_indent = 20
	fields = ('name',)
	list_display = ('name',)

admin.site.register(Menu,MenuAdmin)

class MenuItemAdminForm(ModelForm):
	class Meta:
		model = MenuItem

	class Media:
		js = ('/static/minibobi/js/menu_admin.js',)


class MenuItemAdmin(MPTTModelAdmin,TranslationAdmin):
	mptt_level_indent = 20
	fields = ('name','menu','parent','mtype','category','page','url','weight',)
	list_display = ('name','menu','mtype','url','weight',)
	list_display_links = ('name',)
	form = MenuItemAdminForm

admin.site.register(MenuItem,MenuItemAdmin)

