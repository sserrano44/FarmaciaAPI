# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Farmacia.lon'
        db.alter_column('turnos_farmacia', 'lon', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Farmacia.lat'
        db.alter_column('turnos_farmacia', 'lat', self.gf('django.db.models.fields.FloatField')(null=True))


    def backwards(self, orm):
        
        # Changing field 'Farmacia.lon'
        db.alter_column('turnos_farmacia', 'lon', self.gf('django.db.models.fields.FloatField')(default=0.0))

        # Changing field 'Farmacia.lat'
        db.alter_column('turnos_farmacia', 'lat', self.gf('django.db.models.fields.FloatField')(default=0.0))


    models = {
        'turnos.farmacia': {
            'Meta': {'object_name': 'Farmacia'},
            'col_nombre': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64', 'blank': 'True'}),
            'zona': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64', 'blank': 'True'})
        },
        'turnos.turno': {
            'Meta': {'object_name': 'Turno'},
            'farmacia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['turnos.Farmacia']"}),
            'fin': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['turnos']
