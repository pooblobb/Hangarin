from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Directs the homepage to the 'index' view
]