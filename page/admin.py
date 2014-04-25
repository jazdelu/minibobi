from django.contrib import admin
from page.models import Page
# Register your models here.
class PageAdmin(admin.ModelAdmin):
	list_display = ('name',)

admin.site.register(Page,PageAdmin)