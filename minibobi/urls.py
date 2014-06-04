from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'minibobi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^about/$','minibobi.views.about',name='about'),
    url(r'^notice/$','minibobi.views.notice',name='notice'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^product/',include('product.urls')),
    url(r'^sales/','product.views.get_sales',name='sales'),
    url(r'^lookbook/','lookbook.views.get_lookbooks',name='lookbook'),
    url(r'^cart/',include('cart.urls')),
    url(r'^order/',include('order.urls')),
    url(r'^contact/','minibobi.views.contact',name='contact'),
    #url(r'^lang/$', 'minibobi.views.set_language',name="set language"),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )
