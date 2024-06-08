"""
This module sets up the FastAPI application for a sales management system. 
It includes configurationsfor route handling and server initialization. 
The application serves a user management module and provides a welcoming root endpoint.
"""
from fastapi import FastAPI, status
from api.modules.users.routers.user_router import router as user_router

app = FastAPI(title='Gerenciador de Vendas')

app.include_router(user_router, prefix='/users')

@app.get('/',
         status_code=status.HTTP_200_OK,
         summary=['main'])
async def main_root():
    """
    Main root of the FastAPI application.
    
    Returns a welcome message as part of a JSON object.
    
    Returns:
        dict: A dictionary containing a welcome message.
    """
    return {'message': 'Welcome the Gerenciador de Vendas!'}
    