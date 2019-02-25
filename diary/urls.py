from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('detail/<uuid:pk>/', views.detail, name='detail'),
    path('delete/<uuid:pk>/', views.delete, name='delete'),
]
