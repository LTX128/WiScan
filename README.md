# WiScan 📡🔍

WiScan est une application web moderne et intuitive qui te permet de scanner ton réseau local (Wi-Fi / LAN) pour détecter **tous les appareils connectés**.  
Elle affiche pour chaque appareil son adresse IP, MAC, nom d’hôte (si possible), type d’appareil, système d’exploitation estimé et son état (connecté ou non) — tout ça dans une interface web élégante, responsive et facile à utiliser.  

---

## 🚀 Fonctionnalités

- Scan automatique du réseau local  
- Affichage dynamique en temps réel des appareils détectés  
- Informations complètes : IP, MAC, nom, type d’appareil, OS estimé, état connecté/non  
- Interface moderne, fluide et compatible mobile  
- Indication claire que le scan peut prendre du temps selon la taille du réseau  

---

## ⚠️ Prérequis importants

1. **Installer Nmap**  
WiScan utilise l’outil `nmap` pour scanner le réseau.  
Tu dois installer [Nmap](https://nmap.org/download.html) sur ta machine et **ajouter le dossier contenant `nmap.exe` au PATH système** pour que l’application puisse l’utiliser.  
   
   - Sous Windows, ça ressemble souvent à :  
     `C:\Program Files (x86)\Nmap`  
   - Pense à redémarrer ton terminal/PC après ajout au PATH.  
   - Pour vérifier, tape dans un terminal :  
     ```bash
     nmap --version
     ```
     Tu dois voir la version de nmap s’afficher.

2. **Python 3.8+ installé**

3. **Installer les dépendances Python**  
Dans le dossier du projet, lance :  
```bash
pip install -r requirements.txt
```
## 🛠️ Installation & utilisation
Clone ce dépôt sur ta machine :

bash
Copier
Modifier
git clone https://github.com/ton-utilisateur/WiScan.git
cd WiScan
Installe les dépendances :

bash
Copier
Modifier
pip install -r requirements.txt
Lance le serveur Flask :

bash
Copier
Modifier
python app.py
Ouvre ton navigateur et va à l’adresse :

cpp
Copier
Modifier
http://127.0.0.1:5000
