"""
API REST pour les services (préparation pour application mobile)
"""
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Service, ServiceCategory, ServiceRequest, Deliverable
from .serializers import (
    ServiceSerializer,
    ServiceCategorySerializer,
    ServiceRequestSerializer,
    DeliverableSerializer
)


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet pour les services (lecture seule pour les clients)
    """
    queryset = Service.objects.filter(status='active')
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category__slug=category)
        return queryset


class ServiceCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet pour les catégories de services
    """
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ServiceRequestViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour les demandes de service
    """
    serializer_class = ServiceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_admin() or user.is_manager_qhse() or user.is_manager_info():
            return ServiceRequest.objects.all()
        return ServiceRequest.objects.filter(client=user)
    
    def perform_create(self, serializer):
        serializer.save(client=self.request.user)
    
    @action(detail=True, methods=['post'])
    def upload_deliverable(self, request, pk=None):
        """
        Upload un livrable pour une demande
        """
        service_request = self.get_object()
        file = request.FILES.get('file')
        name = request.data.get('name', '')
        
        if not file:
            return Response(
                {'error': 'Aucun fichier fourni'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        deliverable = Deliverable.objects.create(
            request=service_request,
            name=name or file.name,
            file=file,
            uploaded_by=request.user
        )
        
        serializer = DeliverableSerializer(deliverable)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DeliverableViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet pour les livrables
    """
    serializer_class = DeliverableSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_admin():
            return Deliverable.objects.all()
        return Deliverable.objects.filter(request__client=user)

