from fastapi import FastAPI
from llm import get_exercises
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O puedes restringir a ["http://localhost:3000"] por ejemplo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Endpoint para obtener datos
@app.post("/generate")
def generate(data: dict):
    exercises = get_exercises(data)
    print(data)
    return {"message": "Parámetros recibidos", "data": data, "exercises": exercises}
