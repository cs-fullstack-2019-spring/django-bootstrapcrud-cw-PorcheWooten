from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('edititem/<int:id>/', views.edititem, name='edititem'),


]