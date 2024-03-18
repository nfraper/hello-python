from fastapi import FastAPI

app = FastAPI()

#accedemos al contexto de fastAPI con @app
@app.get("/")  # con "/" estamos llamando a la raíz, es decir, a localhost
async def root():
    return "¡Hola FastAPI!"

@app.get("/url")  # con "/url" estamos llamando a ttp://127.0.0.1:8000/url
async def url():
    return {"url_curso":"lo_que_sea"}