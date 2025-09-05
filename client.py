import requests

# Ejemplo GET (consulta de datos disponibles en la API)
response = requests.get("http://localhost:8000/data")
print(response.json())

# Datos más realistas de medición de luz
data = {
  "sensor": "luz",
  "values": [
    {"timestamp": "2023-03-01T09:15:00Z", "value": 320.5},   # Aula iluminada con luces
    {"timestamp": "2023-03-01T09:20:00Z", "value": 1120.8},  # Cerca de una ventana
    {"timestamp": "2023-03-01T09:25:00Z", "value": 15230.2}  # Exterior bajo sol directo
  ],
  "units": "lux",
  "student_level": "secundaria",
  "exercise_context": "Los alumnos midieron la luz en diferentes lugares de la escuela: dentro del aula, junto a la ventana y en el patio bajo el sol."
}

# Ejemplo POST (enviar datos para procesar)
response = requests.post("http://localhost:8000/generate", json=data)
print(response.json())
