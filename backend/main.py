"""
This script is the entry point for the Gerenciador de Vendas backend application. It sets up
and runs the FastAPI server using Uvicorn with live reload enabled. The server is configured
to start on localhost at port 8000.
"""

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("api.app:app", host='0.0.0.0', port=8000, log_level='info', reload=True)

