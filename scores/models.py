from django.db import models
from django.utils.html import urlize


POLL_CHOICES = (
    ('body', 'bodies'),
    ('boob', 'boobies'),
)


class Event(models.Model):
    date = None
    current = models.BooleanField(default=False)
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = urlize(self.name)
        super(Event, self).save(*args, **kwargs)



class EventPoll(models.Model):
    event = models.ForeignKey('scores.Event')
    poll = models.CharField(max_length=256, choices=POLL_CHOICES)
    value = models.IntegerField()


class Person(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)

    def __str__(self):
        return self.name


class Poll(models.Model):

    event = models.ForeignKey('scores.Event')
    person = models.ForeignKey('scores.Person')
    poll = models.CharField(max_length=256, choices=POLL_CHOICES)
    value = models.IntegerField()
    ranking = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['ranking']
    
    def __str__(self):
        return "[{0}] {1} -- {2}: {3}".format(self.event, self.person,
                                              self.poll, self.value)