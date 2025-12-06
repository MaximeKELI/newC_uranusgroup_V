from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('<slug:slug>/', views.service_detail, name='service_detail'),
    path('<int:service_id>/request/', views.request_service, name='request_service'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('requests/<int:request_id>/', views.request_detail, name='request_detail'),
]

