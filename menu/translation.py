from modeltranslation.translator import translator, TranslationOptions
from menu.models import *

class MenuItemTranslationOptions(TranslationOptions):
	fields = ('name',)
	required_languages = ('en','zh-cn')

translator.register(MenuItem,MenuItemTranslationOptions)