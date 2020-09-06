from django.contrib import admin
from django.urls import path
from appatencion.views import AtencionView

from django.conf import settings
app_name = "appatencion"
urlpatterns = [
    path('atencion/', AtencionView.as_view(), name='atencion'),
  
]
