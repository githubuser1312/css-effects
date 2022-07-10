from django.urls import path
from . import views

app_name = 'css_effects'

urlpatterns = [
    path('', views.index, name="index"),
    path('buttonseffects/', views.buttonseffects, name="buttonseffects"),
    path('menuseffects/', views.menuseffects, name="menuseffects"),
    path('specialeffects/', views.specialeffects, name="specialeffects"),
]