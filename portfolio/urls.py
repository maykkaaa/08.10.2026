from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),

    path('projects/', views.projects_view, name='projects'),

    path(
        'projects/<str:project_name>/',
        views.project_detail_view,
        name='project_detail'
    ),

    path('skills/', views.skills_view, name='skills'),

    path('polls/', views.polls, name='polls'),
]
