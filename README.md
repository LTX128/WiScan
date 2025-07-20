# WiScan 📡🔍

WiScan est une application web moderne et intuitive qui vous permet de scanner votre réseau local (Wi-Fi / LAN) pour détecter **tous les appareils connectés**.  
Elle affiche pour chaque appareil son adresse IP, MAC, nom d’hôte (si possible), type d’appareil, système d’exploitation estimé et son état (connecté ou non) — tout ça dans une interface web élégante, responsive et facile à utiliser. 

---

## ⚠️ WiScan n'est pas compatible sur téléphone !

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

2. **Installer Python** : https://www.youtube.com/watch?v=rq-36A2SvhE&t=9s

# 🛠️ Installation & utilisation


## ⚙️ Configuration importante dans app.py

**Dans le fichier `app.py`, il faut remplacer l'adresse IP utilisée dans la fonction de scan par l'adresse IP locale de votre machine sur le réseau.**

Par exemple, dans la ligne où tu définis la plage IP à scanner **( ligne 131 )**, modifie l’IP pour qu’elle corresponde à ton réseau local (par exemple 192.398.2.0/24 ou 10.0.0.0/24).

**Pour trouver ton IP locale sous Windows, ouvre un terminal (PowerShell ou cmd) et tape :**

```bash
ipconfig
```

**Cherche la ligne "IPv4 Address" de ta connexion active.**

1. **Clonez ce dépôt sur votre machine :**

```bash
git clone https://github.com/ton-utilisateur/WiScan.git
cd WiScan
```

2. **Installez les dépendances :**
```bash
pip install -r requirements.txt
```

3. **Lancez le serveur Flask :**
```bash
python app.py
```

4. **Ouvrez votre navigateur et allez à l’adresse :**
```bash
http://127.0.0.1:5000
```
---

5. **Cliquez sur le bouton "Scanner le réseau" et attendez la fin du scan (cela peut prendre 1 à 2 minutes selon le nombre d’appareils).**

ℹ️ **Notes importantes**

- Le scan réseau doit être lancé depuis un ordinateur connecté au réseau local.  
- L’interface web peut être consultée depuis un téléphone, tablette ou PC, mais le scan ne fonctionne pas sur mobile directement.  
- Pour que le scan soit complet et efficace, assurez-vous que votre firewall ne bloque pas Nmap et que vous avez les permissions nécessaires.  
- La détection des noms d’appareils et OS estimé est basée sur des heuristiques et peut ne pas être 100% précise.

🖼️ **Aperçu**

<img width="1225" height="949" alt="Capture d'écran 2025-07-20 031654" src="https://github.com/user-attachments/assets/f7b2dc29-e3ec-4a8d-b419-e5bec36590f3" />

📄 **Licence**

MIT License — libre à vous de modifier et partager.

---

Amusez-vous bien et découvrez tout ce qui se cache sur votre réseau local avec WiScan ! 🎉
