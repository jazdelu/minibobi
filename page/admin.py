from django.contrib import admin
from page.models import Page
from modeltranslation.admin import TranslationAdmin

# Register your models here.
class PageAdmin(TranslationAdmin):
	list_display = ('name',)

admin.site.register(Page,PageAdmin)