import os
import sys
import subprocess
from datetime import datetime
import ctypes
import socket
import uuid

def is_admin():
    """Vérifie si le script est exécuté en tant qu'administrateur."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        print(f"Erreur lors de la vérification des privilèges administratifs : {e}")
        return False

def run_as_admin():
    """Relance le script en mode administrateur via PowerShell."""
    script = os.path.abspath(sys.argv[0])
    print(f"Relancement du script en tant qu'administrateur : {script}")
    
    command = f'powershell -Command "Start-Process python -ArgumentList \'{script}\' -Verb RunAs"'
    
    try:
        subprocess.Popen(command, shell=True)  # Utilisation de Popen pour ne pas bloquer le script
        print("Demande de privilèges administratifs réussie.")
        return True  # Indique que le script a été relancé
    except Exception as e:
        print(f"Erreur lors de la tentative de relancer le script en tant qu'administrateur : {e}")
    
    return False

def get_ip_mac():
    """Récupère l'adresse IP et l'adresse MAC de l'ordinateur."""
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    return ip_address, mac_address

# Vérifiez si le script est déjà en cours d'exécution avec des privilèges d'administrateur
if not is_admin():
    print("Le script doit être exécuté avec les privilèges d'administrateur.")
    if run_as_admin():
        print("Instance du script relancée avec succès, maintenant nous quittons l'ancienne instance.")
        # Quitte l'ancienne instance seulement après avoir lancé la nouvelle instance
    else:
        print("Échec du relancement du script en tant qu'administrateur.")
else:
    # Une fois en mode administrateur, le script continue ici
    print("Exécution du script avec des privilèges d'administrateur...")

    # Créer un dossier de destination unique dans Documents
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_destination = os.path.join(os.path.expanduser("~"), "Documents", f"sauvegarde_registre_{timestamp}")
    os.makedirs(folder_destination, exist_ok=True)

    # Chemins des fichiers de sauvegarde
    sam_file_path = os.path.join(folder_destination, "sam.save")
    system_file_path = os.path.join(folder_destination, "system.save")
    ip_mac_file_path = os.path.join(folder_destination, "ip_mac_info.txt")

    # Sauvegarder les registres SAM et SYSTEM
    def save_registry_hive(hive, save_path):
        try:
            subprocess.run(["reg", "save", hive, save_path], check=True, shell=True)
            print(f"Sauvegarde du registre {hive} réussie dans {save_path}")
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de la sauvegarde du registre {hive} : {e}")
        except Exception as e:
            print(f"Erreur inattendue lors de la sauvegarde du registre {hive} : {e}")

    # Sauvegarde des clés de registre
    print("Début de la sauvegarde des clés de registre...")
    save_registry_hive("HKLM\\SAM", sam_file_path)
    save_registry_hive("HKLM\\SYSTEM", system_file_path)

    # Récupération de l'adresse IP et de l'adresse MAC
    ip_address, mac_address = get_ip_mac()

    # Écriture des informations IP et MAC dans un fichier
    with open(ip_mac_file_path, "w") as f:
        f.write(f"Adresse IP : {ip_address}\n")
        f.write(f"Adresse MAC : {mac_address}\n")

    print(f"Les fichiers de sauvegarde sont enregistrés dans le dossier : {folder_destination}")
    print(f"Informations IP et MAC enregistrées dans : {ip_mac_file_path}")
