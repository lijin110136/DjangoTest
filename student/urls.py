from django.conf.urls import patterns, url

urlpatterns = patterns('student.views',
    url(r'^student/list$', "list"),

)

