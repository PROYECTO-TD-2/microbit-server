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


    message = [
        ('system',"Eres un profesor de ciencias y matemáticas que genera ejercicios educativos en formato JSON. Para generar los ejercios debes basrte unicamente n los libros. Es un verdadero tutor de matematica presenta ejercicios resueltos para que fijes tecnicas operatorias y metodos de razonamiento. La redaccion detallada de las soluciones te servira de modelo para los ejercicios que tu realices. "),
        ('human',f"""
        Sensor: {sensor}
        Valores: {values}
        Unidad: {units}
        Nivel: {student_level}
        Contexto: {exercise_context}

        Genera ejercicios matemáticos en JSON siguiendo esta estructura:
        [
          {{
            "pregunta": "...",
            "opciones": ["...", "...", "..."],
            "respuesta": "..."
          }}
        ]
        """)
    ]
    response = model.invoke(message)
    return response.content