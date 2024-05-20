from django.urls import path        
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('tables/', views.TableListView.as_view(), name='table list'),
]
