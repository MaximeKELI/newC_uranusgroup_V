from django.contrib import admin
from .models import ServiceCategory, Service, ServiceRequest, Deliverable, Certification, Testimonial


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'status', 'featured', 'order', 'created_at']
    list_filter = ['category', 'status', 'featured']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'service', 'status', 'priority', 'created_at']
    list_filter = ['status', 'priority', 'created_at']
    search_fields = ['title', 'client__username', 'service__name']


@admin.register(Deliverable)
class DeliverableAdmin(admin.ModelAdmin):
    list_display = ['name', 'request', 'uploaded_by', 'uploaded_at']
    list_filter = ['uploaded_at']


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'category', 'order', 'created_at']
    list_filter = ['category', 'created_at']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_company', 'rating', 'featured', 'created_at']
    list_filter = ['rating', 'featured', 'created_at']
