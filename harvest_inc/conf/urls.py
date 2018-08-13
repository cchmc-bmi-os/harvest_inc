import os, re
from django.conf.urls import url, patterns, include
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.template import add_to_builtins
from hub import views

# Get the views from the project
PROJECT = settings.ACTIVE_INSTANCE
site = __import__("{}.views".format(PROJECT))

add_to_builtins('avocado.templatetags.avocado_tags')

admin.autodiscover()

urlpatterns = patterns('',
    # Landing Page
    url(r'^$', 'harvest_inc.views.landing', name='landing'),
    url(r'^stats/', views.ibemc_stats, name='stats'),


    # Cilantro Pages
    url(r'^workspace/', TemplateView.as_view(template_name='index.html'), name='workspace'),
    url(r'^query/', TemplateView.as_view(template_name='index.html'), name='query'),
    url(r'^results/', TemplateView.as_view(template_name='index.html'), name='results'),

    # Serrano-compatible Endpoint
    url(r'^api/', include('serrano.urls')),

    # Administrative components
    url(r'^admin/', include(admin.site.urls)),

    # Site
    url(r'^data_summary/', site.views.data_summary, name='data_summary'),
)

# In production, these two locations must be served up statically
#urlpatterns += patterns('django.views.static',
#    url(r'^{0}(?P<path>.*)$'.format(re.escape(settings.MEDIA_URL.lstrip('/'))), 'serve', {
#        'document_root': settings.MEDIA_ROOT
#    }),
#    url(r'^{0}(?P<path>.*)$'.format(re.escape(settings.STATIC_URL.lstrip('/'))), 'serve', {
#        'document_root': settings.STATIC_ROOT
#    }),
#)
