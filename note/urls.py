from django.urls import path
from . import views

app_name = 'note'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('detail/<int:pk>/', views.Detail.as_view(), name='detail'),
    path('add/', views.Add.as_view(), name='add'),
    path('edit/<int:pk>/', views.Edit.as_view(), name='edit'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
]