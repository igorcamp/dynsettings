# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DynSettings'
        db.create_table(u'dynsettings_dynsettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('type', self.gf('django.db.models.fields.CharField')(default='NoneType', max_length=20)),
        ))
        db.send_create_signal(u'dynsettings', ['DynSettings'])


    def backwards(self, orm):
        # Deleting model 'DynSettings'
        db.delete_table(u'dynsettings_dynsettings')


    models = {
        u'dynsettings.dynsettings': {
            'Meta': {'object_name': 'DynSettings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'NoneType'", 'max_length': '20'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['dynsettings']