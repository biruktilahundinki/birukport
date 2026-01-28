from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.portfolio_home, name='home'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact_submit, name='contact_submit'),
    path('api/projects/', views.projects_api, name='projects_api'),
]
