from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

urlpatterns = patterns('',
    url(r'^pair/+$', 'latch.views.pair', name='latch_pair'),
    url(r'^unpair/+$', 'latch.views.unpair', name='latch_unpair'),
    # This can be disabled if you want to hide the status for your application. 
    url(r'^status/+$', 'latch.views.status', name='latch_status'),
)
