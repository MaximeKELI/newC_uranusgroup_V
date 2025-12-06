"""
Serializers pour l'API REST
"""
from rest_framework import serializers
from .models import Service, ServiceCategory, ServiceRequest, Deliverable


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['id', 'name', 'slug', 'description', 'icon', 'color']


class ServiceSerializer(serializers.ModelSerializer):
    category = ServiceCategorySerializer(read_only=True)
    
    class Meta:
        model = Service
        fields = [
            'id', 'name', 'slug', 'short_description', 'full_description',
            'image', 'icon', 'price_starting_from', 'duration',
            'category', 'featured', 'created_at'
        ]


class ServiceRequestSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    service_id = serializers.IntegerField(write_only=True)
    client = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = ServiceRequest
        fields = [
            'id', 'service', 'service_id', 'client', 'title', 'description',
            'status', 'priority', 'deadline', 'created_at', 'updated_at'
        ]
        read_only_fields = ['status', 'created_at', 'updated_at']


class DeliverableSerializer(serializers.ModelSerializer):
    request = serializers.StringRelatedField(read_only=True)
    uploaded_by = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Deliverable
        fields = [
            'id', 'request', 'name', 'description', 'file',
            'uploaded_by', 'uploaded_at'
        ]
        read_only_fields = ['uploaded_at']

