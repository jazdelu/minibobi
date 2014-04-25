from django.conf.urls import patterns, url

from order import views


urlpatterns = patterns('',
    url(r'^$', views.order, name='order'),
)