from django.contrib import admin
from lookbook.models import *
# Register your models here.

class ImageInline(admin.TabularInline):
	model = Image
	extra = 1

class LookbookAdmin(admin.ModelAdmin):
	list_display = ('name','is_active')
	fields = ('name','description',"is_active")

	inlines = (ImageInline,)

admin.site.register(Lookbook, LookbookAdmin)

