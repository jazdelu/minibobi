from django.conf.urls import patterns, url

from product import views

urlpatterns = patterns('',
    url(r'^$', views.get_products, name='product list'),
    url(r'^(?P<pid>\d+)/$', views.get_product_by_id, name ='get_product_by_id'),
    url(r'^(?P<s>.+)/$', views.get_products_by_category, name='get_products_by_category'),
)