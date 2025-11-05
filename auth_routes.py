from fastapi import APIRouter

auth_router = APIRouter(prefix="/autenticacao", tags=["autenticacao"])

@auth_router.get("/")
async def autenticacao():
    
    """ Rota de autenticacao do sistema"""

    return {"mensagem": "Acesso a rota de autenticacao", "autenticado": False}