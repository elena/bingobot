# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Person.slug'
        db.add_column(u'scores_person', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default=0, max_length=256),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Person.slug'
        db.delete_column(u'scores_person', 'slug')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '256'})
        },
        u'scores.poll': {
            'Meta': {'object_name': 'Poll'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scores.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scores.Person']"}),
            'poll': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'ranking': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['scores']