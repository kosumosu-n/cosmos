from django.urls import path
from . import views

app_name = 'note'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/<int:noteid>/', views.delete, name='delete'),
]