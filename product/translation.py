from modeltranslation.translator import translator, TranslationOptions
from product.models import *

class ProductTranslationOptions(TranslationOptions):
	fields = ('name','short_description','long_description','page_title','description_meta','keywords_meta')
	required_languages = ('en','zh-cn')

translator.register(Product,ProductTranslationOptions)

class ColorTranslationOptions(TranslationOptions):
	fields = ('name',)
	required_languages = ('en','zh-cn')
