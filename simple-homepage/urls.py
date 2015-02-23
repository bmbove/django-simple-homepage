from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from pages.views import PageDetailView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, }),
    url(r'^(?P<slug>.*)/$', PageDetailView.as_view()),
    url(r'^$', PageDetailView.as_view(), {'slug': 'home'})
)
