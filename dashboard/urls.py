from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Dashboard principal
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    
    # Gestion utilisateurs
    path('admin/users/', views.manage_users, name='manage_users'),
    path('admin/users/create/', views.user_create, name='user_create'),
    path('admin/users/<int:user_id>/edit/', views.user_edit, name='user_edit'),
    path('admin/users/<int:user_id>/delete/', views.user_delete, name='user_delete'),
    
    # Gestion services
    path('admin/services/', views.manage_services, name='manage_services'),
    path('admin/services/create/', views.service_create, name='service_create'),
    path('admin/services/<int:service_id>/edit/', views.service_edit, name='service_edit'),
    path('admin/services/<int:service_id>/delete/', views.service_delete, name='service_delete'),
    
    # Gestion catégories de services
    path('admin/service-categories/', views.manage_service_categories, name='manage_service_categories'),
    path('admin/service-categories/create/', views.service_category_create, name='service_category_create'),
    path('admin/service-categories/<int:category_id>/edit/', views.service_category_edit, name='service_category_edit'),
    path('admin/service-categories/<int:category_id>/delete/', views.service_category_delete, name='service_category_delete'),
    
    # Gestion demandes
    path('admin/requests/', views.manage_requests, name='manage_requests'),
    path('admin/requests/<int:request_id>/edit/', views.request_edit, name='request_edit'),
    path('admin/requests/<int:request_id>/delete/', views.request_delete, name='request_delete'),
    path('admin/requests/<int:request_id>/export-pdf/', views.request_export_pdf, name='request_export_pdf'),
    
    # Gestion certifications
    path('admin/certifications/', views.manage_certifications, name='manage_certifications'),
    path('admin/certifications/create/', views.certification_create, name='certification_create'),
    path('admin/certifications/<int:cert_id>/edit/', views.certification_edit, name='certification_edit'),
    path('admin/certifications/<int:cert_id>/delete/', views.certification_delete, name='certification_delete'),
    
    # Gestion témoignages
    path('admin/testimonials/', views.manage_testimonials, name='manage_testimonials'),
    path('admin/testimonials/create/', views.testimonial_create, name='testimonial_create'),
    path('admin/testimonials/<int:testimonial_id>/edit/', views.testimonial_edit, name='testimonial_edit'),
    path('admin/testimonials/<int:testimonial_id>/delete/', views.testimonial_delete, name='testimonial_delete'),
    
    # Gestion articles
    path('admin/articles/', views.manage_articles, name='manage_articles'),
    path('admin/articles/create/', views.article_create, name='article_create'),
    path('admin/articles/<int:article_id>/edit/', views.article_edit, name='article_edit'),
    path('admin/articles/<int:article_id>/delete/', views.article_delete, name='article_delete'),
    
    # Gestion catégories de blog
    path('admin/blog-categories/', views.manage_blog_categories, name='manage_blog_categories'),
    path('admin/blog-categories/create/', views.blog_category_create, name='blog_category_create'),
    path('admin/blog-categories/<int:category_id>/edit/', views.blog_category_edit, name='blog_category_edit'),
    path('admin/blog-categories/<int:category_id>/delete/', views.blog_category_delete, name='blog_category_delete'),
    
    # Gestion slider
    path('admin/slider/', views.manage_slider, name='manage_slider'),
    path('admin/slider/create/', views.slider_item_create, name='slider_item_create'),
    path('admin/slider/<int:item_id>/edit/', views.slider_item_edit, name='slider_item_edit'),
    path('admin/slider/<int:item_id>/delete/', views.slider_item_delete, name='slider_item_delete'),
    
    # Gestion équipe
    path('admin/team/', views.manage_team, name='manage_team'),
    path('admin/team/create/', views.team_member_create, name='team_member_create'),
    path('admin/team/<int:member_id>/edit/', views.team_member_edit, name='team_member_edit'),
    path('admin/team/<int:member_id>/delete/', views.team_member_delete, name='team_member_delete'),
    
    # Gestion messages de contact
    path('admin/contact-messages/', views.manage_contact_messages, name='manage_contact_messages'),
    path('admin/contact-messages/<int:message_id>/update-status/', views.contact_message_update_status, name='contact_message_update_status'),
    path('admin/contact-messages/<int:message_id>/delete/', views.contact_message_delete, name='contact_message_delete'),
    
    # Gestion tickets
    path('admin/tickets/', views.manage_tickets, name='manage_tickets'),
    path('tickets/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('tickets/<int:ticket_id>/update-status/', views.ticket_update_status, name='ticket_update_status'),
    path('tickets/create/', views.create_ticket, name='create_ticket'),
    
    # Notifications
    path('notifications/', views.notifications, name='notifications'),
    path('notifications/<int:notification_id>/read/', views.mark_notification_read, name='mark_notification_read'),
    path('notifications/read-all/', views.mark_all_notifications_read, name='mark_all_notifications_read'),
]
