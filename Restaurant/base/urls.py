from django.urls import path        
from django.contrib.auth.views import LogoutView
from .views import tabel_views , reservation_views , auth_views




urlpatterns = [
    #Auth Views
    path('login/', auth_views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

    path('', tabel_views.HomePageView.as_view(), name='home'),  
    path('home', tabel_views.ListView.as_view(), name='index'),
    path('table/<int:pk>', tabel_views.DetailView.as_view(), name='table'),

    path('reservation/', reservation_views.ReservationCreate.as_view(), name='reservation'),
    path('update-reservation/<int:pk>/', reservation_views.ReservationUpdate.as_view(), name='update_reservation'),
    path('delete-reservation/<int:pk>/', reservation_views.ReservationDelete.as_view(), name='delete_reservation'),

]
