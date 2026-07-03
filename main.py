from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {
        "matricula": "2024118ISINF0065",
        "nome": "Nayanne de Carvalho Cruz"
    }