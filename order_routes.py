from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/")
async def pedidos():

    """ Rota padrão de pedidos do sistema"""
    
    return {"mensagem": "Acesso a lista de pedidos"}