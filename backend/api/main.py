import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api.modules.users.routers.user_router import router as user_router

from fastapi import FastAPI, status

app = FastAPI(title='Gerenciador de Vendas')

app.include_router(user_router, prefix='/users')

@app.get('/',
         status_code=status.HTTP_200_OK,
         summary=['main'])
async def main_root():
    return {'message': 'Welcome the Gerenciador de Vendas!'}

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)