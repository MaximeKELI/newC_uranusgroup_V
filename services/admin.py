from django.contrib import admin
from .models import ServiceCategory, Service, ServiceRequest, Deliverable, Certification, Testimonial


class SoftDeleteMixin(admin.ModelAdmin):
    actions = ['delete_selected']
    
    def delete_queryset(self, request, queryset):
        # Surcharge pour la suppression douce si nécessaire
        queryset.delete()

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(SoftDeleteMixin):
    list_display = ['name', 'slug', 'order', 'is_active']
    list_filter = ['is_active']
    prepopulated_fields = {'slug': ('name',)}
    actions = ['delete_selected']


@admin.register(Service)
class ServiceAdmin(SoftDeleteMixin):
    list_display = ['name', 'category', 'status', 'featured', 'order', 'created_at', 'is_active']
    list_filter = ['category', 'status', 'featured', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    actions = ['delete_selected']


@admin.register(ServiceRequest)
class ServiceRequestAdmin(SoftDeleteMixin):
    list_display = ['title', 'client', 'service', 'status', 'priority', 'created_at', 'is_active']
    list_filter = ['status', 'priority', 'created_at', 'is_active']
    search_fields = ['title', 'client__username', 'service__name']
    actions = ['delete_selected']


@admin.register(Deliverable)
class DeliverableAdmin(SoftDeleteMixin):
    list_display = ['name', 'request', 'uploaded_by', 'uploaded_at', 'is_active']
    list_filter = ['uploaded_at', 'is_active']
    actions = ['delete_selected']


@admin.register(Certification)
class CertificationAdmin(SoftDeleteMixin):
    list_display = ['name', 'code', 'category', 'order', 'created_at']
    list_filter = ['category', 'created_at']
    actions = ['delete_selected']


@admin.register(Testimonial)
class TestimonialAdmin(SoftDeleteMixin):
    list_display = ['client_name', 'client_company', 'rating', 'featured', 'created_at']
    list_filter = ['rating', 'featured', 'created_at']
    actions = ['delete_selected']
