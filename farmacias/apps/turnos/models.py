import datetime
import logging

from django.db import models

def today():
    return datetime.datetime.now()

def tomorrow():
    return datetime.datetime.now() + datetime.timedelta(days=1)

class DeTurnoManager(models.Manager):
    def __init__(self, when, * args, ** kwargs):
        self.when = when
        super(DeTurnoManager, self).__init__(* args, ** kwargs)

    def get_query_set(self):
        when = self.when()
        return super(DeTurnoManager, self).get_query_set().filter(turno__inicio__lt=when,turno__fin__gt=when)

class Farmacia(models.Model):
    nombre      = models.CharField(max_length=64)
    #the name as it appears on the college website
    col_nombre  = models.CharField(max_length=64)
    zona        = models.CharField(max_length=64, default="", blank=True)
    direccion   = models.CharField(max_length=128, default="")
    descripcion = models.TextField(default="", blank=True)
    telefono    = models.CharField(max_length=64, default="", blank=True)
    lat         = models.FloatField(null=True, blank=True)
    lon         = models.FloatField(null=True, blank=True)
    revisado    = models.BooleanField(default=False)

    objects           = models.Manager()
    on_guard_today    = DeTurnoManager(today)
    on_guard_tomorrow = DeTurnoManager(tomorrow)
 
    def __unicode__(self):
        return u"%s" % self.nombre

    def resolve(self, save=True):
        from geopy import geocoders  
        g = geocoders.Google()
        try:
            direccion = self.direccion.encode("ascii", "ignore")
            place, (lat, lng) = g.geocode(u"%s, La Plata, Buenos Aires Province, Argentina" % direccion, exactly_one=False)[0]
        except IndexError:
            return
        logging.info("%s: %.5f, %.5f" % (place, lat, lng))
        self.lat = lat
        self.lon = lng
        if save:
            self.save()
        return

    def save(self, * args, ** kwargs):
        if self.lat == None:
            try:
                self.resolve(save=False)
            except:
                logging.exception("problem resolving lat/lon of %s" % self.direccion)
        super(Farmacia, self).save(* args, ** kwargs)

    def guard_today(self):
        now = datetime.datetime.now()
        try:
            self.turno_set.filter(inicio__lt=now, fin__gt=now)[0]
            return True
        except IndexError:
            return False

    def guard_tomorrow(self):
        tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
        try:
            self.turno_set.filter(inicio__lt=tomorrow, fin__gt=tomorrow)[0]
            return True
        except IndexError:
            return False

class Turno(models.Model):
    farmacia    = models.ForeignKey(Farmacia)
    inicio      = models.DateTimeField()
    fin         = models.DateTimeField()

    def __unicode__(self):
        return u"%s: %s" % (self.farmacia.nombre, self.inicio.strftime("%Y-%m-%d"))

