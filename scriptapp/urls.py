from django.urls import path
from . import views

urlpatterns = [
    path('', views.script_input, name='script_input'),
    path('chapters/', views.chapter_list, name='chapter_list'),

]
