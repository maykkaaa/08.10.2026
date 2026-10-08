from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('projects/', views.projects_view, name='projects'),
    path('skills/', views.skills_view, name='skills'),
    path('polls/', views.polls, name='polls'),
]