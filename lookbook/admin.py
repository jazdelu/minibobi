from django.contrib import admin
from lookbook.models import *
# Register your models here.

class ImageInline(admin.TabularInline):
	model = Image
	extra = 1

class LookbookAdmin(admin.ModelAdmin):
	list_display = ('name',)
	fields = ('name','description')

	inlines = (ImageInline,)

admin.site.register(Lookbook, LookbookAdmin)

