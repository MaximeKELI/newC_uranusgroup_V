// Animation au chargement de la page
document.addEventListener('DOMContentLoaded', function() {
    // Animation des éléments du tableau
    const tableRows = document.querySelectorAll('#result_list tbody tr');
    tableRows.forEach((row, index) => {
        row.style.opacity = '0';
        row.style.transform = 'translateY(10px)';
        row.style.transition = `all 0.3s ease ${index * 0.05}s`;
        setTimeout(() => {
            row.style.opacity = '1';
            row.style.transform = 'translateY(0)';
        }, 50);
    });

    // Amélioration des tooltips
    const tooltips = document.querySelectorAll('[title]');
    tooltips.forEach(tooltip => {
        const tooltipText = tooltip.getAttribute('title');
        if (tooltipText) {
            const tooltipElement = document.createElement('span');
            tooltipElement.className = 'tooltip-text';
            tooltipElement.textContent = tooltipText;
            tooltip.appendChild(tooltipElement);
            tooltip.classList.add('has-tooltip');
            tooltip.removeAttribute('title');
        }
    });

    // Animation des boutons
    const buttons = document.querySelectorAll('button, .button, input[type="submit"], input[type="button"]');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
            this.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.15)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 2px 4px rgba(0, 0, 0, 0.1)';
        });
    });

    // Animation des champs de formulaire
    const formInputs = document.querySelectorAll('input, select, textarea');
    formInputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('input-focused');
        });
        
        input.addEventListener('blur', function() {
            this.parentElement.classList.remove('input-focused');
        });
    });

    // Notification de chargement
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitButton = this.querySelector('input[type="submit"], button[type="submit"]');
            if (submitButton) {
                submitButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> ' + submitButton.textContent;
                submitButton.disabled = true;
            }
        });
    });
});

// Fonction pour afficher des notifications
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    // Animation d'entrée
    setTimeout(() => {
        notification.style.opacity = '1';
        notification.style.transform = 'translateY(0)';
    }, 10);
    
    // Suppression après 5 secondes
    setTimeout(() => {
        notification.style.opacity = '0';
        notification.style.transform = 'translateY(-20px)';
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 5000);
}

// Gestion des messages Django
const messages = document.querySelectorAll('.messagelist li');
messages.forEach(message => {
    message.style.opacity = '0';
    message.style.transform = 'translateX(20px)';
    message.style.transition = 'all 0.3s ease';
    
    setTimeout(() => {
        message.style.opacity = '1';
        message.style.transform = 'translateX(0)';
    }, 100);
    
    // Ajout d'un bouton de fermeture
    const closeButton = document.createElement('button');
    closeButton.innerHTML = '&times;';
    closeButton.className = 'close-message';
    closeButton.addEventListener('click', function() {
        message.style.opacity = '0';
        message.style.transform = 'translateX(20px)';
        setTimeout(() => {
            message.remove();
        }, 300);
    });
    
    message.appendChild(closeButton);
});
