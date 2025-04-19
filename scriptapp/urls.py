from django.urls import path
from . import views

urlpatterns = [
    path('', views.script_input, name='script_input'),
    path('chapters/', views.chapter_list, name='chapter_list'),
      path('entry/<int:entry_id>/edit/', views.edit_entry, name='edit_entry'),
    path('entry/<int:entry_id>/delete/', views.delete_entry, name='delete_entry'),

]
