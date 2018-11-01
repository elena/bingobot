from django.contrib import admin
from scores.models import Event, Person, EventPoll, Poll


class EventPollInline(admin.TabularInline):
    model = EventPoll
    extra = 0


class EventAdmin(admin.ModelAdmin):
    inlines = [EventPollInline]

admin.site.register(Event, EventAdmin)


class PersonPollInline(admin.TabularInline):
    model = Poll
    extra = 0


class PersonAdmin(admin.ModelAdmin):
    inlines = [PersonPollInline]

admin.site.register(Person, PersonAdmin)
