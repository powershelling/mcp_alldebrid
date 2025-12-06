# MCP AllDebrid

Un outil MCP (Micro Command Processor) pour interagir avec l'API AllDebrid.

## Fonctionnalités
- Gestion des téléchargements
- Intégration avec les services de débridage
- Automatisation des tâches liées à AllDebrid

## Installation
```bash
pip install -e .
```

## Utilisation
```python
from mcp_alldebrid import AllDebridAPI
api = AllDebridAPI("VOTRE_CLE_API")
print(api.get_user_info())
```