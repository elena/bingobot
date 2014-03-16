# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'scores_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('current', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'scores', ['Event'])

        # Adding model 'EventPoll'
        db.create_table(u'scores_eventpoll', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scores.Event'])),
            ('poll', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'scores', ['EventPoll'])

        # Adding model 'Person'
        db.create_table(u'scores_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'scores', ['Person'])

        # Adding model 'Poll'
        db.create_table(u'scores_poll', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scores.Event'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scores.Person'])),
            ('poll', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'scores', ['Poll'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'scores_event')

        # Deleting model 'EventPoll'
        db.delete_table(u'scores_eventpoll')

        # Deleting model 'Person'
        db.delete_table(u'scores_person')

        # Deleting model 'Poll'
        db.delete_table(u'scores_poll')


    models = {
        u'scores.event': {
            'Meta': {'object_name': 'Event'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'scores.eventpoll': {
            'Meta': {'object_name': 'EventPoll'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scores.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'scores.person': {
            'Meta': {'object_name': 'Person'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'scores.poll': {
            'Meta': {'object_name': 'Poll'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scores.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scores.Person']"}),
            'poll': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['scores']