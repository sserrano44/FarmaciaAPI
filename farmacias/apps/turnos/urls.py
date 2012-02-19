from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^update/$', 'apps.turnos.views.update', name='turnos_update'),
    url(r'^mapa/$', 'apps.turnos.views.mapa', name='turnos_mapa'),
)