import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Informations de l'expéditeur et du destinataire
sender_email = "jesuisjusteunteste@gmail.com"  # Remplace par ton adresse email
receiver_email = "anas.sghir.2912@gmail.com"  # Adresse du destinataire
password = "@JESUISJUSTEUNTESTE-2024"  # Remplace par ton mot de passe

# Créer un objet MIME
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Test Email"

# Corps du message
body = "Ceci est un email de test envoyé depuis Python!"
msg.attach(MIMEText(body, 'plain'))

try:
    # Établir une connexion avec le serveur SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Pour Gmail
    server.starttls()  # Activer la sécurité
    server.login(sender_email, password)  # Connexion
    text = msg.as_string()  # Convertir le message en string
    server.sendmail(sender_email, receiver_email, text)  # Envoyer l'email
    print("Email envoyé avec succès!")
except Exception as e:
    print(f"Erreur lors de l'envoi de l'email : {e}")
finally:
    server.quit()  # Fermer la connexion
