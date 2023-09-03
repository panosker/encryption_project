from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('action/', views.action, name='action'),
    path('encrypted/', views.encrypted, name='encrypted'),
    path('decrypted/', views.decrypted, name='decrypted'),
    path('about/',views.about,name='about')
]