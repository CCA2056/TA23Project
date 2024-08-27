from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPage, name='landing-page'),
    path('home', views.homePage, name='home-page'),
    path('scenario-role-play',views.scenarioRolePlay, name = 'scenario-role-play'),
    path('scenario-role-play-list',views.scenarioRolePlayList, name = 'scenario-role-play-list'),
]