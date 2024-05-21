from django.urls import path        
from .views import tabel_views , reservation_views


urlpatterns = [
    path('', tabel_views.IndexView.as_view(), name='home'),
    path('', reservation_views.CreateView.as_view(), name='reservation'),
]
