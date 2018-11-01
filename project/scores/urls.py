from django.urls import path
from django.views import generic
from scores import views


urlpatterns = [

    path('',
         views.PollFormView.as_view(),
         name='person_poll'),

    path('success/',
         generic.TemplateView.as_view(template_name="success.html"),
         name='person_poll_success'),

    path('results/<slug:slug>/',
         views.EventDetailView.as_view(),
         name='event_detail_view'),

]
