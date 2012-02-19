from django.conf.urls.defaults import patterns, include, url

from tastypie.api import Api
from apps.turnos.api import FarmaciaResource, TurnoResource

v1_api = Api(api_name='v1')
v1_api.register(FarmaciaResource())
v1_api.register(TurnoResource())

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),    
    (r'^api/', include(v1_api.urls)),
    url(r'^turnos/', include('apps.turnos.urls')),
)

