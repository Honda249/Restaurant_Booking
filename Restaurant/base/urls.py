from django.urls import path        
from .views import tabel_views


urlpatterns = [
    path('tables/', tabel_views.IndexView.as_view(), name='Home'),
]
