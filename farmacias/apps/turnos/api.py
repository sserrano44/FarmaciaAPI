from tastypie.resources import ModelResource
from tastypie import fields

from apps.turnos.models import Farmacia, Turno
import logging
import datetime
import time

YESTERDAY = datetime.datetime.now() - datetime.timedelta(days=1)

class FarmaciaResource(ModelResource):
    class Meta:
        queryset = Farmacia.objects.all()

class TurnoResource(ModelResource):
    farmacia = fields.DictField()
    inicio   = fields.IntegerField()
    fin      = fields.IntegerField()

    class Meta:
        queryset = Turno.objects.filter(inicio__gt=YESTERDAY)
        filtering = {
            'inicio': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
    
    def dehydrate_farmacia(self, bundle):
        farmacia = bundle.obj.farmacia
        res = {
            'id': farmacia.id,
            'nombre': farmacia.nombre,
            'descripcion': farmacia.descripcion,
            'direccion': farmacia.direccion,
            'telefono': farmacia.telefono,
            'lat': farmacia.lat,
            'lon': farmacia.lon,
        }
        return res

    def dehydrate_inicio(self, bundle):
        inicio = bundle.obj.inicio
        timestamp = u"%s" % int(time.mktime(inicio.timetuple()))
        logging.info("%s" % timestamp)
        return timestamp

    def dehydrate_fin(self, bundle):
        fin = bundle.obj.fin
        timestamp = u"%s" % int(time.mktime(fin.timetuple()))
        logging.info("%s" % timestamp)
        return timestamp

