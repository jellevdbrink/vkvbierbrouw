from django.urls import path

from brouwen import views

urlpatterns = [
    path('', views.index, name='index'),
]
