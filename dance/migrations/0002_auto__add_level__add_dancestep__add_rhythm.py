# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Level'
        db.create_table('dance_level', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('dance', ['Level'])

        # Adding model 'DanceStep'
        db.create_table('dance_dancestep', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('rhythm', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'dancesteps', null=True, to=orm['dance.Rhythm'])),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'level', null=True, to=orm['dance.Level'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('dica', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('dance', ['DanceStep'])

        # Adding model 'Rhythm'
        db.create_table('dance_rhythm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('dance', ['Rhythm'])


    def backwards(self, orm):
        # Deleting model 'Level'
        db.delete_table('dance_level')

        # Deleting model 'DanceStep'
        db.delete_table('dance_dancestep')

        # Deleting model 'Rhythm'
        db.delete_table('dance_rhythm')


    models = {
        'dance.dancestep': {
            'Meta': {'ordering': "['name']", 'object_name': 'DanceStep'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dica': ('django.db.models.fields.TextField', [], {}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'update_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dance']