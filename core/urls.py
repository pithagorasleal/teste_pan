from django.urls import path
from core.views import *

urlpatterns = [
    path('', login, name='login'),
    path('index/', index, name='index'),
    path('step/new', step_new, name='step_new'),
    path('process/new', process_new, name='process_new'),
    path(r'^process/config/(?P<form.id>\d+)$', process_config, name='process_config')
]