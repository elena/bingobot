from django.conf.urls import patterns, url
from django.views import generic
from scores import views


urlpatterns = patterns('',

    url(r'^$', views.PollFormView.as_view(), name='person_poll'),

    url(r'^success$', generic.TemplateView.as_view(template_name="success.html"),
                      name='person_poll_success'),
)
