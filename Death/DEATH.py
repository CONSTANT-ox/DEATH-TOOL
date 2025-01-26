import socket
import whois
import os
import requests
from datetime import datetime
import subprocess
import hashlib
from colorama import init, Fore
import webbrowser  # Pour ouvrir une recherche dans un navigateur

# Initialisation de colorama
init(autoreset=True)

# Codes couleur colorama pour la couleur violette
PURPLE = Fore.MAGENTA

def banner():
    print(f"""{PURPLE}
    ▓█████▄ ▓█████ ▄▄▄     ▄▄▄█████▓ ██░ ██ 
    ▒██▀ ██▌▓█   ▀▒████▄   ▓  ██▒ ▓▒▓██░ ██▒
    ░██   █▌▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██▀▀██░
    ░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ░▓█ ░██ 
    ░▒████▓ ░▒████▒▓█   ▓██▒ ▒██▒ ░ ░▓█▒░██▓
     ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░    ▒ ░░▒░▒
     ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░   ░     ▒ ░▒░ ░
     ░ ░  ░    ░    ░   ▒    ░       ░  ░░ ░
       ░       ░  ░     ░  ░         ░  ░  ░
     ░                                      
    BY VENOM
    {PURPLE}""")

def ip_info():
    ip = input(f"{PURPLE}Entrez une adresse IP à analyser: {PURPLE}")
    try:
        hostname = socket.gethostbyaddr(ip)
        print(f"{PURPLE}Informations sur l'IP {ip}:\nHostname: {hostname}{PURPLE}")
    except socket.herror:
        print(f"{PURPLE}Impossible de résoudre l'IP {ip}.{PURPLE}")
    except socket.gaierror:
        print(f"{PURPLE}L'IP {ip} est invalide.{PURPLE}")

def whois_info():
    domain = input(f"{PURPLE}Entrez un domaine à rechercher (ex: example.com): {PURPLE}")
    try:
        w = whois.whois(domain)
        print(f"{PURPLE}Informations WHOIS pour {domain}:\n{w}{PURPLE}")
    except Exception as e:
        print(f"{PURPLE}Erreur lors de la recherche WHOIS: {e}{PURPLE}")

def dns_lookup():
    domain = input(f"{PURPLE}Entrez un domaine à rechercher via DNS: {PURPLE}")
    try:
        result = subprocess.check_output(['nslookup', domain])
        print(f"{PURPLE}Résultat DNS pour {domain} :\n{result.decode()}{PURPLE}")
    except subprocess.CalledProcessError as e:
        print(f"{PURPLE}Erreur lors de la recherche DNS pour {domain}: {e}{PURPLE}")

def search_tool():
    search_term = input(f"{PURPLE}Entrez un terme de recherche: {PURPLE}")
    query = search_term.replace(" ", "+")  # Prépare le terme pour la recherche
    url = f"https://www.google.com/search?q={query}"
    print(f"{PURPLE}Ouverture du navigateur pour la recherche...{PURPLE}")
    webbrowser.open(url)  # Ouvre la recherche dans le navigateur par défaut

def port_scan():
    target = input(f"{PURPLE}Entrez l'adresse IP ou le domaine à scanner: {PURPLE}")
    try:
        os.system(f"nmap {target}")
    except Exception as e:
        print(f"{PURPLE}Erreur lors du scan de port pour {target}: {e}{PURPLE}")

def data_breach_check():
    email = input(f"{PURPLE}Entrez un email à vérifier pour une fuite de données: {PURPLE}")
    url = f"https://haveibeenpwned.com/api/v2/breachedaccount/{email}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{PURPLE}L'email {email} a été impliqué dans une ou plusieurs fuites de données.{PURPLE}")
            print(response.json())
        else:
            print(f"{PURPLE}L'email {email} n'a pas été impliqué dans des fuites de données.{PURPLE}")
    except Exception as e:
        print(f"{PURPLE}Erreur lors de la vérification des fuites de données: {e}{PURPLE}")

