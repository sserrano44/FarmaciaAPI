# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Farmacia'
        db.create_table('turnos_farmacia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('lon', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('turnos', ['Farmacia'])

        # Adding model 'Turno'
        db.create_table('turnos_turno', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('farmacia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['turnos.Farmacia'])),
            ('inicio', self.gf('django.db.models.fields.DateTimeField')()),
            ('fin', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('turnos', ['Turno'])


    def backwards(self, orm):
        
        # Deleting model 'Farmacia'
        db.delete_table('turnos_farmacia')

        # Deleting model 'Turno'
        db.delete_table('turnos_turno')


    models = {
        'turnos.farmacia': {
            'Meta': {'object_name': 'Farmacia'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lon': ('django.db.models.fields.FloatField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '128'})
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
