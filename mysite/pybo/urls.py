from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
     path('', views.index, name='index'),
     path('<int:qs_id>/', views.detail, name='detail'),
     path('aw/create/<int:qs_id>/', views.aw_create, name='aw_create'),
]
