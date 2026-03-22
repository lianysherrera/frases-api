from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(
    title="Frases API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

frases = [
    {"id": 1, "frase": "Cree en ti, incluso cuando nadie más lo haga"},
    {"id": 2, "frase": "Cada paso cuenta, por pequeño que sea"},
    {"id": 3, "frase": "Hoy es un buen día para empezar"},
    {"id": 4, "frase": "No te rindas, lo mejor está por venir"},
    {"id": 5, "frase": "La disciplina vence al talento sin esfuerzo"},
    {"id": 6, "frase": "Todo logro comienza con la decisión de intentarlo"},
    {"id": 7, "frase": "Hazlo con miedo, pero hazlo"},
    {"id": 8, "frase": "Tu límite está en tu mente"},
    {"id": 9, "frase": "El progreso es mejor que la perfección"},
    {"id": 10, "frase": "Los sueños no funcionan si tú no trabajas"},
    {"id": 11, "frase": "Confía en el proceso"},
    {"id": 12, "frase": "No compares tu inicio con el final de otros"},
    {"id": 13, "frase": "La constancia es la clave del éxito"},
    {"id": 14, "frase": "Eres más fuerte de lo que crees"},
    {"id": 15, "frase": "Convierte los obstáculos en oportunidades"},
    {"id": 16, "frase": "El éxito es la suma de pequeños esfuerzos diarios"},
    {"id": 17, "frase": "Aprende de cada caída"},
    {"id": 18, "frase": "Rodéate de energía positiva"},
    {"id": 19, "frase": "Lo imposible solo tarda un poco más"},
    {"id": 20, "frase": "Haz que suceda"},
    {"id": 21, "frase": "Cada día es una nueva oportunidad"},
    {"id": 22, "frase": "No dejes que el miedo decida por ti"},
    {"id": 23, "frase": "Mantén la vista en tus metas"},
    {"id": 24, "frase": "Tu actitud define tu dirección"},
    {"id": 25, "frase": "Nunca es tarde para empezar de nuevo"},
    {"id": 26, "frase": "Sé paciente, todo llega"},
    {"id": 27, "frase": "Atrévete a salir de tu zona de confort"},
    {"id": 28, "frase": "Cree en el poder de tus sueños"},
    {"id": 29, "frase": "La motivación te inicia, el hábito te mantiene"},
    {"id": 30, "frase": "Hoy puedes ser mejor que ayer"},
    {"id": 31, "frase": "La acción vence a la duda"},
    {"id": 32, "frase": "El cambio comienza contigo"},
    {"id": 33, "frase": "Hazlo por ti"},
    {"id": 34, "frase": "La perseverancia abre puertas"},
    {"id": 35, "frase": "No hay éxito sin esfuerzo"},
    {"id": 36, "frase": "El fracaso es parte del camino"},
    {"id": 37, "frase": "Sigue adelante, incluso cuando sea difícil"},
    {"id": 38, "frase": "Tú decides hasta dónde llegar"},
    {"id": 39, "frase": "No te detengas hasta estar orgulloso"},
    {"id": 40, "frase": "Lo mejor está en proceso"},
    {"id": 41, "frase": "Da lo mejor de ti cada día"},
    {"id": 42, "frase": "La mente positiva crea resultados positivos"},
    {"id": 43, "frase": "No sueñes tu vida, vive tu sueño"},
    {"id": 44, "frase": "Haz que cada día cuente"},
    {"id": 45, "frase": "Todo es posible con determinación"},
    {"id": 46, "frase": "Cree, actúa y logra"},
    {"id": 47, "frase": "El éxito empieza con un paso"},
    {"id": 48, "frase": "Nunca subestimes tu potencial"},
    {"id": 49, "frase": "La clave es no rendirse"},
    {"id": 50, "frase": "Tú tienes el control de tu destino"},
]

@app.get("/frases", tags=["frases"], summary="Obtener todas las frases", description="Devuelve la lista completa de frases motivadoras.")
def get_phrase():
    return frases

@app.get("/frases/aleatoria", tags=["frases"], summary="Frase aleatoria", description="Devuelve una frase motivadora al azar")
def phrase_random():
    return random.choice(frases)

@app.post("/frases", tags=["frases"], summary="Añadir frase", description="Añade una nueva frase a la lista.")
def create_phrase(nueva_frase: dict):
    nueva_frase["id"] = len(frases) + 1
    frases.append(nueva_frase)
    return {"mensaje": "Frase añadida", "frase": nueva_frase}

@app.delete("/frases/{id}", tags=["frases"], summary="Eliminar frase", description="Elimina una frase por su ID. Devuelve 404 si no existe.")
def delete_phrase(id: int):
    for frase in frases:
        if frase["id"] == id:
            frases.remove(frase)
            return {"mensaje": "Frase eliminada"}
    raise HTTPException(status_code=404, detail="Frase no encontrada")