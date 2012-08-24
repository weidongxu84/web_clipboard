# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Clip'
        db.create_table('clipboard_clip', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('content_text', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clipboard.User'])),
        ))
        db.send_create_signal('clipboard', ['Clip'])

        # Adding model 'User'
        db.create_table('clipboard_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('ip_addr', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('clipboard', ['User'])


    def backwards(self, orm):
        # Deleting model 'Clip'
        db.delete_table('clipboard_clip')

        # Deleting model 'User'
        db.delete_table('clipboard_user')


    models = {
        'clipboard.clip': {
            'Meta': {'object_name': 'Clip'},
            'content_text': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clipboard.User']"})
        },
        'clipboard.user': {
            'Meta': {'object_name': 'User'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_addr': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['clipboard']