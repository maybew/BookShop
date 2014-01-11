from shop import settings
from django.conf.urls import patterns, include, url
from account.views import signup, login, logout, update_profile, profile, set_password
from item.views import index, search, item
from cart.views import add_to_cart
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shop.views.home', name='home'),
    # url(r'^shop/', include('shop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),

   
    url(r'^$', index),
    url(r'^index/$', index),
    url(r'^search/$', search),
    url(r'^item/(\d+)/$', item),
    
    url(r'^add_to_cart/$', add_to_cart),
    
    url(r'^signup/$', signup),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^profile/$', profile),
    url(r'^profile/update/$', update_profile),
    url(r'^profile/password/$', set_password),
    url(r'^search/$', update_profile),
)
