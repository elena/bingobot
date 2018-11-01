from django.shortcuts import reverse
from django.views import generic
from django.utils.text import slugify
from scores.models import Event, Person, Poll
from scores.forms import PersonPollForm


class PollFormView(generic.edit.FormView):

    model = Poll
    template_name = 'form.html'
    form_class = PersonPollForm
    success_url = 'success/'

    def form_valid(self, form):

        event = Event.objects.filter(current=True)[0]
        name = form.cleaned_data.get('name')
        person = Person(name=name, slug=slugify(name))
        person.save()

        if 'bodies' in form.cleaned_data:
            poll_body = Poll(poll='body', person=person, event=event)
            poll_body.value = form.cleaned_data.get('bodies')
            poll_body.save()

        if 'boobs' in form.cleaned_data:
            poll_boob = Poll(poll='boob', person=person, event=event)
            poll_boob.value = form.cleaned_data.get('boobs')
            poll_boob.save()

        return super(PollFormView, self).form_valid(form)


class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'results.html'

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['body_list'] = self.get_object().poll_set.filter(poll='body')
        context['boob_list'] = self.get_object().poll_set.filter(poll='boob')
        return context
