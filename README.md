# 🌐 MCP AllDebrid
**[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![Python](https://img.shields.io/badge/python-3.8+-yellow.svg)](https://www.python.org/downloads/)**

Un **Micro Command Processor (MCP)** pour interagir avec l’API **AllDebrid**, conçu pour automatiser et simplifier la gestion des téléchargements, le débridage de liens, et l’intégration avec tes applications Python.

---

## 📋 Description
`mcp_alldebrid` est une bibliothèque et un serveur **FastAPI** qui permet d’interagir facilement avec l’API AllDebrid.
Idéal pour :
- **Automatiser** les téléchargements et le débridage.
- **Intégrer** AllDebrid dans tes projets existants.
- **Gérer** tes fichiers et liens de manière programmatique.

---

## ✨ Fonctionnalités
| Fonctionnalité               | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| **Gestion des utilisateurs** | Récupérer les informations du compte (quota, historique, etc.).           |
| **Débridage de liens**       | Générer des liens de téléchargement directs depuis des liens cryptés.      |
| **Téléchargements**          | Lancer et suivre des téléchargements depuis des magnets ou liens torents.  |
| **Automatisation**           | Planifier des tâches (ex: débridage automatique de liens).                 |
| **Webhooks**                 | Recevoir des notifications en temps réel (téléchargement terminé, etc.).  |
| **Intégration FastAPI**      | API REST prête à l’emploi pour une utilisation en réseau.                  |

---

## 🛠️ Installation
### Prérequis
- Python **3.8+**
- Une **clé API AllDebrid** ([obtenir une clé](https://alldebrid.com/apikeys))

### Étapes
1. Cloner le dépôt :
   ```bash
   git clone https://github.com/powershelling/mcp_alldebrid.git
   cd mcp_alldebrid
   ```
2. Installer les dépendances :
   ```bash
   pip install -e .
   ```
3. Configurer ton environnement :
   ```bash
   echo "ALLDEBRID_API_KEY=ta_clé_api" > .env
   ```

---

## 🚀 Utilisation
### Exemple 1 : Récupérer les infos utilisateur
```python
from mcp_alldebrid import AllDebridAPI

api = AllDebridAPI()
user_info = api.get_user_info()
print(f"Pseudo: {user_info.username}, Quota: {user_info.quota}")
```

### Exemple 2 : Débrider un lien
```python
link = "https://exemple.com/file.crypted"
unlocked_link = api.unlock_link(link)
print(f"Lien débridé: {unlocked_link}")
```

### Exemple 3 : Lancer un téléchargement
```python
magnet = "magnet:?xt=urn:btih:..."
download_id = api.add_magnet(magnet)
print(f"Téléchargement lancé (ID: {download_id})")
```

### Exemple 4 : Utiliser l’API FastAPI
Lance le serveur :
```bash
uvicorn server:app --reload
```
- Accède à la doc Swagger : [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📂 Structure du Projet
```
mcp_alldebrid/
├── server.py       # Serveur FastAPI
├── pyproject.toml  # Configuration Python
├── README.md       # Documentation
└── LICENSE         # Licence MIT
```

---

## 📄 Licence
Ce projet est sous licence **MIT** – libre à l’usage, modification et distribution.
*(Voir [LICENSE](LICENSE) pour plus de détails.)*

---

## 🤝 Contribution
Les **pull requests** sont les bienvenues !
Pour signaler un bug ou proposer une feature, ouvre une **[issue](https://github.com/powershelling/mcp_alldebrid/issues)**.