from django.urls import path
from . import views

urlpatterns = [
    path('', views.script_input_view, name='script_input'),
]
