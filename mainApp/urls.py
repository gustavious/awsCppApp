from django.conf.urls import url
from mainApp import views
from rest_framework.urlpatterns import  format_suffix_patterns

urlpatterns = [
    url(r'^envios/$', views.EnvioViewSet.as_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)
