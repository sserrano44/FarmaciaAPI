import urllib

from django.http import HttpResponse

import httplib2
from django.utils import simplejson
import datetime
import re
from apps.turnos.models import Turno, Farmacia
import logging
from django.shortcuts import render_to_response
from django.template.context import RequestContext

URL = "http://opensa.colfarmalp.org.ar/colfarm/web/frontend.php/secretaria/list"

def update(request):
    """
        View that gets the last turnos

        {u'content': u"
        <strong>Farmacia: </strong>ITALIANA DE LOS HORNOS<br />
        <strong>Direccion: </strong>137 nro 1573<br />
        <strong>Telefono: </strong>4504256<br />
        <strong>Zona: </strong>Los Hornos
        ", 
         u'start': u'2012-02-29', u'end': u'2012-02-29', u'id': u'12186', 
         u'title': u'Los Hornos - 137 nro 1573'}


    """
    http = httplib2.Http()
    t0 = datetime.datetime.today()
    t1 = t0 + datetime.timedelta(days=1)
    now = datetime.datetime.now()
    params = {
     'start': t0.strftime("%s000"),
     'end':   t1.strftime("%s000"),
     '_':     now.strftime("%s000")
    }
    url = "%s?%s" % (URL, urllib.urlencode(params))
    
    (status, content) = http.request(url)

    res = simplejson.loads(content)
    
    for item in res:        
        try:
            Turno.objects.get(id=item['id'])
            continue
        except Turno.DoesNotExist:
            pass
        
        nombre = re.search("<strong>Farmacia:\s*</strong>([^<]+)<br />", item['content'])
        if nombre:
            nombre = nombre.group(1).strip()
        else:
            raise Exception("problem parsing turnos")
        
        direccion = re.search("<strong>Direccion:\s*</strong>([^<]+)<br />", item['content'])
        if direccion:
            direccion = direccion.group(1).strip()
        else:
            direccion = ""
        telefono = re.search("<strong>Telefono:\s*</strong>([^<]+)<br />", item['content'])
        if telefono:
            telefono = telefono.group(1).strip()
        else:
            telefono = ""
        zona = re.search("<strong>Zona:\s*</strong>([^<]+)<br />", item['content'])
        if zona:
            zona = zona.group(1).strip()
        else:
            zona = ""

        try:
            farmacia = Farmacia.objects.get(col_nombre=nombre)
        except Farmacia.DoesNotExist:
            farmacia = Farmacia(
                nombre = nombre.title(),
                col_nombre=nombre,
                direccion=direccion,
                telefono=telefono,
                zona=zona
            )
            farmacia.save()
            
        inicio = datetime.datetime.strptime(item['start'] + " 08:30", "%Y-%m-%d %H:%M")
        Turno(
            id=item['id'],
            farmacia = farmacia,
            inicio   = inicio,
            fin      = inicio + datetime.timedelta(days=1)
        ).save()
    
    return HttpResponse("done", mimetype="application/json")


def mapa(request):
    params = {
       'farmacias':         Farmacia.objects.filter(lat__isnull=False),
       'on_guard_today':    Farmacia.on_guard_today.all(),
       'on_guard_tomorrow': Farmacia.on_guard_tomorrow.all()
       
    }
    return render_to_response('mapa.html', params, RequestContext(request))

