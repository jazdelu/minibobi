from django.conf.urls import patterns, url

from lookbook import views


urlpatterns = patterns('',
    url(r'^$', views.get_products, name='lookbook'),
)