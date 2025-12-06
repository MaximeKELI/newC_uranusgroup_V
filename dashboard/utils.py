"""
Utilitaires pour le dashboard (export PDF, etc.)
"""
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from services.models import ServiceRequest

User = get_user_model()


def generate_request_pdf(request_id):
    """
    Génère un PDF pour une demande de service
    """
    try:
        service_request = ServiceRequest.objects.get(id=request_id)
    except ServiceRequest.DoesNotExist:
        return None
    
    # Créer la réponse HTTP avec le type de contenu PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="demande_{service_request.id}.pdf"'
    
    # Créer le document PDF
    doc = SimpleDocTemplate(response, pagesize=A4)
    story = []
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#0A1A2F'),
        spaceAfter=30,
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#0DE1E7'),
        spaceAfter=12,
    )
    
    # Contenu
    story.append(Paragraph("Uranus Group", title_style))
    story.append(Paragraph("Demande de Service", heading_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Informations de la demande
    data = [
        ['Titre:', service_request.title],
        ['Service:', service_request.service.name],
        ['Client:', service_request.client.username],
        ['Statut:', service_request.get_status_display()],
        ['Priorité:', service_request.get_priority_display()],
        ['Date de création:', service_request.created_at.strftime('%d/%m/%Y %H:%M')],
    ]
    
    if service_request.deadline:
        data.append(['Date limite:', service_request.deadline.strftime('%d/%m/%Y %H:%M')])
    
    if service_request.assigned_to:
        data.append(['Assigné à:', service_request.assigned_to.username])
    
    table = Table(data, colWidths=[2*inch, 4*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#0A1A2F')),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('BACKGROUND', (1, 0), (1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    story.append(table)
    story.append(Spacer(1, 0.3*inch))
    
    # Description
    story.append(Paragraph("Description", heading_style))
    story.append(Paragraph(service_request.description, styles['Normal']))
    
    # Construire le PDF
    doc.build(story)
    
    return response

