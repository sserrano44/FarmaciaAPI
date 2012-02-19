# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Farmacia.ubicacion'
        db.delete_column('turnos_farmacia', 'ubicacion')

        # Adding field 'Farmacia.col_nombre'
        db.add_column('turnos_farmacia', 'col_nombre', self.gf('django.db.models.fields.CharField')(default='', max_length=64), keep_default=False)

        # Adding field 'Farmacia.zona'
        db.add_column('turnos_farmacia', 'zona', self.gf('django.db.models.fields.CharField')(default='', max_length=64), keep_default=False)

        # Adding field 'Farmacia.direccion'
        db.add_column('turnos_farmacia', 'direccion', self.gf('django.db.models.fields.CharField')(default='', max_length=128), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Farmacia.ubicacion'
        db.add_column('turnos_farmacia', 'ubicacion', self.gf('django.db.models.fields.CharField')(default='', max_length=128), keep_default=False)

        # Deleting field 'Farmacia.col_nombre'
        db.delete_column('turnos_farmacia', 'col_nombre')

        # Deleting field 'Farmacia.zona'
        db.delete_column('turnos_farmacia', 'zona')

        # Deleting field 'Farmacia.direccion'
        db.delete_column('turnos_farmacia', 'direccion')


    models = {
        'turnos.farmacia': {
            'Meta': {'object_name': 'Farmacia'},
            'col_nombre': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'direccion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lon': ('django.db.models.fields.FloatField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'zona': ('django.db.models.fields.CharField', [], {'max_length': '64'})
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
