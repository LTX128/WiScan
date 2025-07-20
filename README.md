# WiScan 📡🔍

WiScan est une application web moderne et intuitive qui vous permet de scanner votre réseau local (Wi-Fi / LAN) pour détecter **tous les appareils connectés**.  
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

2. **Installer Python** : https://www.youtube.com/watch?v=rq-36A2SvhE&t=9s

## 🛠️ Installation & utilisation

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



📄 **Licence**

MIT License — libre à vous de modifier et partager.

---

Amusez-vous bien et découvrez tout ce qui se cache sur votre réseau local avec WiScan ! 🎉
