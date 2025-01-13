from django.urls import path

from aplicatie1 import views

app_name = 'locations'

urlpatterns = [
    path('', views.LocationView.as_view(), name='lista_locatii'),
    path('adaugare/', views.CreateLocationView.as_view(), name='adaugare'),
    path('<int:pk>/update/', views.UpdateLocationView.as_view(), name='editare'),
    path('<int:pk>/delete/', views.delete_location, name='stergere'),
    path('<int:pk>/restore/', views.restore_location, name='reactivare'),
    path('start_timesheet/', views.start_timesheet, name='start_pontaj'),
    path('stop_timesheet/', views.stop_timesheet, name='stop_pontaj')
]