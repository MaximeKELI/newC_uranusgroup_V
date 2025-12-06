from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ServiceViewSet, ServiceCategoryViewSet, ServiceRequestViewSet, DeliverableViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'categories', ServiceCategoryViewSet, basename='category')
router.register(r'requests', ServiceRequestViewSet, basename='request')
router.register(r'deliverables', DeliverableViewSet, basename='deliverable')

urlpatterns = [
    path('', include(router.urls)),
]

