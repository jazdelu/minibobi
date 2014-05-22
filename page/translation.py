from modeltranslation.translator import translator, TranslationOptions
from page.models import *

class PageTranslationOptions(TranslationOptions):
	fields = ('content',)
	required_languages = ('en','zh-cn')

translator.register(Page,PageTranslationOptions)

