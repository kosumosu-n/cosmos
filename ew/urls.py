from django.urls import path
from . import views

app_name = 'ew'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('word/add/', views.add, name='add'),
    path('word/<str:slug>/', views.detail, name='detail'),
    path('word/<str:slug>/edit/', views.Edit.as_view(), name='edit'),
    path('word/<str:slug>/delete/', views.Delete.as_view(), name='delete'),
    path('exs/', views.Examplesview.as_view(), name='examples'),
    path('exs/add/', views.Exadd.as_view(), name='exadd'),
    path('exs/<int:pk>/', views.Exedit.as_view(), name='exedit'),
    path('exs/<int:pk>/delete/', views.Exdelete.as_view(), name='exdelete'),
]