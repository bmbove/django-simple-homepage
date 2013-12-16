from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns(
    '',
    url(r'^$', views.BlogListView.as_view()),
    url(r'^(?P<slug>[^/]+)/$', views.PostDetailView.as_view()),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[^/]+)/$',
        views.PostDetailView.as_view()),
)
