from django.conf.urls import patterns, url

from cart import views


urlpatterns = patterns('',
    url(r'^$', views.cart, name='cart'),
    url(r'^add/$',views.add,name = 'add'),
    url(r'^update/$',views.update,name = 'update'),
    url(r'^delete/(?P<iid>\d+)/$',views.delete,name = 'delete'),
)