def md5_hash_check():
    md5_hash = input(f"{PURPLE}Entrez un hash MD5 à vérifier: {PURPLE}")
    url = f"https://www.md5online.org/md5-decrypt.html?md5={md5_hash}"
    try:
        response = requests.get(url)
        print(f"{PURPLE}Résultat de la vérification du hash MD5: {response.text}{PURPLE}")
    except Exception as e:
        print(f"{PURPLE}Erreur lors de la vérification du hash MD5: {e}{PURPLE}")

def screenshot_grabber():
    url = input(f"{PURPLE}Entrez une URL pour obtenir une capture d'écran: {PURPLE}")
    try:
        # Placeholder: Implémenter une méthode pour obtenir une capture d'écran d'un site
        print(f"{PURPLE}Obtenir une capture d'écran de {url}{PURPLE}")
    except Exception as e:
        print(f"{PURPLE}Erreur lors de la capture d'écran: {e}{PURPLE}")

def subdomain_enum():
    domain = input(f"{PURPLE}Entrez un domaine pour l'énumération des sous-domaines: {PURPLE}")
    try:
        os.system(f"sublist3r -d {domain}")
    except Exception as e:
        print(f"{PURPLE}Erreur lors de l'énumération des sous-domaines pour {domain}: {e}{PURPLE}")

def check_ssl_cert():
    domain = input(f"{PURPLE}Entrez un domaine pour vérifier le certificat SSL: {PURPLE}")
    try:
        response = requests.get(f"https://{domain}", verify=True)
        print(f"{PURPLE}Certificat SSL valide pour {domain}.{PURPLE}")
    except requests.exceptions.SSLError:
        print(f"{PURPLE}Le certificat SSL pour {domain} est invalide.{PURPLE}")
    except Exception as e:
        print(f"{PURPLE}Erreur lors de la vérification SSL pour {domain}: {e}{PURPLE}")

def osint_menu():
    banner()
    print(f"\n{PURPLE}Sélectionnez un outil OSINT à utiliser :{PURPLE}")
    print(f"{PURPLE}1. Analyse d'IP{PURPLE}")
    print(f"{PURPLE}2. WHOIS (domaine){PURPLE}")
    print(f"{PURPLE}3. Recherche DNS{PURPLE}")
    print(f"{PURPLE}4. Recherche{PURPLE}")
    print(f"{PURPLE}5. Scan de ports{PURPLE}")
    print(f"{PURPLE}6. Vérification des fuites de données{PURPLE}")
    print(f"{PURPLE}7. Vérification de hash MD5{PURPLE}")
    print(f"{PURPLE}8. Capture d'écran d'URL (placeholder){PURPLE}")
    print(f"{PURPLE}9. Énumération des sous-domaines{PURPLE}")
    print(f"{PURPLE}10. Vérification SSL{PURPLE}")
    print(f"{PURPLE}11. Quitter{PURPLE}")
    
    choice = input(f"{PURPLE}Entrez le numéro de l'option souhaitée: {PURPLE}")
    
    if choice == "1":
        ip_info()
    elif choice == "2":
        whois_info()
    elif choice == "3":
        dns_lookup()
    elif choice == "4":
        search_tool()
    elif choice == "5":
        port_scan()
    elif choice == "6":
        data_breach_check()
    elif choice == "7":
        md5_hash_check()
    elif choice == "8":
        screenshot_grabber()
    elif choice == "9":
        subdomain_enum()
    elif choice == "10":
        check_ssl_cert()
    elif choice == "11":
        print(f"{PURPLE}Merci d'avoir utilisé le panel OSINT. Au revoir!{PURPLE}")
        exit()
    else:
        print(f"{PURPLE}Option invalide. Veuillez réessayer.{PURPLE}")
    
    osint_menu()  # Redemander après l'exécution

if __name__ == "__main__":
    osint_menu()
