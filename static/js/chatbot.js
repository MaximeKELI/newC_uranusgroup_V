// Chatbot IA Gemini - Uranus Group

class Chatbot {
    constructor() {
        this.isOpen = false;
        this.chatHistory = [];
        this.init();
    }

    init() {
        this.createChatbotUI();
        this.attachEventListeners();
    }

    createChatbotUI() {
        // Créer le conteneur du chatbot
        const chatbotContainer = document.createElement('div');
        chatbotContainer.id = 'chatbot-container';
        chatbotContainer.innerHTML = `
            <!-- Bouton flottant pour ouvrir le chatbot -->
            <button id="chatbot-toggle" class="chatbot-toggle" aria-label="Ouvrir le chatbot">
                <i class="fas fa-comments"></i>
                <span class="chatbot-pulse"></span>
            </button>

            <!-- Fenêtre du chatbot -->
            <div id="chatbot-window" class="chatbot-window">
                <div class="chatbot-header">
                    <div class="chatbot-header-content">
                        <div class="chatbot-avatar">
                            <i class="fas fa-robot"></i>
                        </div>
                        <div class="chatbot-header-text">
                            <h3>Assistant Uranus Group</h3>
                            <p class="chatbot-status">En ligne</p>
                        </div>
                    </div>
                    <button id="chatbot-close" class="chatbot-close" aria-label="Fermer le chatbot">
                        <i class="fas fa-times"></i>
                    </button>
                </div>

                <div class="chatbot-messages" id="chatbot-messages">
                    <div class="chatbot-message bot-message">
                        <div class="message-avatar">
                            <i class="fas fa-robot"></i>
                        </div>
                        <div class="message-content">
                            <p>Bonjour ! Je suis l'assistant virtuel d'Uranus Group. Comment puis-je vous aider aujourd'hui ?</p>
                        </div>
                    </div>
                </div>

                <div class="chatbot-input-container">
                    <form id="chatbot-form" class="chatbot-form">
                        <input 
                            type="text" 
                            id="chatbot-input" 
                            class="chatbot-input" 
                            placeholder="Tapez votre message..."
                            autocomplete="off"
                        />
                        <button type="submit" id="chatbot-send" class="chatbot-send" aria-label="Envoyer le message">
                            <i class="fas fa-paper-plane"></i>
                        </button>
                    </form>
                </div>
            </div>
        `;

        document.body.appendChild(chatbotContainer);
    }

    attachEventListeners() {
        const toggleBtn = document.getElementById('chatbot-toggle');
        const closeBtn = document.getElementById('chatbot-close');
        const form = document.getElementById('chatbot-form');
        const input = document.getElementById('chatbot-input');

        toggleBtn.addEventListener('click', () => this.toggleChatbot());
        closeBtn.addEventListener('click', () => this.closeChatbot());
        form.addEventListener('submit', (e) => this.handleSubmit(e));
        
        // Permettre l'envoi avec Enter
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                form.dispatchEvent(new Event('submit'));
            }
        });
    }

    toggleChatbot() {
        this.isOpen = !this.isOpen;
        const window = document.getElementById('chatbot-window');
        const toggle = document.getElementById('chatbot-toggle');

        if (this.isOpen) {
            window.classList.add('open');
            toggle.classList.add('hidden');
            document.getElementById('chatbot-input').focus();
        } else {
            this.closeChatbot();
        }
    }

    closeChatbot() {
        this.isOpen = false;
        const window = document.getElementById('chatbot-window');
        const toggle = document.getElementById('chatbot-toggle');

        window.classList.remove('open');
        toggle.classList.remove('hidden');
    }

    async handleSubmit(e) {
        e.preventDefault();
        const input = document.getElementById('chatbot-input');
        const message = input.value.trim();

        if (!message) return;

        // Ajouter le message de l'utilisateur
        this.addMessage(message, 'user');
        input.value = '';

        // Afficher l'indicateur de frappe
        this.showTypingIndicator();

        try {
            const response = await fetch('/chatbot/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.getCsrfToken()
                },
                body: JSON.stringify({ message: message })
            });

            const data = await response.json();
            this.hideTypingIndicator();

            if (data.status === 'success') {
                this.addMessage(data.response, 'bot');
            } else {
                this.addMessage('Désolé, une erreur est survenue. Veuillez réessayer plus tard.', 'bot', true);
            }
        } catch (error) {
            this.hideTypingIndicator();
            this.addMessage('Désolé, je ne peux pas me connecter au serveur. Veuillez réessayer plus tard.', 'bot', true);
            console.error('Erreur chatbot:', error);
        }
    }

    addMessage(text, sender, isError = false) {
        const messagesContainer = document.getElementById('chatbot-messages');
        const messageDiv = document.createElement('div');
        messageDiv.className = `chatbot-message ${sender}-message ${isError ? 'error-message' : ''}`;

        const avatarIcon = sender === 'user' ? 'fa-user' : 'fa-robot';
        
        messageDiv.innerHTML = `
            <div class="message-avatar">
                <i class="fas ${avatarIcon}"></i>
            </div>
            <div class="message-content">
                <p>${this.formatMessage(text)}</p>
            </div>
        `;

        messagesContainer.appendChild(messageDiv);
        this.scrollToBottom();
    }

    formatMessage(text) {
        // Échapper le HTML et convertir les retours à la ligne
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML.replace(/\n/g, '<br>');
    }

    showTypingIndicator() {
        const messagesContainer = document.getElementById('chatbot-messages');
        const typingDiv = document.createElement('div');
        typingDiv.id = 'typing-indicator';
        typingDiv.className = 'chatbot-message bot-message typing-indicator';
        typingDiv.innerHTML = `
            <div class="message-avatar">
                <i class="fas fa-robot"></i>
            </div>
            <div class="message-content">
                <div class="typing-dots">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        `;
        messagesContainer.appendChild(typingDiv);
        this.scrollToBottom();
    }

    hideTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }

    scrollToBottom() {
        const messagesContainer = document.getElementById('chatbot-messages');
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    getCsrfToken() {
        // Essayer de récupérer depuis le meta tag
        const metaToken = document.querySelector('meta[name="csrf-token"]');
        if (metaToken && metaToken.content) {
            return metaToken.content;
        }
        
        // Sinon, récupérer depuis les cookies
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            const [name, value] = cookie.trim().split('=');
            if (name === 'csrftoken') {
                return decodeURIComponent(value);
            }
        }
        return '';
    }
}

// Initialiser le chatbot quand le DOM est chargé
document.addEventListener('DOMContentLoaded', () => {
    new Chatbot();
});

