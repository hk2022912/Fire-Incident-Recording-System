from django.urls import path
from . import views

urlpatterns = [
    path('personnel/',            views.personnel_list,   name='personnel-list'),
    path('personnel/<int:slot>/', views.personnel_detail, name='personnel-detail'),
    path('incidents/',            views.incident_list,    name='incident-list'),
    path('incidents/bulk/',       views.incident_bulk,    name='incident-bulk'),
    path('incidents/<int:pk>/',   views.incident_detail,  name='incident-detail'),
]