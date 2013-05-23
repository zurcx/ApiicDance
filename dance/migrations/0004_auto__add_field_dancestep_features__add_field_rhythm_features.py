# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DanceStep.features'
        db.add_column('dance_dancestep', 'features',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Rhythm.features'
        db.add_column('dance_rhythm', 'features',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DanceStep.features'
        db.delete_column('dance_dancestep', 'features')

        # Deleting field 'Rhythm.features'
        db.delete_column('dance_rhythm', 'features')


    models = {
        'dance.dancestep': {
            'Meta': {'ordering': "['name']", 'object_name': 'DanceStep'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dica': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'features': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'level'", 'null': 'True', 'to': "orm['dance.Level']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rhythm': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dancesteps'", 'null': 'True', 'to': "orm['dance.Rhythm']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'dance.level': {
            'Meta': {'ordering': "['name']", 'object_name': 'Level'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'dance.rhythm': {
            'Meta': {'ordering': "['name']", 'object_name': 'Rhythm'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'features': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'update_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dance']