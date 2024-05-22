from django.urls import path        
from .views import tabel_views , reservation_views 


urlpatterns = [
    path('home/', tabel_views.HomePageView.as_view(), name='home'),  # Home page URL
    path('', tabel_views.ListView.as_view(), name='index'),
    path('table/<int:pk>', tabel_views.DetailView.as_view(), name='table'),
    path('reservation/', reservation_views.CreateView.as_view(), name='reservation'),
]
