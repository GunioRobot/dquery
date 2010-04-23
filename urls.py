from django.conf.urls.defaults import *
from basic.views import *
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^toys/$', toys_list),
    (r'^toys/(?P<toy_id>\d+)$', toys_detail),
    (r'^toys/edit/(?P<toy_id>\d+)$', toys_edit),
    (r'^toys/add/$', toys_add),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
