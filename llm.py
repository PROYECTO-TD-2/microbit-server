from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import json
import re
#comando para levantar el servidor: uvicorn api:app --reload
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
        ('system', """Eres un profesor de ciencias y matemáticas..."""),
        ('human', f"""
        Sensor: {sensor}
        Valores: {values}
        Unidad: {units}
        Nivel: {student_level}
        Contexto: {exercise_context}

        Genera un ejercicio matemático en JSON siguiendo esta estructura:
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
    raw = response.content.strip()

    #Eliminar los ```json y ```
    if raw.startswith("```"):
        raw = re.sub(r"^```[a-zA-Z]*\n", "", raw)
        raw = raw.rstrip("`").strip()
        if raw.endswith("```"):
            raw = raw[:-3].strip()

    try:
        exercises = json.loads(raw)
        print("Parsed JSON successfully.")
        print(exercises)
    except json.JSONDecodeError:
        exercises = {"raw_response": response.content}  # fallback

    return exercises