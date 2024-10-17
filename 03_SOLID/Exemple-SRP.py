
"""Single responsability principe (SRP) : chaque classe doit avoir une seule responsabilité ou raison de changer."""

# Classe de base pour les notifications
class NotificationSender:
    def send(self, message):
        pass
    
# Classe pour envoyer des notifications par email
class EmailSender(NotificationSender):
    def send(self, message):
        print(f"Envoi d'un email : {message}")

# Classe pour envoyer des notifications par SMS
class SMSSender(NotificationSender):
    def send(self, message):
        print(f"Envoi d'un SMS : {message}")

# Nouvelle classe ajoutée pour l'envoi par push notification
class PushNotificationSender(NotificationSender):
    def send(self, message):
        print(f"Envoi d'une notification push : {message}")
