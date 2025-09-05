from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="openai/gpt-oss-20b"
)

def get_exercises(data):
    sensor = data.get("sensor", "unknown")
    values = data.get("values", [])
    units = data.get("units", "unknown")
    student_level = data.get("student_level", "unknown")
    exercise_context = data.get("exercise_context", "unknown")

    prompt = f"""
  Eres un profesor de ciencias y matematicas que recibe datos y contexto de sensores que usaron los alumnos para medir del ambiente:
  Sensor: {sensor}
  Valores: {values}
  Unidad de medida del sensor: {units}
  Nivel de los estudiantes: {student_level}
  Contexto del ejercicio: {exercise_context}

Responde en formato JSON con los ejercicios matematicos que los estudiantes deberan resolver segun su nivel. Responde con la siguiente estructura:
[
  
    "pregunta": "¿Cuánto es la suma de los valores medidos?",
    "opciones": ["Opcion1", "Opcion2", "Opcion3"],
    "respuesta": "Opcion1"
  


    "pregunta": "Por que los valores estan en descenso?",
    "opciones": ["Opcion1", "Opcion2", "Opcion3"],
    "respuesta": "Opcion1"
  
]

las preguntas deben estar relacionadas con el contexto del ejercicio y los datos proporcionados por los estudiantes. Esto con el proposito de que los estudiantes puedan conectar mejor la teoria con la realidad.
    """
    response = model.invoke(prompt)
    return response.content