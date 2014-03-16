from django import forms
from scores.models import Person, Poll, Event


class PersonPollForm(forms.Form):

    name = forms.CharField()
    bodies = forms.CharField()
    boobs = forms.CharField()

    def clean(self, *args, **kwargs):
        clean_data = super(PersonPollForm, self).clean(*args, **kwargs)

        # check name unique
        name = clean_data.get('name')
        person = Person.objects.filter(name=name)
        if person:
            raise forms.ValidationError('Yo, that name is taken ~')

        # check event exists
        event = Event.objects.filter(current=True)
        if not event:
            raise forms.ValidationError("Hey! There aren't any current events. Go tell an organiser to activate an event.")
        return clean_data
