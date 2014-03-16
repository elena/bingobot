from django.db import models


POLL_CHOICES = (
    ('body', 'bodies'),
    ('boob', 'boobies'),
)


class Event(models.Model):
    date = None
    current = models.BooleanField(default=False)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return "[{0}] {1} -- {2}: {3}".format(self.event, self.person,
                                              self.poll, self.value)