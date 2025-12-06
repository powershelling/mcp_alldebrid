"""
Serveur MCP pour AllDebrid
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInfo(BaseModel):
    username: str
    email: str

@app.get("/user", response_model=UserInfo)
async def get_user_info():
    """Récupère les informations utilisateur depuis AllDebrid."""
    # Logique d'appel à l'API AllDebrid ici
    return {"username": "exemple", "email": "user@example.com"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)