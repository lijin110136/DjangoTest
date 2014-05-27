from django.conf.urls import patterns, include, url
from mysite.view import current_datetime
from student.views import search
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^myapp/', include("student.urls")),
    (r'^time/$', current_datetime),
    (r'^search/$', search),
)
