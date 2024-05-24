from django.urls import path        
from .views import tabel_views , reservation_views 


urlpatterns = [
    path('', tabel_views.HomePageView.as_view(), name='home'),  
    path('home', tabel_views.ListView.as_view(), name='index'),
    path('table/<int:pk>', tabel_views.DetailView.as_view(), name='table'),

    path('reservation/', reservation_views.ReservationCreate.as_view(), name='reservation'),
    path('update-reservation/<int:pk>/', reservation_views.ReservationUpdate.as_view(), name='update_reservation'),
    path('delete-reservation/<int:pk>/', reservation_views.ReservationDelete.as_view(), name='delete_reservation'),

]
